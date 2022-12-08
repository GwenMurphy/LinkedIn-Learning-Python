"""
He's going on about scheduling functions to do the thing at certain times.

Challenge:          Write a Python function to schedule another given function to execute at a specified time.

Input:              Event time
                    Function
                    Any number of arguments

schedule_function(time.time()+1, print, 'Welcome to Zombocom.')

"""


##### ##### ##### ##### ##### Instructor's Solution

## Import modules
import sched
import time


## A thing that does a thing
## ## ## "function" is the function to execute
## ## ## "*args" means a variable number of arguments
def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep) # scheduler object
    s.enterabs(event_time, 1, function, argument=args) ## "enterabs" function allows for scheduling of an event to execute at an absolute time
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()