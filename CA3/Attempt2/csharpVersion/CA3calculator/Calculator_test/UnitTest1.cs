using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Calculator_test : Calculator
{
    [TestClass]
public class UnitTest1
{
    [TestMethod]
    public void TestMethod1()
    {




        public void class CalculatorTest
    {
        //#1. add a test - Add
        public void test_Add()
        {
            var calculator = new Calculator();

            this.Equals(4, calculator.add(2, 2));
            this.Equals(5, calculator.add(2, 3));
            this.Equals(-1, calculator.add(2, -3));
            this.Equals(0, calculator.add(2, -2));
            this.Equals(2, calculator.add(2, 0));
            this.Equals(-5, calculator.add(-2, -3));
        }

        //  #2. run - error comes back saying no attribute for 'add'. So go to calculator file and add 'add' function

        //#7. add a test - Subtract
        public void test_Subtract()
        {
            var calculator = new Calculator();

            this.Equals(0, calculator.subtract(2, 2));
            this.Equals(-1, calculator.subtract(2, 3));
            this.Equals(5, calculator.subtract(2, -3));
            this.Equals(2, calculator.subtract(2, 0));
            this.Equals(-2, calculator.subtract(0, 2));
            this.Equals(1, calculator.subtract(-2, -3));


        }
        //#8. run - error comes back saying no attribute for 'subtract'. So go to calculator file and add 'subtract' function

        //#13. add a test - Multiply
        public void test_Multiply()
        {
            var calculator = new Calculator();

            this.Equals(4, calculator.multiply(2, 2));
            this.Equals(6, calculator.multiply(2, 3));
            this.Equals(-6, calculator.multiply(2, -3));
            this.Equals(0, calculator.multiply(2, 0));
            this.Equals(4, calculator.multiply(-2, -2));
        }
        //#14. run - error comes back saying no attribute for 'multiply'. So go to calculator file and add 'multiply' function

        //#19. add a test - Squared
        public void test_Squared()
        {
            var calculator = new Calculator();
            this.Equals(0, calculator.squared(0));
            this.Equals(1, calculator.squared(1));
            this.Equals(4, calculator.squared(2));
            this.Equals(9, calculator.squared(3));
            this.Equals(4, calculator.squared(-2));
            this.Equals(6.25, calculator.squared(2.5));
        }
        //#20 run - error comes back saying no attribute for 'squared'. So go to calculatro file and add 'squared' function

        //#25. add a test - Cubed
        public void test_Cubed()
        {
            var calculator = new Calculator();
            this.Equals(0, calculator.cubed(0));
            this.Equals(1, calculator.cubed(1));
            this.Equals(8, calculator.cubed(2));
            this.Equals(27, calculator.cubed(3));
            this.Equals(-27, calculator.cubed(-3));
        }
        //#26. run - error comes back saying no attribute for 'cubed'. So go to calculator file and add 'cubed' function

        //#31. add a test - Divide
        public void test_Divide()
        {
            var calculator = new Calculator();
            this.Equals(0, calculator.divide(0, 2));
            this.Equals(2, calculator.divide(2, 1));
            this.Equals(1, calculator.divide(2, 2));
            this.Equals(2, calculator.divide(4, 2));
            this.Equals(2.5, calculator.divide(5, 2));
            this.Equals(-2, calculator.divide(8, -4));
            this.Equals(2, calculator.divide(-8, -4));
        }
        //#32. run - error comes back saying no attribute for 'divide'. So go to calculator file and add 'divide' function

        //#37. add a test - Factorial
        public void test_Factorial()
        {
            var calculator = new Calculator();
            this.Equals(1, calculator.factorial(0));
            this.Equals(1, calculator.factorial(1));
            this.Equals(2, calculator.factorial(2));
            this.Equals(6, calculator.factorial(3));
            this.Equals(24, calculator.factorial(4));
        }
        //#38. run - error comes back saying no attribute for 'factorial', so go to calculator file and add 'factorial' function.

        //#44. add a test - Square Root
        public void test_SqRoot()
        {
            var calculator = new Calculator();
            this.Equals(5, calculator.sqroot(25));
            this.Equals(8, calculator.sqroot(64));
            this.Equals(1, calculator.sqroot(1));
        }
        //#45. run - error comes back saying no attribute for 'sqroot', so go to calculator file and add 'sqroot' function

        //#50. add a test - Power
        public void test_Power()
        {
            var calculator = new Calculator();
            this.Equals(1, calculator.power(0, 0));
            this.Equals(0, calculator.power(0, 1));
            this.Equals(1, calculator.power(1, 1));
            this.Equals(1, calculator.power(1, 2));
            this.Equals(2, calculator.power(2, 1));
            this.Equals(4, calculator.power(2, 2));
            this.Equals(32, calculator.power(2, 5));
            this.Equals(-32, calculator.power(-2, 5));
        }
        //#51. run - error comes back saying no attribute for 'power', so go to calculator file and add 'power' function

        //#56 add a test - 10Power
        public void test_TenPowerX()
        {
            var calculator = new Calculator();
            this.Equals(100, calculator.tenPower(2));
            this.Equals(100000000, calculator.tenPower(8));
            this.Equals(1, calculator.tenPower(0));
            this.Equals(0.01, calculator.tenPower(-2));
        }
        //#57. run - error comes back saying no attribute for 'tenPower' so go to calculator file and add 'tenPower' function
    
    

        }
    }
}

