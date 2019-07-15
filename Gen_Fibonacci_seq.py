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
    elm = []
#    print(inp_num,order)
    for N in range(order):    
        elm.append(1)
#    print(elm)
    for i in range(order,inp_num):
        new_elm = 0
        for N in range(1,order+1):
            new_elm += elm[i-N] 
        elm.append(new_elm)
#    print(elm)
    return elm
    
elm = Fibonacci_Sequence(inp_num, inp_order)

field_width = len(str(abs(elm[inp_num-1])))
#print(field_width)
field_width_format = '{:>'+'{}'.format(field_width)+'}'

#print(elm)
if inp_num == 0:
    print(field_width_format.format(0), 'with index number', 1)
else:
    for i in range(inp_num):
        print(field_width_format.format(elm[i]), 'with index number', i+1)
