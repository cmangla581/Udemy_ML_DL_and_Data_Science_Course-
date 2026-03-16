'''
Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, meaning it reads the same forwards and backwards.
'''

def is_palindrome_tuple(tup): 
    left = 0 
    right = len(tup) - 1 

    while left < right: 
        if tup[left != tup[right]]: 
            return False 
        left += 1 
        right -=1 

    return True  

tup = (1, 2, 3, 2, 1) 

print(is_palindrome_tuple(tup)) 