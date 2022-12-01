"""
Challenge:          Create a waiting game.

"""


##### ##### ##### ##### ##### My Attempt

#import random, time
#
#
#
#def waiting_game():
#    timeElapsed = 0
#    targetTime = random.randint(2000,4000)/1000
#
#    timeMsgS = f"""
#    Elapsed time: {timeElapsed} seconds
#    ({timeElapsed - targetTime} seconds too slow)
#    """
#    timeMsgF = f"""
#    Elapsed time: {timeElapsed} seconds
#    ({targetTime - timeElapsed} seconds too fast)
#    """
#    timeMsgE = f"""
#    Elapsed time: {timeElapsed} seconds
#    """
#
#    if timeElapsed > targetTime:
#        return timeMsgS
#    elif timeElapsed < targetTime:
#        return timeMsgF
#    else:
#        return timeMsgE
#



##### ##### ##### ##### ##### Instructor's Solution

import time
import random

def waiting_game():
    target = random.randint(2,4) ## Target seconds to wait.
    print(f'\nYour target time is {target} seconds')

    input(' --- Press Enter to Begin --- ')
    start = time.perf_counter()

    input(f'\n... Press Enter again after {target} seconds...')
    elapsed = time.perf_counter() - start

    print(f'\nElapsed time:  {elapsed :.3f} seconds')
    if elapsed == target:
        print('Unbelievable! Perfect timing!')
    elif elapsed < target:
        print(f'{target - elapsed :.3f} seconds too fast')
    else:
        print(f'{elapsed - target :.3f} seconds too slow')

waiting_game()