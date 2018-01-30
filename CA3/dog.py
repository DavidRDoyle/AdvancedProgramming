# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:02:36 2018

@author: David Doyle
"""

class dog:                      #create a class
    number_of_legs = 4          #define properties of the class
    breed = "labrador"
    color = "golden"
    
ruffles = dog()                 #create an object of that class

print ruffles.number_of_legs    #access a property of that class
print ruffles.breed
print ruffles.color

print "Ruffles has " + str(ruffles.number_of_legs) + " legs"



class bigDog:
    
    def __init__(self, x):  #
        self.speed = x

    def get_speed(self):
        print(self.speed)
        

rooney = bigDog(3)      
chui = bigDog(7)                #created two objects with different speeds
                                #from the same class

rooney.get_speed()
chui.get_speed()



class Girl:                     #create a class
    
    gender = "female"           #class variable
    
    def __init__(self, name):   #
        self.name = name        #instance variable
        
r = Girl("Rachel")              
s = Girl("Susan")

print "The girl %s is a %s" % (r.name, r.gender)
print "The other girl %s is a %s" % (s.name, s.gender)



choice = raw_input("Enter the number you want: ")
print choice * 2
# enter '4' but this prints 44 because raw_input deals with strings. so it prints '4' twice, i.e. '4''4' 

# to get numbers, use just 'input'
choice = input("Enter the number you want: ")
print choice *2
# enter '4' but prints 8




while True:
    try:
        a = input("Enter the first number: ")
        break
    except:
        print "What the whatsa? Try again. Enter the first number: "
        
        
store_inputA = float(a)

o = raw_input("Enter the operation you want: ")
store_operation = o

if store_operation == '+':
    
    while True:
        try:
            b = float(raw_input("Enter second number: "))
            break
        except:
            print "You're having a laugh now. Enter a second NUMBER: "
            
    result = store_inputA + b
elif store_operation == 'S':
    result = store_inputA**2    
    
print result




