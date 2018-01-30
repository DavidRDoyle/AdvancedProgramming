# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:20:48 2018

@author: David Doyle
"""

from calculator import Calculator

#62. comment out the print statements as the testing of the functions is now complete
'''
calculator = Calculator()


#5. add print statements for 'add' function in case they are needed to be viewed
print "Add"
print calculator.add(2,2)
print calculator.add(2,3)
print calculator.add(2,-3)
print calculator.add(2,-2)
print calculator.add(2,0)
#6. go back to calculator_test and run to see if there are any errors.

#11. add print statements for 'subtract' function in case they need to be viewed
print "Subtract"
print calculator.subtract(2,2)
print calculator.subtract(2,3)
print calculator.subtract(2,-3)
print calculator.subtract(2,0)
print calculator.subtract(0,2)
print calculator.subtract(-2,-3)
#12. go back to calculator_test and run to see if there are any errors.

#17. add print statements for 'multiply' function in case they need to be viewed
print "Multiply"
print calculator.multiply(2,2)
print calculator.multiply(2,3)
print calculator.multiply(2,-3)
print calculator.multiply(2, 0)
print calculator.multiply(-2,-2)
#18. go back to calculator_test and run to see if there are any errors

#23. add print statements for 'squared' function in case they need to be viewed
print "Squared"
print calculator.squared(0)
print calculator.squared(1)
print calculator.squared(2)
print calculator.squared(3)
print calculator.squared(-2)
print calculator.squared(2.5)
#24. go back to calculator_test and run to see if there are any errors

#29. add print statements for 'cubed' function in case they need to be viewed
print "Cubed"
print calculator.cubed(1)
print calculator.cubed(2)
print calculator.cubed(3)
print calculator.cubed(-3)
#30. go back to calculator_test and run to see if there are any errors

#35. add print statements for 'divide' function in case they are needed
print "Divide"
print calculator.divide(0,2)
print calculator.divide(2,1)
print calculator.divide(2,2)
print calculator.divide(4,2)
print calculator.divide(5,2)
print calculator.divide(8,-4)
print calculator.divide(-8,-4)
#36. go back to calculator_test and run to see if there are any errors

#42. add print statements for 'factorial' function in case they are needed
print "Factorial"
print calculator.factorial(0)
print calculator.factorial(1)
print calculator.factorial(2)
print calculator.factorial(3)
print calculator.factorial(4)
#43. go back to calculator_test and run to see if there are any errors

#48. add print statements for 'sqroot' function in case they are needed
print "Square Root"
print calculator.sqroot(25)
print calculator.sqroot(64)
print calculator.sqroot(1)
#49. go back to calculator test and run to see if there are any errors

#54. add print statements for 'power' function in case they are needed
print "Power"
print calculator.power(0,0)
print calculator.power(0,1)
print calculator.power(1,1)
print calculator.power(1,2)
print calculator.power(2,1)
print calculator.power(2,2)
print calculator.power(2,5)
print calculator.power(-2,5) 
#55. go back to calculator test and run to see if there are any errors

#60. ad print statements for 'tenPower' function in case they are needed
print 'TenToThePowerOf"
print calculator.tenPower(2)
print calculator.tenPower(8)
print calculator.tenPower(0)
print calculator.tenPower(-2)
#61. go back to calculator test and run to see if there are any errors
'''
#62. comment out all of the print statements as the testing of the functions is now complete

#63. include the code requesting the user's raw input
my_calc = Calculator()
value = ''
while value != 'E':
   value = raw_input('Press Number or E to Finish: ')
   my_calc.input(value)
   print my_calc.getOutput()
#64. run - get the error saying 'no attribute of 'input', so add input to Calculator file