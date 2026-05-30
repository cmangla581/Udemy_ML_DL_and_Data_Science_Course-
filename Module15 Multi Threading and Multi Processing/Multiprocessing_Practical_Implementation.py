
# Multiprocessing Practical Implementation 
'''
Processes that run in parallel are mainly called as the multiprocessing. It is used in various tasks like the:

1. CPU Bound Tasks: Taks that are heavy on the computer usage liek themathematical operations and data preprocessing. 
2. Parallel Execution: multiple cores of the CPU. 
''' 

import multiprocessing 
import time 

def square_numbers(): 
    for i in range(5): 
        time.sleep(1) 
        print(f"Square: {i*i}") 

def cube_numbers(): 
    for i in range(5): 
        time.sleep(1.5) 
        print(f"Cube: {i*i*i}") 

if __name__=="__main__": 

    p1 = multiprocessing.Process(target = square_numbers) 
    p2 = multiprocessing.Process(target = cube_numbers)
    t = time.time() 

    p1.start() 
    p2.start() 

    p1.join() 
    p2.join() 

    finished_time = time.time() - t 
    print(finished_time)