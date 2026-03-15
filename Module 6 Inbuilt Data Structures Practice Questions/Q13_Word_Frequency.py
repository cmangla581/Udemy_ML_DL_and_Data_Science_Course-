'''
Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.
''' 

def count_word_frequency(sentence): 
    words = sentence.split() 
    frequency = {} 

    for word in words: 
        if word in frequency: 
            frequency[word] += 1 

        else: 
            frequency[word] = 1 

    return frequency  

sentence = "hello world hello" 

print(count_word_frequency(sentence)) 