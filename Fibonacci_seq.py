# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:06:45 2019

@author: mb1988
"""
while True:    
    inp_num = int(input("""How many numbers in the Fibonacci Sequence 
    do you want me to print (an integer number more than 0): """))
    if inp_num == 0:
        print('You entered "0". Please enter an integer number more than 0.')
        continue
    else:
        break

def Fibonacci_Sequence(inp_num):
    elm = []
    elm.append(0)
    elm.append(1)
    for i in range(2,inp_num):
        elm.append(elm[i-2] + elm[i-1])
#    print(elm)
    return elm
    
elm = Fibonacci_Sequence(inp_num)

field_width = len(str(abs(elm[inp_num-1])))
print(field_width)
field_width_format = '{:>'+'{}'.format(field_width)+'}'

#print(elm)
if inp_num == 0:
    print(field_width_format.format(0), 'with index number', 1)
else:
    for i in range(inp_num):
        print(field_width_format.format(elm[i]), 'with index number', i+1)
