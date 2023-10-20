#!/usr/bin/env python3

def return_evens(num_list):
    if (num_list == None): return None;
    elif (len(num_list) < 1): return [];
    else: return [num for num in num_list if (num % 2 == 0)];

def make_exclamation(sentence_list):
    if (sentence_list == None): return None;
    elif (len(sentence_list) < 1): return [];
    else: return [phrase + "!" for phrase in sentence_list];
