#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:12:34 2019

@author: marco
"""
import random 
import matplotlib.pyplot as plt
import time
import numpy as np

def counting_sort_integers(input_int_list, max_int):
    
    counter = [0] * (max_int + 1) 
    
    # Counting the occurrences of a number in the input list
    for n in input_int_list:
        counter[n] += 1
        
    sorted_list = [0] * len(input_int_list) # Default value for sorted list is not in range [0-9] (debug purposes)
    current_index = 0 # We have to keep track of the next available index in the sorted list
    
    for i in range(len(counter)): # We have to use values in range [0-len(counter)]-> [0-9].
        count = counter[i] # How many occurrences have there been in the input list?
        if count > 0: # If there is something to put in the sorted list
            sorted_list[current_index:(current_index+count)] = [i] * count # Then put them (count) at a times
            current_index += count
            
    return sorted_list


def counting_sort_list_letters(input_str):
    ''' The counting sort here is implemented using the feature that python dictionaries
        provide: ordering of the keys while preserving access in constant time.
    '''
    
    # Initializing the dict that will act as counter, access will be in constant time.
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    counter_letters = dict.fromkeys(list(letters), 0)
    
    # Counting the occurrences of the letters in the input string (k)
    for l in list(input_str):
        counter_letters[l] += 1
        
    # Initializing the value of the sorted array to a default char not in alphabet (debug purposes, could be any char value)
    sorted_array = ['?'] * len(input_str)
    
    # This is here to keep track of how many chars have been inserted in the string, so we can access using 
    # this variable as an index.
    current_index = 0 
    for k in counter_letters.keys(): # Keys list keeps the order, now traversing it from left to right (from the least important value to the most important)
        
        count = counter_letters[k] # First get how many occurrences of a letter have been found
        
        if count > 0: # If > 0 then the letter (key) will end up in the sorted array (count) times
            sorted_array[current_index:(current_index+count)] = [k] * count # Put multiple separated values at multiple separated indexes (1 index -> 1 value)
            counter_letters[k] -= count # Just keeping track of the inserted values
            current_index += count # The position has to move of (count) moves to the right
            
    return sorted_array


''' This becomes useful ONLY IF the strings to compare are of the same length. '''
def map_char_to_int(letter):
    letters_dict = dict()
    letters_dict['a'] = 1
    letters_dict['b'] = 2
    letters_dict['c'] = 3
    letters_dict['d'] = 4
    letters_dict['e'] = 5
    letters_dict['f'] = 6
    letters_dict['g'] = 7
    letters_dict['h'] = 8
    letters_dict['i'] = 9
    letters_dict['j'] = 10
    letters_dict['k'] = 11
    letters_dict['l'] = 12
    letters_dict['m'] = 13
    letters_dict['n'] = 14
    letters_dict['o'] = 15
    letters_dict['p'] = 16
    letters_dict['q'] = 17
    letters_dict['r'] = 18
    letters_dict['s'] = 19
    letters_dict['t'] = 20
    letters_dict['u'] = 21
    letters_dict['v'] = 22
    letters_dict['w'] = 23
    letters_dict['x'] = 24
    letters_dict['y'] = 25
    letters_dict['z'] = 26
    
    '''
    letters_dict['a'] = 27
    letters_dict['b'] = 28
    letters_dict['c'] = 29
    letters_dict['d'] = 30
    letters_dict['e'] = 31
    letters_dict['f'] = 32
    letters_dict['g'] = 33
    letters_dict['h'] = 34
    letters_dict['i'] = 35
    letters_dict['j'] = 36
    letters_dict['k'] = 37
    letters_dict['l'] = 38
    letters_dict['m'] = 39
    letters_dict['n'] = 40
    letters_dict['o'] = 41
    letters_dict['p'] = 42
    letters_dict['q'] = 43
    letters_dict['r'] = 44
    letters_dict['s'] = 45
    letters_dict['t'] = 46
    letters_dict['u'] = 47
    letters_dict['v'] = 48
    letters_dict['w'] = 49
    letters_dict['x'] = 50
    letters_dict['y'] = 51
    letters_dict['z'] = 52
    '''
    return letters_dict[letter]

''' This implementation works, but it's absolutely inefficient resources-wise.
    The keys (integers) used in the counting sort for strings become very large, very quickly.
    
def map_string_to_int(string): # Mapping to int allows for an ordering of strings.
    res = 0
    for i in range(len(string)):
       index = len(string) - i - 1 # We start mapping from the most significant char (so from the right)
       res += map_char_to_int(string[index]) * (52 ** i)
      
    return res

def count_sort_list_of_strings_inefficient(strings, length_m, string_len_n):
    len_list = [dict() for i in range(string_len_n + 1)]
    res = []

    for s in strings:
            len_list[len(s)][map_string_to_int(s)] = s
    
    # Since we are using the dictionaries, where the key is the mapping from string to int, we sort the keys.
    for d in len_list:    
        if d != {}:
            k = d.keys()
            ordered_k = counting_sort_integers(k)
            
            for ok in ordered_k:
                res.append(d[ok])
    
    return res
'''

def map_to_int(string, max_len):
    
    res = 0
    
    for i in range(len(string)):
        exp = max_len - i
        
        res += map_char_to_int(string[i]) * (10 ** exp)
    
    return res
  
def count_sort_list_of_strings(strings, length_m, string_len_n):
    
    d = dict()
    
    for i in range(length_m):
        
        s = strings[i]
        mapping = map_to_int(s, length_m)
        d[mapping] = s
    
    max_int = max(d.keys())
    k_sorted = counting_sort_integers(d.keys(), max_int)    
    
    res = []
    for k in k_sorted:
        res.append(d[k])
    return res




if __name__ == '__main__':
    ''' Empirical results from counting sort for single words'''
    
    strings = []
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    '''
    # Generate random strings of length from 1 to (iterations)
    iterations = 5000
    for i in range(1, iterations+1):
        curr_str = ''
        for j in range(0, i):
            letter = letters[random.randint(0, len(letters)-1)]
            curr_str += letter
        
        strings.append(curr_str)
        
    performance = []
    for i in range(len(strings)):
        s = strings[i]
        start = time.time()
        counting_sort_list_letters(s)
        end = time.time()
        elapsed_time = end - start
        performance.append([elapsed_time, s])

    #performance.sort(key=lambda x : x[0], reverse=True)

    plt.figure(figsize=(10, 7))      
    plt.xlabel('String length')
    plt.ylabel('Time elapsed (s)')
    
    times = [x[0] for x in performance]
    plt.plot(times)
    plt.show()
    '''
    ''' Empirical results from counting sort applied to list of strings '''
    s = ['a', 'ab', 'ba', 'aba','aaa','abc','baa','abc','aabc','aaaa','abbb','babbb','ccc','ddddd']
    m = len(s)
    n = 5
    r = count_sort_list_of_strings(s, m, n)
        
    


    
