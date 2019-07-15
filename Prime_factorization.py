# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:22:31 2019

@author: mb1988
"""

import math 
import time

number = int(input('Please enter a positive integer number more than "1": '))

sign_prime = 'true'

t0 = time.time()

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

list_elm = [] 
new_number = number

j = 1
for k in range(number):
#    print(new_number)    
    if int(new_number)%2 == 0 :
        print(new_number, 2, new_number%2)
        new_number = int(new_number)/2
        list_elm.append(2)
#        print(new_number%2)
        if new_number/2 == 1.0:
            break
        j = j-1
    elif int(new_number)%(2*j+1) == 0 :
        print(new_number, 2*j+1, new_number%(2*j+1))
        new_number = int(new_number)/(2*j+1)
        list_elm.append(2*j+1)
#        print(new_number/(2*j+1))
        if new_number == 1.0:
#            print('break')
            break
        j = j-1
    j += 1

#print(list_elm)

print('\nHowever {} is a combination of these prime numbers: \n'.format(number))

for idx in range(len(list_elm)):
    print('Prime number: {} , times: {} '.format(list_elm[idx], list_elm.count(list_elm[idx]))) 
    idx += 1
print('In order not to print redundant numbers, I have to use "dictionary"')

t1 = time.time()
print('TIme required: ', t1 - t0)