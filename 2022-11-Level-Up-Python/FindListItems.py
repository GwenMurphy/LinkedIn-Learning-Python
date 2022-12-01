"""
Challenge:          Find all list items.

Input:              List to search, value to search for
Output:             List of indices
"""

##### ##### ##### ##### ##### My Attempt

# It's just gonna get harder. I'll settle for noting down the solution and adding commenting.


##### ##### ##### ##### ##### Instructor's Solution


## The function itself.
def index_all(search_list, item):
    ## The list if items to be indexed, I presume.
    index_list = []

    ## Iterates through the list.
    for index, value in enumerate(search_list):
        ## If the value matches an item in the list.
        if value == item:
            ## Append it to the above list.
            index_list.append([index])
        elif isinstance(search_list[index], item):
            index_list.append([index] + 1)
    return index_list