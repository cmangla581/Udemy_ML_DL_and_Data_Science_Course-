'''
You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. 
The difference is defined as the absolute value of the difference between two consecutive elements. 
''' 

def max_consecutive_difference(nums): 
    if len(nums) < 2: 
        return 0 
    
    max_diff = 0 

    for i in range(len(nums) - 1): 
        diff = abs(nums[i] - nums[i+1]) 

        if diff > max_diff: 
            max_diff = diff 

    return max_diff 

lst  =[1,7,10,3,5] 

print(max_consecutive_difference(lst))