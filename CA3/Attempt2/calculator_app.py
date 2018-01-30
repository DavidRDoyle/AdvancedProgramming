# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:42:04 2018

@author: David Doyle
"""
from calculator import Calculator

my_calc = Calculator()

#61. print the menu for the user when the program starts
my_calc.menu()
a = ''

#62. ask the user for their first number
while a != 'E':
    
    a = raw_input("Enter the first number: ")
      
    if a == 'E':
        print "Goodbye. Call Again"
    
    elif a.isdigit():
        store_inputA = float(a)
        print store_inputA
        o = raw_input("Enter the operation you want: ")
        store_operation = o
        print "Answer: " + str(my_calc.run_calc(store_inputA, store_operation))
    
    else:
        print "That wasn't a number. Try again: "
    
    #63. run - error comes back saying my_calc has no instance attribute of 'run_calc' method. therefore go to calculator file and define it.

         





