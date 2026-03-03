'''
Write a Python function that calculates the sum of all elements in a given list of integers.
''' 

def sum_list(numbers): 
    total = 0 
    for num in numbers: 
        total += num
    return total 

nums = [1,2,3,4,5] 
print(sum_list(nums))  

