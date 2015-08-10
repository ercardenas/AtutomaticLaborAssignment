#!/usr/bin/python
#
# example code to accompany https://developer.surveymonkey.com/mashery/guide_polling
# 
# developed for Python 2.6+
# 
# The MIT License (MIT)

# Copyright (c) <2014> <SurveyMonkey>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import requests # http://docs.python-requests.org/en/latest/user/install/
import json
import pprint
import __future__ #for compatibility with Python 2.6 & 2.7
from time import gmtime, mktime, sleep, time
from datetime import timedelta, datetime	
from itertools import cycle


class rate_wait:
    """Non-threadsafe way to wait until the next time a 
       rate-limited function should be called.
       Initialize by passing the maxi mum calls per second."""
       
    def __init__(self, maxPerSecond):
        self.last_called = 0.0
        self.min_interval = 1.0 / float(maxPerSecond)
        
    def wait(self):
        time_to_wait = self.last_called + self.min_interval - time() 
        if time_to_wait > 0:
            sleep(time_to_wait)
        self.last_called_is_now()
        
    def last_called_is_now(self):
        self.last_called = time()

def polling():
    USER_ACCESS_TOKEN = "paTBz61kMlD0mPWrsaHR3921EuYbHlBvqU0GDZQ.5nahBvB1GbdZpbh2WnOzXY4SzVqw2B-UZ1YP0JHU72xSCB-hZ93w-cyQUnTtyk99rZ8="
    API_KEY = "wy5kg6tj3jvfe4sdprjzwmwc"

    client = requests.session()
    client.headers = {
        "Authorization": "bearer %s" % USER_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    client.params = {
        "api_key": API_KEY
    }

    SURVEY_TITLE = "Labor Availability Form" #use get_survey_list to find the survey ID
    HOST = "https://api.surveymonkey.net"
    MAX_REQUESTS_PER_SECOND = 2
    POLL_CYCLE_LENGTH_IN_MINUTES = 60.0
     
    # initialize objects used later on
    pp = pprint.PrettyPrinter(indent=4) 
    limiter = rate_wait(MAX_REQUESTS_PER_SECOND) 

    # add paths to HOST to create the two API endpoint URIs
    surveys_uri = "%s/v2/surveys/get_survey_list" % HOST
    details_uri = "%s/v2/surveys/get_survey_details" % HOST
    respondent_uri = "%s/v2/surveys/get_respondent_list" % HOST
    response_uri = "%s/v2/surveys/get_responses" % HOST

    # find the survey ID by title
    survey_request = {}
    survey_request["title"] = SURVEY_TITLE 
    survey_request["fields"] = ["title","date_created"]
    limiter.wait() #avoid making requests too quickly
    try:
        survey_data = client.post(surveys_uri, data=json.dumps(survey_request))
    except requests.exceptions.RequestException as e:
        print("Error finding survey by title: ",SURVEY_TITLE," Exception: ",e)
        exit()
    limiter.last_called_is_now() #save the time when request completes
    if survey_data.status_code == 200: #the API responded
        survey_json = survey_data.json()
        number_of_surveys_found = len(survey_json["data"]["surveys"])
        if number_of_surveys_found > 1: #title search no specific enough
            print("Number of surveys found matching \"",SURVEY_TITLE,
                  "\" is ",number_of_surveys_found,".")
            print("Please configure a more specific title.")
            print("note: searches are case insensitive.")
            print()
            for survey in survey_json["data"]["surveys"]:
                print("Found: ",survey["title"])
            exit()
        elif number_of_surveys_found == 0: #title search too specific or wrong account
            print("No survey was found matching the title: \"",SURVEY_TITLE,
                  "\" for the authorized SurveyMonkey account.")
            exit()
    else: #got an error before reaching the API. message below should help determine why.
        print("Error finding suvery by title: \"",SURVEY_TITLE,"\"")
        print(" Response code: ",survey_data.response_code," Message: ", survey_data.text)
        exit()

    # found one and only one survey matching SURVEY_TITLE  
    # save the survey_id for use in requests for respondents & responses
    survey_id = survey_json["data"]["surveys"][0]["survey_id"]
    # start checking for respondents at the time the survey was created
    last_date_checked = survey_json["data"]["surveys"][0]["date_created"]
    print("Found survey title: ",SURVEY_TITLE," survey_id: ",survey_id," created: ",last_date_checked)

    # survey_request = {}
    # survey_request["survey_id"] = survey_id
    # survey = client.post(details_uri, data=json.dumps(survey_request))
    # survey_data = survey.json()
    # survey_answers = survey_data['data']['pages'][0]['questions'][2]['answers']
    # matrix = dict((survey_answers[r]['answer_id'], \
    #               dict((survey_answers[c]['answer_id'], (0)) \ 
    #                 for c in range(17,24))) \
    #             for r in range(0,17))
    # pp.pprint(matrix)

    # set up the initial post data for respondents
    respondent_request = {} #create empty associative array/map/dictionary
    respondent_request["survey_id"] = survey_id #key:"survey_id", value:survey_id
    respondent_request["fields"] = ["status"]

    # set up the initial post data for responses
    response_request = {}
    response_request["survey_id"] = survey_id

    # get time 5 seconds ago for use as the "end_modified_date"
    # in string format for API - this will ensure SurveyMonkey 
    # is done processing all responses between start & end dates
    five_seconds_ago = (datetime.fromtimestamp(mktime(gmtime())) - 
                        timedelta(seconds = 5)).strftime('%Y-%m-%d %H:%M:%S')
    respondent_request["start_modified_date"] = last_date_checked
    respondent_request["end_modified_date"] = five_seconds_ago
    # get responses modified at or later than start_modified_date and
    # responses EARLIER than (but not at) end_modified_date
    last_date_checked = five_seconds_ago #save for next poll cycle
     
    respondents_cur_page = 1 #start at page 1
    respondent_ids = [] #initialize empty respondent list for this poll cycle
    while True: #get pages of respondents until there are no more
        respondent_request["page"] = respondents_cur_page
        limiter.wait() #avoid making requests too quickly
        respondent_data = client.post(respondent_uri,
                                      data=json.dumps(respondent_request)) 
        limiter.last_called_is_now()
        respondent_json = respondent_data.json() #decode JSON in respondent_data
        if len(respondent_json["data"]["respondents"]) == 0:
            break #all respondents gotten, break out of "while True:" loop
        
        for respondent in respondent_json["data"]["respondents"]:
            # only want finished responses
            # discover the meaning of finished surveys http://goo.gl/JoRWb5
            if respondent["status"] == "completed":
                respondent_ids.append(respondent["respondent_id"])
        respondents_cur_page += 1 #add 1 to respondents_cur_page
     
    # get_responses can only take in 100 respondent_ids, so 
    # we need to batch these requests in chunks of 100
    start_pos = 0 # starts at 0, 0 is the first respondent
    respondent_count = len(respondent_ids) # starts at 1
    # initialize blank list of responses for this poll cycle
    output_response_list = []
    while start_pos < respondent_count: #see NOTE below
        response_request["respondent_ids"] = \
            respondent_ids[start_pos:start_pos + 100] #see NOTE
        limiter.wait()
        response_data = client.post(response_uri, 
                                    data=json.dumps(response_request))
        limiter.last_called_is_now()
        response_json = response_data.json()
        for response in response_json["data"]:
            output_response_list.append(response)
        start_pos += 100

    return output_response_list



    # off by one bugs are a common software failure pattern (bug)
    # http://en.wikipedia.org/wiki/Off-by-one_error
    # the NOTE below discusses the correctness of this code in Python
    # Porting this code to other languages will require care when 
    # considering this section of code.

    # NOTE
    # start_pos starts at 0 http://en.wikipedia.org/wiki/Zero-based_numbering
    # while respondent_count is a natural number and starts at 1.
    # If both were zero-based, we would need to compare them with "<=" since
    # Python includes the start position when slicing an array but EXCLUDES 
    # the end position. However, since start_pos has a value one less than the
    # cardinal number of the respondent to which it refers, using "<" is 
    # appropriate in Python.