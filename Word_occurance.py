# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:03:28 2019

@author: mb1988
"""

import operator

sentence = input('just write a sentence and do not use colons or semicolons: \n')

word = sentence.rstrip().split()

print('\nHere is a list of all the word in that sentence: \n', word)

#print(word.count('the'))

lower_word = dict()
for itr in word:
    lower_itr = itr.lower()
    lower_word[lower_itr] = lower_word.get(lower_itr, 0) + 1

#print(lower_word, '\n')

sorted_lower_word = sorted(lower_word.items(), key=operator.itemgetter(1), reverse=True)

print('\nThis is a sorted list of words in this sentence from the most abundant to the least abundant word: ')
for key,value in sorted_lower_word:
    print(key, value)
    
bigcount = None
bigword = None
for word,count in lower_word.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
        
print('\nThe most repeatable word "{}" is repeated "{}" times.'.format(bigword,bigcount))