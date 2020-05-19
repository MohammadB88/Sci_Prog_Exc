# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:34:01 2019

@author: mb1988
"""

# ***** The Generalized Fibonacci numbers start from "1" not "0"!!! ***** 

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
    elm_fib = []
#    print(inp_num,order)
    for N in range(order):    
        elm_fib.append(1)
#    print(elm_fib)
    for i in range(order,inp_num):
        fibo = 0
        for N in range(1,order+1):
            fibo += elm_fib[i-N] 
        elm_fib.append(fibo)
#    print(elm_fib)
    return elm_fib

# return an array of Fibonacci numbers
def Fibonacci_Sequence(inp_num, order=2):
    """ calculates generalized Fibonacci-numbers
    
    Generalized Fibonacci-numbers are obtained by summing up the previous N numbers
    of the series, where N is the order of the Fibonacci-numbers. The conventional
    Fibonacci-series can be obtained with N=2.
    
    Args:
        inp_num: Number of terms to calculate.
        order: Order of Fibonacci-numbers (Optional, default: 2).
        
    Returns:
        List of Fibonacci-numbers.
    """
    elm_fib = np.empy(inp_num, dtype=int)
    elm_fib[0 : min(inp_num, order)] = 1
    for itm in range(order, inp_num):
        elm_fib[itm] = np.sum(elm_fib[itm - order: itm])
    return elm_fib

fibbos = Fibonacci_Sequence(inp_num, inp_order)

field_width = len(str(abs(fibbos[inp_num-1])))
#print(field_width)
field_width_format = '{:>'+'{}'.format(field_width)+'}'

#print(fibbos)
if inp_num == 0:
    print(field_width_format.format(0), 'with index number', 1)
else:
    for i in range(inp_num):
        print(field_width_format.format(fibbos[i]), 'with index number', i+1)
