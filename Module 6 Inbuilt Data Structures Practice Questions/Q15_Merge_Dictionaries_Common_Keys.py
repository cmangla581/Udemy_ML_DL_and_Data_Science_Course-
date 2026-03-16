'''
Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. 
If a key appears in more than one dictionary, sum up their values.
''' 

def merge_dicts_with_overlapping_keys(dicts):
    result = {}

    for d in dicts:
        for key in d:
            if key in result:
                result[key] += d[key]
            else:
                result[key] = d[key]

    return result


dicts = {'a': 1, 'b': 2},{'b': 3, 'c': 4},{'a': 5} 

print(merge_dicts_with_overlapping_keys(dicts))  
