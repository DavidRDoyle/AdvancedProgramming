# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:08:02 2018

@author: David Doyle
"""

"""
> Define what a Calculator is.                  -- Create a class called Calculator

> Ten methods:
    a. Add. User input will be "number", "operator", "number"
    b. Subtract. User input will be "number", "operator", "number"
    c. Multiply. User input will be "number", "operator", "number"
    d. Squared. User input will be "number", "operator"
    e. Cubed. User input will be "number", "operator"
    f. Divide. User input will be "number", "operator", "number"
    g. Factorial. User input will be "number", "operator"
    h. Square Root. User input will be "number", "operator"
    i. Power. User input will be "number", "operator", "number
    j. Ten to the Power Of. User input will be "number", "operator"

> results can be intergers or decimals

> User input
- asks for the first number, and                                   -- 
- asks what operation is to be performed
- if appropriate asks for the second number

> Output
- result

> All built starting with tests.

"""

#39. import the math module to make defining the method for 'factorial' easier
import math

class Calculator:
# Methods to define how the calculator's operations will work >>
        
    #3. add 'add' function to define how 'add' should behave
    def add(self, first, second):
        return first + second
    #4. add print statements to calculator_app
    
     #9. add 'subtract' function to define how 'subtract' should behave
    def subtract(self, first, second):
        return first - second
    #10. add print statements to calculator_app file
    
    #15. add 'multiply' function to define how 'multiply' should behave
    def multiply(self, first, second):
        return first * second
    #16. add print statements to calculator_app file
    
    #21. add 'squared' function to define how 'squared' should behave
    def squared(self, first):
        return first * first
    #22. add print statements to calculator_app file
    
    #27. add 'cubed' function to define how 'cubed' should behave
    def cubed(self, first):
        return first * first * first
    #28. add print statements to calculator_app file
    
    #33. add 'divide' function to define how 'divide' should behave
    def divide(self, first, second):
        if second == 0:
            return "Cannot divide by zero"
        else:
            return float(first) / float(second)
    #34. add print statements to calculator app file
    
    #40. having imported 'math', define a method for how 'factorial' should behave
    def factorial(self, first):
        return math.factorial(first)
    #41. add print statements to the calculator app file
    
    #46. add 'sqroot' function to define how 'sqroot' should behave
    def sqroot(self, first):
        return math.sqrt(first)
    #47. add print statements to the calculator app file
    
    #52. add 'power' function to define how 'power' should behave
    def power(self, first, second):
        return first ** second
    #53. add print statements to the calculator app file
    
    #58. add 'ten to the Power of' function to define how 'tenPower' should behave
    def tenPower(self, first):
        return float(10**first)
    #59. add print statements to the calculator app file
    
    # 60. what can the user do?    
    def menu(self):
        print ""
        print "-------------------------"
        print "Welcome to the Calculator"
        print "-------------------------"
        print ""
        print "This caculator performs the following operations:"
        print "Add -- Press '+"
        print "Subtract -- Press '-'"
        print "Multiply -- Press '*'"
        print "Squared -- Press 'S'"
        print "Cubed -- Press 'C'"
        print "Divide -- Press '/'"
        print "Factorial -- Press 'F'"
        print "Square Root -- Press 'R'"
        print "To the Power Of -- Press 'P'"
        print "Ten To the Power Of -- Press 'T'"
        print "-------------------------"
        print "Enter/Return to 'equals'"
        print "-------------------------"
        print "Or, press 'E' to end."
    
    #63. define how 'run_calc' works
    store_inputA = ' '
    store_operation = ' '
    
    def run_calc(self, store_inputA, store_operation):
        
        if store_operation == '+':
            b = float(raw_input("Enter second number: "))
            result = self.add(store_inputA, b)
            
        elif store_operation == '-':
            b = float(raw_input("Enter second number: "))
            result = self.subtract(store_inputA, b)
        
        elif store_operation == '*':
            b = float(raw_input("Enter second number: "))
            result = self.multiply(store_inputA, b)
        
        elif store_operation == 'S':
            result = self.squared(store_inputA)
        
        elif store_operation == 'C':
            result = self.cubed(store_inputA) 
        
        elif store_operation == '/':
            b = float(raw_input("Enter second number: "))
            result = self.divde(store_inputA, b)
        
        elif store_operation == 'F':
            result = self.factorial(store_inputA) 
        
        elif store_operation == 'R':
            result = self.sqroot(store_inputA) 
        
        elif store_operation == 'P':
            result = self.power(store_inputA) 
        
        elif store_operation == 'T':
            result = self.tenPower(store_inputA)
        
        else:
            result = "Not a valid entry. Please try again."
        return result
        
   