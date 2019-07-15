# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:04:57 2019

@author: mb1988
"""

sentence = input('just write a sentence and do not use colons or semicolons: \n')

word = sentence.rstrip().split()

print('\nHere is a list of all the word in that sentence: \n', word)

lower_word = []
for itr in word:
    lower_itr = itr.lower()
    if lower_itr not in lower_word:
        lower_word.append(lower_itr)    
#    print(lower_word)

sorted_lower_word = lower_word.copy()
sorted_lower_word.sort()

print('\nHere is a list of all the word in that sentence in lower case: \n', lower_word)

print('\nHere is what the excercise is asking for: ')
for sorted_itr in sorted_lower_word:
    print(sorted_itr+'; ', end='')
