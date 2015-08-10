#!/usr/bin/python

labors_list = [["Mon - Morning Hobbit - 8-9am", 1], 
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

labor_map = {u'9275058246': {   u'9275058263': 0,                           # Sun     6 - 7 am
                        u'9275058264': 0,                               # Mon  
                        u'9275058265': 0,                               # Tues
                        u'9275058266': 0,                               # Wed
                        u'9275058268': 0,                               # Thurs
                        u'9275058269': 0,                               # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058247': {   u'9275058263': 0,                               # Sun     7 - 8 am
                        u'9275058264': 0,                               # Mon  
                        u'9275058265': 0,                               # Tues
                        u'9275058266': 0,                               # Wed
                        u'9275058268': 0,                               # Thurs
                        u'9275058269': 0,                               # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058248': {   u'9275058263': 0,                               # Sun     8 - 9 am
                        u'9275058264': "Mon - Morning Hobbit - 8-9am",  # Mon  
                        u'9275058265': "Tues - Morning Hobbit - 8-9am", # Tues
                        u'9275058266': "Wed - Morning Hobbit - 8-9am",  # Wed
                        u'9275058268': "Thurs - Morning Hobbit - 8-9am",# Thurs
                        u'9275058269': "Fri - Morning Hobbit - 8-9am",  # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058249': {   u'9275058263': "Sun - Morning Hobbit - 9-10am", # Sun     9 - 10 am
                        u'9275058264': "Mon - Lunch Cook - 9-10am",     # Mon  
                        u'9275058265': "Tues - Lunch Cook - 9-10am",    # Tues
                        u'9275058266': "Wed - Lunch Cook - 9-10am",     # Wed
                        u'9275058268': "Thurs - Lunch Cook - 9-10am",   # Thurs
                        u'9275058269': "Fri - Lunch Cook - 9-10am",     # Fri
                        u'9275058270': "Sat - Morning Hobbit - 9-10am"},# Sat

     u'9275058250': {   u'9275058263': "Sun - Brunch Cook - 10-11am",   # Sun     10 - 11 am
                        u'9275058264': "Mon - Lunch Cook - 10-11am",    # Mon  
                        u'9275058265': "Tues - Lunch Cook - 10-11am",   # Tues
                        u'9275058266': "Wed - Lunch Cook - 10-11am",    # Wed
                        u'9275058268': "Thurs - Lunch Cook - 10-11am",  # Thurs
                        u'9275058269': "Fri - Lunch Cook - 10-11am",    # Fri
                        u'9275058270': "Sat - Brunch Cook - 10-11am"},  # Sat

     u'9275058251': {   u'9275058263': "Sun - Brunch Cook - 11am-12pm", # Sun     11 am - 12 pm
                        u'9275058264': 0,                               # Mon  
                        u'9275058265': 0,                               # Tues
                        u'9275058266': 0,                               # Wed
                        u'9275058268': 0,                               # Thurs
                        u'9275058269': 0,                               # Fri
                        u'9275058270': "Sat - Brunch Cook - 11am-12pm"},# Sat

     u'9275058252': {   u'9275058263': 0,                               # Sun     12 - 1 pm
                        u'9275058264': "Mon - Lunch Clean - 12-1pm",    # Mon  
                        u'9275058265': "Tues - Lunch Clean - 12-1pm",   # Tues
                        u'9275058266': "Wed - Lunch Clean - 12-1pm",    # Wed
                        u'9275058268': "Thurs - Lunch Clean - 12-1pm",  # Thurs
                        u'9275058269': "Fri - Lunch Clean - 12-1pm",    # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058253': {   u'9275058263': "Sun - Brunch Clean - 1-2pm",    # Sun     1 - 2 pm
                        u'9275058264': "Mon - Lunch Clean - 1-2pm",     # Mon  
                        u'9275058265': "Tues - Lunch Clean - 1-2pm",    # Tues
                        u'9275058266': "Wed - Lunch Clean - 1-2pm",     # Wed
                        u'9275058268': "Thurs - Lunch Clean - 1-2pm",   # Thurs
                        u'9275058269': "Fri - Lunch Clean - 1-2pm",     # Fri
                        u'9275058270': "Sat - Brunch Clean - 1-2pm"},   # Sat

     u'9275058254': {   u'9275058263': "Sun - Brunch Clean - 2-3pm",    # Sun     2 - 3 pm
                        u'9275058264': "Mon - Dinner Cook - 2-3pm",     # Mon  
                        u'9275058265': "Tues - Dinner Cook - 2-3pm",    # Tues
                        u'9275058266': "Wed - Dinner Cook - 2-3pm",     # Wed
                        u'9275058268': "Thurs - Dinner Cook - 2-3pm",   # Thurs
                        u'9275058269': "Fri - Dinner Cook - 2-3pm",     # Fri
                        u'9275058270': "Sat - Brunch Clean - 2-3pm"},   # Sat

     u'9275058255': {   u'9275058263': 0,                               # Sun     3 - 4 pm
                        u'9275058264': "Mon - Dinner Cook - 3-4pm",     # Mon  
                        u'9275058265': "Tues - Dinner Cook - 3-4pm",    # Tues
                        u'9275058266': "Wed - Dinner Cook - 3-4pm",     # Wed
                        u'9275058268': "Thurs - Dinner Cook - 3-4pm",   # Thurs
                        u'9275058269': "Fri - Dinner Cook - 3-4pm",     # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058256': {   u'9275058263': 0,                               # Sun     4 - 5 pm
                        u'9275058264': "Mon - Dinner Cook - 4-5pm",     # Mon  
                        u'9275058265': "Tues - Dinner Cook - 4-5pm",    # Tues
                        u'9275058266': "Wed - Dinner Cook - 4-5pm",     # Wed
                        u'9275058268': "Thurs - Dinner Cook - 4-5pm",   # Thurs
                        u'9275058269': "Fri - Dinner Cook - 4-5pm",     # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058257': {   u'9275058263': 0,                               # Sun     5 - 6 pm
                        u'9275058264': "Mon - Dinner Cook - 5-6pm",     # Mon  
                        u'9275058265': "Tues - Dinner Cook - 5-6pm",    # Tues
                        u'9275058266': "Wed - Dinner Cook - 5-6pm",     # Wed
                        u'9275058268': "Thurs - Dinner Cook - 5-6pm",   # Thurs
                        u'9275058269': "Fri - Dinner Cook - 5-6pm",     # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058258': {   u'9275058263': 0,                               # Sun     6 - 7 pm
                        u'9275058264': 0,                               # Mon  
                        u'9275058265': 0,                               # Tues
                        u'9275058266': 0,                               # Wed
                        u'9275058268': 0,                               # Thurs
                        u'9275058269': 0,                               # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058259': {   u'9275058263': 0,                               # Sun     7 - 8 pm
                        u'9275058264': "Mon - Dinner Clean - 7-8pm",    # Mon  
                        u'9275058265': "Tues - Dinner Clean - 7-8pm",   # Tues
                        u'9275058266': "Wed - Dinner Clean - 7-8pm",    # Wed
                        u'9275058268': "Thurs - Dinner Clean - 7-8pm",  # Thurs
                        u'9275058269': "Fri - Dinner Clean - 7-8pm",    # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058260': {   u'9275058263': 0,                               # Sun     8 - 9 pm
                        u'9275058264': "Mon - Dinner Clean - 8-9pm",    # Mon  
                        u'9275058265': "Tues - Dinner Clean - 8-9pm",   # Tues
                        u'9275058266': "Wed - Dinner Clean - 8-9pm",    # Wed
                        u'9275058268': "Thurs - Dinner Clean - 8-9pm",  # Thurs
                        u'9275058269': "Fri - Dinner Clean - 8-9pm",    # Fri
                        u'9275058270': 0},                              # Sat

     u'9275058261': {   u'9275058263': 0,                               # Sun     9 - 10 pm
                        u'9275058264': "Mon - Snack Cook - 9-10pm",     # Mon  
                        u'9275058265': "Tues - Snack Cook - 9-10pm",    # Tues
                        u'9275058266': "Wed - Snack Cook - 9-10pm",     # Wed
                        u'9275058268': "Thurs - Snack Cook - 9-10pm",   # Thurs
                        u'9275058269': 0,                               # Fri
                        u'9275058270': 0},                              # Sat
                        
     u'9275058262': {   u'9275058263': 0,                               # Sun     10 - 11 pm
                        u'9275058264': "Mon - Snack Clean - 10-11pm",   # Mon  
                        u'9275058265': "Tues - Snack Clean - 10-11pm",  # Tues
                        u'9275058266': "Wed - Snack Clean - 10-11pm",   # Wed
                        u'9275058268': "Thurs - Snack Clean - 10-11pm", # Thurs
                        u'9275058269': 0,                               # Fri
                        u'9275058270': 0}}                              # Sat
