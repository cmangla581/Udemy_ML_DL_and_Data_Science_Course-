'''
Real World Example: Multithreading for Input Output Tasks 
Scenario: Web Scrapping 

Web Scrapping often involves the making the numerous network requests to fetch web pages. These tassks are the input output 
time waiting for the resonses from servers. Multi threading can significantly improve the performance by 
allowing the multiple web pages. 

''' 
'''
https://langchain-doc.readthedocs.io/en/latest/index.html  

https://docs.langchain.com/oss/python/langchain/overview 

https://python.langchain.com/api_reference#main-content

''' 

import threading 
import requests 
from bs4 import BeautifulSoup 

urls = [ 

'https://langchain-doc.readthedocs.io/en/latest/index.html',  

'https://docs.langchain.com/oss/python/langchain/overview', 

'https://python.langchain.com/api_reference#main-content'

] 

# Creating a function to fetch the content as: 

def fetch_content(url): 
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, 'html.parser') 
    print(f"Fetched {len(soup.text)} charcters from {url}") 

threads =[] 

for url in urls: 
    thread = threading.Thread(target = fetch_content, args = (url,)) 
    threads.append(thread)  
    thread.start() 

for thread in threads: 
    thread.join() 

print("All web pages scrapped") 