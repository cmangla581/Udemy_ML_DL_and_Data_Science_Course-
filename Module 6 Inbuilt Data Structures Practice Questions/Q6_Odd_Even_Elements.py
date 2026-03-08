'''
You are given a list of integers. 
Write a Python program that counts and returns the number of even and odd numbers in the list.
''' 

def count_even_odd(nums): 
    even_count = 0
    odd_count = 0 

    for num in nums: 
        if num%2 == 0: 
            even_count += 1 

        else: 
            odd_count += 1 

    return even_count,odd_count 

lst = [1,2,3,4,5,6,7,8] 

print(count_even_odd(lst)) 
