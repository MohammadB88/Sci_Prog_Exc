# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:27:55 2019

@author: mb1988
"""

# This script only works for words but not sentences!!!
# ********** Next step would be to generalize it so that it works for sentences as well. ********** 

list_letter = []
list_reverse_letter = []

print('Please write only one word at a time. \nI will check if it is a "Palindrome". \nWrite "Q" or "q" to quit.')

#while True:
#for itr in range(10):
while True:
    word = input('Now what is the word on your mind? ')
    if word == 'Q' or word == 'q':
        break
    elif ' ' in word:
        print('You have written more than one word.')
        word = input('Please write only one word: ')
    list_letter = list(word.lower())
    print(list_letter)
    list_reverse_letter = list_letter.copy()
    list_reverse_letter.reverse()
    print(list_reverse_letter)
    print(list_letter)
    if list_letter == list_reverse_letter:
        print('Ta da!!! "{}" is a Palindrome!!!'.format(word))
    else:
        print('"{}" is not a Palindrome!!!'.format(word))
    
    list_letter.clear()
    list_reverse_letter.clear()
