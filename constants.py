#!/usr/bin/python

__author__ = "Erick Cardenas"
__email__ = "ecardenas@utexas.edu"

# A list of all the existing labors in Halstead
# Each member of the list is another list in which
# the first elemenet is the name of the labor
# and the second element is the number of people required
LABORS_LIST = [["Mon - Morning Hobbit - 8-9am", 1], 
      ["Tues - Morning Hobbit - 8-9am", 1],
      ["Wed - Morning Hobbit - 8-9am", 1],
      ["Thurs - Morning Hobbit - 8-9am", 1],
      ["Fri - Morning Hobbit - 8-9am", 1],
      ["Sun - Morning Hobbit - 9-10am", 2],
      ["Mon - Lunch Cook - 9-10am", 3],
      ["Tues - Lunch Cook - 9-10am", 3],
      ["Wed - Lunch Cook - 9-10am", 3],
      ["Thurs - Lunch Cook - 9-10am", 3],
      ["Fri - Lunch Cook - 9-10am", 3],
      ["Sat - Morning Hobbit - 9-10am", 2],
      ["Sun - Brunch Cook - 10-11am", 3],
      ["Mon - Lunch Cook - 10-11am", 3],
      ["Tues - Lunch Cook - 10-11am", 3],
      ["Wed - Lunch Cook - 10-11am", 3],
      ["Thurs - Lunch Cook - 10-11am", 3],
      ["Fri - Lunch Cook - 10-11am", 3],
      ["Sat - Brunch Cook - 10-11am", 3],
      ["Sun - Brunch Cook - 11am-12pm", 3],
      ["Sat - Brunch Cook - 11am-12pm", 3],
      ["Mon - Lunch Clean - 12-1pm", 3],
      ["Tues - Lunch Clean - 12-1pm", 3],
      ["Wed - Lunch Clean - 12-1pm", 3],
      ["Thurs - Lunch Clean - 12-1pm", 3],
      ["Fri - Lunch Clean - 12-1pm", 3],
      ["Sun - Brunch Clean - 1-2pm", 3],
      ["Mon - Lunch Clean - 1-2pm", 3],
      ["Tues - Lunch Clean - 1-2pm", 3],
      ["Wed - Lunch Clean - 1-2pm", 3],
      ["Thurs - Lunch Clean - 1-2pm", 3],
      ["Fri - Lunch Clean - 1-2pm", 3],
      ["Sat - Brunch Clean - 1-2pm", 3],
      ["Sun - Brunch Clean - 2-3pm", 3],
      ["Mon - Dinner Cook - 2-3pm", 3],
      ["Tues - Dinner Cook - 2-3pm", 3],
      ["Wed - Dinner Cook - 2-3pm", 3],
      ["Thurs - Dinner Cook - 2-3pm", 3],
      ["Fri - Dinner Cook - 2-3pm", 3],
      ["Sat - Brunch Clean - 2-3pm", 3],
      ["Mon - Dinner Cook - 3-4pm", 3],
      ["Tues - Dinner Cook - 3-4pm", 3],
      ["Wed - Dinner Cook - 3-4pm", 3],
      ["Thurs - Dinner Cook - 3-4pm", 3],
      ["Fri - Dinner Cook - 3-4pm", 3],
      ["Mon - Dinner Cook - 4-5pm", 3],
      ["Tues - Dinner Cook - 4-5pm", 3],
      ["Wed - Dinner Cook - 4-5pm", 3],
      ["Thurs - Dinner Cook - 4-5pm", 3],
      ["Fri - Dinner Cook - 4-5pm", 3],
      ["Mon - Dinner Cook - 5-6pm", 3],
      ["Tues - Dinner Cook - 5-6pm", 3],
      ["Wed - Dinner Cook - 5-6pm", 3],
      ["Thurs - Dinner Cook - 5-6pm", 3],
      ["Fri - Dinner Cook - 5-6pm", 3],
      ["Mon - Dinner Clean - 7-8pm", 3],
      ["Tues - Dinner Clean - 7-8pm", 3],
      ["Wed - Dinner Clean - 7-8pm", 3],
      ["Thurs - Dinner Clean - 7-8pm", 3],
      ["Fri - Dinner Clean - 7-8pm", 3],
      ["Mon - Dinner Clean - 8-9pm", 3], 
      ["Tues - Dinner Clean - 8-9pm", 3],
      ["Wed - Dinner Clean - 8-9pm", 3],
      ["Thurs - Dinner Clean - 8-9pm", 3],
      ["Fri - Dinner Clean - 8-9pm", 3],
      ["Mon - Snack Cook - 9-10pm", 2],
      ["Tues - Snack Cook - 9-10pm", 2],
      ["Wed - Snack Cook - 9-10pm", 2],
      ["Thurs - Snack Cook - 9-10pm", 2],
      ["Mon - Snack Clean - 10-11pm", 3],
      ["Tues - Snack Clean - 10-11pm", 3],
      ["Wed - Snack Clean - 10-11pm", 3], 
      ["Thurs - Snack Clean - 10-11pm", 3]]

