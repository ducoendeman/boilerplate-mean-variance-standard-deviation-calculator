import numpy as np


def calculate(list):
    # Raise ValueError if argument list does not contain nine entries
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a numpy array and reshape it
    array_3x3 = np.array(list).reshape(3, 3)
    # Create empy dictionary to hold the results
    calculations = {}
    
    key_function_list = [('mean', np.mean),
                         ('variance', np.var),
                         ('standard deviation', np.std),
                         ('max', np.max),
                         ('min', np.min),
                         ('sum', np.sum)]
    
    for key, function in key_function_list:
        calculations[key] = [function(array_3x3, axis=0).tolist(),
                             function(array_3x3, axis=1).tolist(),
                             function(array_3x3.flatten()).tolist()]
    
    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))