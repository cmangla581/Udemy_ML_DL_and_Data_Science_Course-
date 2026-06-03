'''
Thread Pool Executor is used to efficiently manage and reuse a pool of worker threads to execute the  
asynchronous tasks. It reduces the performance of the creating new threads for every task. 
''' 

from concurrent.futures import ThreadPoolExecutor 
import time 

def print_number(number): 
    time.sleep(1) 
    return f"Number: {number}" 

numbers = [1,2,3,4,5] 

with ThreadPoolExecutor(max_workers = 3) as executor: 
    results = executor.map(print_number, numbers)  

for result in results: 
    print(result) 
