'''
You are given two lists of integers. Write a Python program that checks whether the first list is a subset of the second list using a brute-force approach, without using the in keyword. 
A list is considered a subset if all elements of the first list are present in the second list. 
''' 

def is_subset(list1, list2): 
    for i in range(len(list1)): 
        found = False 
        for j in range(len(list2)):
            if list1[i] == list2[j]: 
                found = True 
                break 
        if not found: 
            return False 
        
    return True 

print(is_subset([1,2], [1,2,3,4]))  


