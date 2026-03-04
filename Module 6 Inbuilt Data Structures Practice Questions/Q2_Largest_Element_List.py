'''
Write a Python function that finds and returns the largest element in a given list of integers.
''' 

def find_largest(numbers): 
    largest = numbers[0] 

    for num in numbers: 
        if num > largest:  
            largest = num 

    return largest 

nums = [10,45,2,99,23] 

print(find_largest(nums))  




 