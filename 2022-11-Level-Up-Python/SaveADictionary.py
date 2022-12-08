"""
Challenge:          Write a Python function to save a dictionary to a file.

Input:              File path to saved directory.

Output:             Retrieved dictionary object.

"""




##### ##### ##### ##### ##### My Attempt

# a thing that does a thing





##### ##### ##### ##### ##### Instructor's Solution


import pickle   # The fuck is this? Sounds like a euphemism.

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)     ## Who the hell names this thing?

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
