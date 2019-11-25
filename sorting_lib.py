#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:12:34 2019

@author: marco
"""

def counting_sort_integers(input_int_list):
    ''' Here I'm supposing to know the values range, which is [0-9], all are integers'''
    counter = [0] * (9+1) # From 0-9 -> 10 elements in counter array
    
    #counter = [0] * (max(input_int_list) + 1) # This could be used in case I didn't know the max possible value in the list. It's against the definition of counting sort though.
    
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
    
    # Initializing the dict that will act as counter, will run in constant time.
    letters = 'abcdefghijklmnopqrstuvwxyz'
    counter_letters = dict.fromkeys(list(letters), 0)
    
    # Counting the occurrences of the letters in the input string 
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



