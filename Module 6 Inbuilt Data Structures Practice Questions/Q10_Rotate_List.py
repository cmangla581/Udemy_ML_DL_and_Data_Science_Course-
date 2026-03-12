'''
You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. 
A rotation shifts elements from the end of the list to the front. 
''' 

def rotate_list(lst, k): 
    n = len(lst) 
    if n == 0: 
        return lst 
    
    k = k % n 

    for _ in range(k): 
        last = lst[-1] 
        i = n-1 

        while i > 0: 
            lst[i] = lst[i-1] 
            i-=1 
        lst[0] = last 


    return last 

lst  =[1,2,3,4,5] 
k = 2 

print(rotate_list(lst, k)) 