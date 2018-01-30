# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:49:00 2018

@author: David Doyle
"""

#Attempt1


#Start by writing a failing test using the unittest module, then import Calculator from calculator




import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    #1. add a test - Add
    def test_Add(self):
        calculator = Calculator()
        self.assertEqual(4, calculator.add(2, 2))
        self.assertEqual(5, calculator.add(2, 3))
        self.assertEqual(-1, calculator.add(2, -3))
        self.assertEqual(0, calculator.add(2, -2))
        self.assertEqual(2, calculator.add(2, 0))
        self.assertEqual(-5, calculator.add(-2, -3))
    #2. run - error comes back saying no attribute for 'add'. So go to calculator file and add 'add' function
    
    #7. add a test - Subtract
    def test_Subtract(self):
        calculator = Calculator()
        self.assertEqual(0, calculator.subtract(2,2))
        self.assertEqual(-1, calculator.subtract(2,3))
        self.assertEqual(5, calculator.subtract(2,-3))
        self.assertEqual(2, calculator.subtract(2,0))
        self.assertEqual(-2, calculator.subtract(0,2))
        self.assertEqual(1, calculator.subtract(-2,-3))
    #8. run - error comes back saying no attribute for 'subtract'. So go to calculator file and add 'subtract' function
    
    #13. add a test - Multiply
    def test_Multiply(self):
        calculator = Calculator()
        self.assertEqual(4, calculator.multiply(2,2))
        self.assertEqual(6, calculator.multiply(2,3))
        self.assertEqual(-6, calculator.multiply(2,-3))
        self.assertEqual(0, calculator.multiply(2, 0))
        self.assertEqual(4, calculator.multiply(-2,-2))
    #14. run - error comes back saying no attribute for 'multiply'. So go to calculator file and add 'multiply' function
    
    #19. add a test - Squared
    def test_Squared(self):
        calculator = Calculator()
        self.assertEqual(0, calculator.squared(0))
        self.assertEqual(1, calculator.squared(1))
        self.assertEqual(4, calculator.squared(2))
        self.assertEqual(9, calculator.squared(3))
        self.assertEqual(4, calculator.squared(-2))
        self.assertEqual(6.25, calculator.squared(2.5))
    #20 run - error comes back saying no attribute for 'squared'. So go to calculatro file and add 'squared' function
    
    #25. add a test - Cubed
    def test_Cubed(self):
        calculator = Calculator()
        self.assertEqual(0, calculator.cubed(0))
        self.assertEqual(1, calculator.cubed(1))
        self.assertEqual(8, calculator.cubed(2))
        self.assertEqual(27, calculator.cubed(3))
        self.assertEqual(-27, calculator.cubed(-3))
    #26. run - error comes back saying no attribute for 'cubed'. So go to calculator file and add 'cubed' function
    
    #31. add a test - Divide
    def test_Divide(self):
        calculator = Calculator()
        self.assertEqual(0, calculator.divide(0,2))
        self.assertEqual(2, calculator.divide(2,1))
        self.assertEqual(1, calculator.divide(2,2))
        self.assertEqual(2, calculator.divide(4,2))
        self.assertEqual(2.5, calculator.divide(5,2))
        self.assertEqual(-2, calculator.divide(8,-4))
        self.assertEqual(2, calculator.divide(-8,-4))
    #32. run - error comes back saying no attribute for 'divide'. So go to calculator file and add 'divide' function
    
    #37. add a test - Factorial
    def test_Factorial(self):
        calculator = Calculator()
        self.assertEqual(1, calculator.factorial(0))
        self.assertEqual(1, calculator.factorial(1))
        self.assertEqual(2, calculator.factorial(2))
        self.assertEqual(6, calculator.factorial(3))
        self.assertEqual(24, calculator.factorial(4))
    #38. run - error comes back saying no attribute for 'factorial', so go to calculator file and add 'factorial' function.
    
    #44. add a test - Square Root
    def test_SqRoot(self):
        calculator = Calculator()
        self.assertEqual(5, calculator.sqroot(25))
        self.assertEqual(8, calculator.sqroot(64))
        self.assertEqual(1, calculator.sqroot(1))
    #45. run - error comes back saying no attribute for 'sqroot', so go to calculator file and add 'sqroot' function
    
    #50. add a test - Power
    def test_Power(self):
        calculator = Calculator()
        self.assertEqual(1, calculator.power(0,0))
        self.assertEqual(0, calculator.power(0,1))
        self.assertEqual(1, calculator.power(1,1))
        self.assertEqual(1, calculator.power(1,2))
        self.assertEqual(2, calculator.power(2,1))
        self.assertEqual(4, calculator.power(2,2))
        self.assertEqual(32, calculator.power(2,5))
        self.assertEqual(-32, calculator.power(-2,5))    
    #51. run - error comes back saying no attribute for 'power', so go to calculator file and add 'power' function
    
    #56 add a test - 10Power
    def test_TenPowerX(self):
        calculator = Calculator()
        self.assertEqual(100, calculator.tenPower(2))
        self.assertEqual(100000000, calculator.tenPower(8))
        self.assertEqual(1, calculator.tenPower(0))
        self.assertEqual(0.01, calculator.tenPower(-2)) 
    #57. run - error comes back saying no attribute for 'tenPower' so go to calculator file and add 'tenPower' function
    
    
        
    
    



unittest.main()