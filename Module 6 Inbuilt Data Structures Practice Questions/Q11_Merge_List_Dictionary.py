'''
Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act 
as keys and elements from the second list act as values.
''' 

def merge_lists_to_dictionary(keys, values):
    result = {}
    length = min(len(keys), len(values))
    
    for i in range(length):
        result[keys[i]] = values[i]
        
    return result

keys = ['a', 'b', 'c'] 
values = [1, 2, 3] 

print(merge_lists_to_dictionary(keys, values))