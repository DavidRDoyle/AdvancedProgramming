# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:54:19 2018

@author: David Doyle
"""


'''Calculator Requirements

> Caclculator starts by asking user for input. Input can be a number 

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
        
        '''




#39. import the math module to make defining the method for factorial easier
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
    
    
# function to take user's inputs and choice of operation >>
    

