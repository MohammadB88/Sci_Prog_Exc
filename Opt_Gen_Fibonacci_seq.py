# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 18:03:28 2019

@author: mb1988
"""

# ***** The Optimized Generalized Fibonacci numbers start from "1" not "0"!!! ***** 

while True:    
    inp_num = int(input('How many numbers in the Fibonacci Sequence do you want me to print (an integer number more than 0): '))
    inp_order = int(input('In which order do you want them (an integer number between 1 and the Fibonacci number): '))
    if inp_num == 0:
        print('You entered "0" for the Fibonacci number.')
        continue
    elif inp_order == 1 or inp_order > inp_num:
        print('You entered the wrong number for the order.')
        continue        
    else:
        break

def Fibonacci_Sequence(inp_num, order=2):
    """ Calculates Generalized Fibonacci-numbers.

    Generalized Fibonacci-numbers are obtained by summing up the previous N numbers
    of the series, where N is the order of the Fibonacci-numbers. The conventional
    Fibonacci-series can be obtained with N=2.
    
    This functions uses an optimized algorithm without explicit summation.
    
    Arg:
        inp_num: Number of terms to calculate.
        order:   Order of Fibonacci-numbers (Optional, default: 2).
        
    return:
        List of Fibonacci-numbers
    """
    elm_fibo = []
#    print(inp_num,order)
    for N in range(order):    
        elm_fibo.append(1)
#    print(elm_fibo)
    elm_fibo.append(order)
    for i in range(order+1,inp_num):
        fibo = 2 * elm_fibo[i - 1] - elm_fibo[i - order - 1]
#        print(elm[i - order - 1])
        elm_fibo.append(fibo)
#    print(elm_fibo)
    return elm_fibo

#Fibonacci_Sequence(inp_num, inp_order)
fibbos = Fibonacci_Sequence(inp_num, inp_order)

field_width = len(str(abs(fibbos[inp_num-1])))
#print(field_width)
field_width_format = '{:>'+'{}'.format(field_width)+'}'

#print(elm)
if inp_num == 0:
    print(field_width_format.format(0), 'with index number', 1)
else:
    for i in range(inp_num):
        print(field_width_format.format(fibbos[i]), 'with index number', i+1)
