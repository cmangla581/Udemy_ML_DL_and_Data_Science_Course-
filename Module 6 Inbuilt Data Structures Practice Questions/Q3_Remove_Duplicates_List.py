'''
You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. 
The order of elements in the list should be maintained.
''' 

def remove_duplicates(numbers): 
    seen = set() 
    unique_list = [] 

    for num in numbers: 
        if num not in seen: 
            unique_list.append(num) 
            seen.add(num) 
    return unique_list 

nums = [1,2,3,2,3,4,6,7,8,2,1] 
print(remove_duplicates(nums))   


