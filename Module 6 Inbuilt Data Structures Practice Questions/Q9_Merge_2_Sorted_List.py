'''
You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. 
The resulting list should also be in non-decreasing order. 
''' 

def merge_two_sorted_lists(list1, list2): 
    merged = [] 
    i = 0 
    j = 0 

    while i < len(list1) and j < len(list2): 
        if list1[i] <= list2[j]: 
            merged.append(list1[i]) 
            i += 1 
        else: 
            merged.append(list2[j]) 
            j += 1 

    while i < len(list1): 
        merged.append(list1[i]) 
        i += 1 

    while j < len(list2): 
        merged.append(list2[j]) 
        j += 1 

    return merged  

list1 = [1,2,3] 
list2 = [3,4,5,2] 

print(merge_two_sorted_lists(list1, list2)) 