'''
You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.
''' 

def check_unique(nums):
    return len(nums) == len(set(nums))

lst = [1,2,3,4,5,6]

print(check_unique(lst)) 