# A dictionary from the answers of the survey to its given labor
LABOR_MAP = {u'9275058246': {   u'9275058263': 0, # Sun 6-7am
                        u'9275058264': 0,  # Mon 6-7am 
                        u'9275058265': 0,  # Tues 6-7am
                        u'9275058266': 0,  # Wed 6-7am
                        u'9275058268': 0,  # Thurs 6-7am
                        u'9275058269': 0,  # Fri 6-7am
                        u'9275058270': 0}, # Sat 6-7am

     u'9275058247': {   u'9275058263': 0,  # Sun 7-8am
                        u'9275058264': 0,  # Mon 7-8am 
                        u'9275058265': 0,  # Tues 7-8am
                        u'9275058266': 0,  # Wed 7-8am
                        u'9275058268': 0,  # Thurs 7-8am
                        u'9275058269': 0,  # Fri 7-8am
                        u'9275058270': 0}, # Sat 7-8am

     u'9275058248': {   u'9275058263': 0,  # Sun 8-9am
                        u'9275058264': "Mon - Morning Hobbit - 8-9am",    
                        u'9275058265': "Tues - Morning Hobbit - 8-9am", 
                        u'9275058266': "Wed - Morning Hobbit - 8-9am",  
                        u'9275058268': "Thurs - Morning Hobbit - 8-9am",
                        u'9275058269': "Fri - Morning Hobbit - 8-9am",  
                        u'9275058270': 0}, # Sat 8-9am                             

     u'9275058249': {   u'9275058263': "Sun - Morning Hobbit - 9-10am", 
                        u'9275058264': "Mon - Lunch Cook - 9-10am",       
                        u'9275058265': "Tues - Lunch Cook - 9-10am",    
                        u'9275058266': "Wed - Lunch Cook - 9-10am",     
                        u'9275058268': "Thurs - Lunch Cook - 9-10am",   
                        u'9275058269': "Fri - Lunch Cook - 9-10am",     
                        u'9275058270': "Sat - Morning Hobbit - 9-10am"},

     u'9275058250': {   u'9275058263': "Sun - Brunch Cook - 10-11am",  
                        u'9275058264': "Mon - Lunch Cook - 10-11am",      
                        u'9275058265': "Tues - Lunch Cook - 10-11am",   
                        u'9275058266': "Wed - Lunch Cook - 10-11am",    
                        u'9275058268': "Thurs - Lunch Cook - 10-11am",  
                        u'9275058269': "Fri - Lunch Cook - 10-11am",    
                        u'9275058270': "Sat - Brunch Cook - 10-11am"},  

     u'9275058251': {   u'9275058263': "Sun - Brunch Cook - 11am-12pm", 
                        u'9275058264': 0, # Mon 11am-12pm                                
                        u'9275058265': 0, # Tus 11am-12pm                           
                        u'9275058266': 0, # Wed 11am-12pm                              
                        u'9275058268': 0, # Thurs 11am-12pm                              
                        u'9275058269': 0, # Fri 11am-12pm                              
                        u'9275058270': "Sat - Brunch Cook - 11am-12pm"},

     u'9275058252': {   u'9275058263': 0, # Sun 12-1pm
                        u'9275058264': "Mon - Lunch Clean - 12-1pm",      
                        u'9275058265': "Tues - Lunch Clean - 12-1pm",   
                        u'9275058266': "Wed - Lunch Clean - 12-1pm",    
                        u'9275058268': "Thurs - Lunch Clean - 12-1pm",  
                        u'9275058269': "Fri - Lunch Clean - 12-1pm",    
                        u'9275058270': 0}, # Sat 12-1pm                             

     u'9275058253': {   u'9275058263': "Sun - Brunch Clean - 1-2pm",    
                        u'9275058264': "Mon - Lunch Clean - 1-2pm",       
                        u'9275058265': "Tues - Lunch Clean - 1-2pm",    
                        u'9275058266': "Wed - Lunch Clean - 1-2pm",     
                        u'9275058268': "Thurs - Lunch Clean - 1-2pm",   
                        u'9275058269': "Fri - Lunch Clean - 1-2pm",     
                        u'9275058270': "Sat - Brunch Clean - 1-2pm"},   

     u'9275058254': {   u'9275058263': "Sun - Brunch Clean - 2-3pm",    
                        u'9275058264': "Mon - Dinner Cook - 2-3pm",    
                        u'9275058265': "Tues - Dinner Cook - 2-3pm",    
                        u'9275058266': "Wed - Dinner Cook - 2-3pm",     
                        u'9275058268': "Thurs - Dinner Cook - 2-3pm",  
                        u'9275058269': "Fri - Dinner Cook - 2-3pm",     
                        u'9275058270': "Sat - Brunch Clean - 2-3pm"},   

     u'9275058255': {   u'9275058263': 0, # Sun 3-4pm
                        u'9275058264': "Mon - Dinner Cook - 3-4pm",      
                        u'9275058265': "Tues - Dinner Cook - 3-4pm",    
                        u'9275058266': "Wed - Dinner Cook - 3-4pm",     
                        u'9275058268': "Thurs - Dinner Cook - 3-4pm",   
                        u'9275058269': "Fri - Dinner Cook - 3-4pm",    
                        u'9275058270': 0}, # Sat 3-4pm

     u'9275058256': {   u'9275058263': 0,  # Sun 4-5pm
                        u'9275058264': "Mon - Dinner Cook - 4-5pm",      
                        u'9275058265': "Tues - Dinner Cook - 4-5pm",    
                        u'9275058266': "Wed - Dinner Cook - 4-5pm",     
                        u'9275058268': "Thurs - Dinner Cook - 4-5pm",   
                        u'9275058269': "Fri - Dinner Cook - 4-5pm",     
                        u'9275058270': 0}, # Sat 4-5pm

     u'9275058257': {   u'9275058263': 0,  # Sun 5-6pm
                        u'9275058264': "Mon - Dinner Cook - 5-6pm",       
                        u'9275058265': "Tues - Dinner Cook - 5-6pm",    
                        u'9275058266': "Wed - Dinner Cook - 5-6pm",     
                        u'9275058268': "Thurs - Dinner Cook - 5-6pm",   
                        u'9275058269': "Fri - Dinner Cook - 5-6pm",     
                        u'9275058270': 0}, # Sat 5-6pm

     u'9275058258': {   u'9275058263': 0,  # Sun 6-7pm
                        u'9275058264': 0,  # Mon 6-7pm 
                        u'9275058265': 0,  # Tues 6-7pm
                        u'9275058266': 0,  # Wed 6-7pm
                        u'9275058268': 0,  # Thurs 6-7pm
                        u'9275058269': 0,  # Fri 6-7pm
                        u'9275058270': 0}, # Sat 6-7pm

     u'9275058259': {   u'9275058263': 0,  # Sun 7-8 pm
                        u'9275058264': "Mon - Dinner Clean - 7-8pm",    
                        u'9275058265': "Tues - Dinner Clean - 7-8pm",   
                        u'9275058266': "Wed - Dinner Clean - 7-8pm",    
                        u'9275058268': "Thurs - Dinner Clean - 7-8pm",  
                        u'9275058269': "Fri - Dinner Clean - 7-8pm",    
                        u'9275058270': 0}, # Sat 7-8pm

     u'9275058260': {   u'9275058263': 0,  # Sun 8-9pm
                        u'9275058264': "Mon - Dinner Clean - 8-9pm",     
                        u'9275058265': "Tues - Dinner Clean - 8-9pm",   
                        u'9275058266': "Wed - Dinner Clean - 8-9pm",    
                        u'9275058268': "Thurs - Dinner Clean - 8-9pm",  
                        u'9275058269': "Fri - Dinner Clean - 8-9pm",    
                        u'9275058270': 0}, # Sat 8-9pm

     u'9275058261': {   u'9275058263': 0,  # Sun 9-10pm
                        u'9275058264': "Mon - Snack Cook - 9-10pm",      
                        u'9275058265': "Tues - Snack Cook - 9-10pm",    
                        u'9275058266': "Wed - Snack Cook - 9-10pm",    
                        u'9275058268': "Thurs - Snack Cook - 9-10pm",   
                        u'9275058269': 0,  # Fri 9-10pm
                        u'9275058270': 0}, # Sat 9-10pm
                        
     u'9275058262': {   u'9275058263': 0,  # Sun 10-11pm
                        u'9275058264': "Mon - Snack Clean - 10-11pm",    
                        u'9275058265': "Tues - Snack Clean - 10-11pm",  
                        u'9275058266': "Wed - Snack Clean - 10-11pm",   
                        u'9275058268': "Thurs - Snack Clean - 10-11pm", 
                        u'9275058269': 0,  # Fri 10-11pm
                        u'9275058270': 0}} # Sat 10-11pm
