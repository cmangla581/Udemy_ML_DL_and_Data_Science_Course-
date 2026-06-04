
'''
Real World Example: Multiprocessing for the CPU bound tasks 
Scenario: Factorial Calculation 
Factorial Calculations for the large numbers involve the significant computational work. 

ultiprocessing include the distribution of the workload across the multiple CPU cores. 
''' 

import multiprocessing 
import time 
import math 


# Computing the factorial of a number 
def compute_factorial(number): 
    print(f"Computing the factorial of a {number}") 
    result = math.factorial(number) 
    print(f"Factorial of a {number} is {result}") 
    return result 

if __name__=="__main__": 
    numbers = [5000, 6000, 700, 8000] 

    start_time = time.time()  

    # create a poll of the workers process 
    with multiprocessing.Pool() as pool: 
        results = pool.map(compute_factorial, numbers) 

    end_time = time.time() 

    print(f"Results: {results}") 
    print(f"Time taken: {end_time - start_time} seconds") 



