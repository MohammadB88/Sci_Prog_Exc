# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:15:00 2019

@author: mb1988
"""
import math 

number = int(input('Please enter a positive integer number more than "1": '))

sign_prime = 'true'

i=1
while 2*i+1 <= int(math.sqrt(number)) :
    if number%2 == 0 or number%(2*i+1) == 0  :
        #print(number, 2*i+1, number%(2*i+1))
        sign_prime = 'false'
        break
    i += 1

print('\nYou entered this number: "{}" '.format(number))
if number <= 1 :
    print('\nI asked for a number greater than "1"!!! \nI am sorry but I have to stop the script!!!')   
else:
    if number == 2 or number == 3:
        print('\nYou hit the jackpot!!! \n"{}" is a prime number!'.format(number))
    elif sign_prime == 'false' :
        print('\nIt seems "{}" is not a prime number! \nMaybe next time you will get more lucky!'.format(number))
    else :
        print('\nYou hit the jackpot!!! \n"{}" is a prime number!'.format(number))
        

