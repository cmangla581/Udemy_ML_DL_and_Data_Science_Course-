'''
Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.
'''

def merge_three_dictionaries(dict1, dict2, dict3): 
    result = {} 
    
    for key in dict1: 
        result[key] = dict1[key] 
        
    for key in dict2: 
        result[key] = dict2[key] 
        
    for key in dict3: 
        result[key] = dict3[key] 
        
    return result 

dict1 = {'a': 1, 'b': 2} 
dict2 = {'c': 3, 'd': 4} 
dict3 = {'e': 5, 'f': 6} 

print(merge_three_dictionaries(dict1, dict2 , dict3)) 