#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:12:34 2019

@author: marco
"""


''' The counting sort here is implemented using the feature that python dictionaries
    provide: ordering of the keys while preserving access in constant time'''
    
# Initializing the dict that will act as counter, will run in constant time.
letters = 'abcdefghijklmnopqrstuvwxyz'
counter_letters = dict.fromkeys(list(letters), 0)

input_str = 'abaccdnnvjjf'

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
        
    