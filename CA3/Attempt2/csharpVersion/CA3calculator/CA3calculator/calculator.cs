using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace CA3calculator
{
    class calculator
    {
        static void Main(string[] args)
        {

            /*
            > Define what a Calculator is.                  -- Create a class called Calculator

            > Ten methods:
            a.Add.User input will be "number", "operator", "number"
            b.Subtract.User input will be "number", "operator", "number"
            c.Multiply.User input will be "number", "operator", "number"
            d.Squared.User input will be "number", "operator"
            e.Cubed.User input will be "number", "operator"
            f.Divide.User input will be "number", "operator", "number"
            g.Factorial.User input will be "number", "operator"
            h.Square Root.User input will be "number", "operator"
            i.Power.User input will be "number", "operator", "number
            j.Ten to the Power Of.User input will be "number", "operator"

            > results can be intergers or decimals

            > User input
            - asks for the first number, and                                   -- 
            - asks what operation is to be performed
            - if appropriate asks for the second number

            > Output
            - result

            > All built starting with tests.
            */

            

            public class Calculator {
            // Methods to define how the calculator's operations will work >>
            decimal result = 0;
            //3. add 'add' function to define how 'add' should behave

            public void add(decimal first, decimal second)
            {
                result = first + second;
            //  4. add print statements to calculator_app
            }
            
            //9. add 'subtract' function to define how 'subtract' should behave
            public void subtract(decimal first, decimal second)
            {
                result = first - second;
            }
            //10. add print statements to calculator_app file

            //15. add 'multiply' function to define how 'multiply' should behave
            public void multiply(decimal first, decimal second)
            {
                result = first * second;
            }        
            //16. add print statements to calculator_app file
    
            //21. add 'squared' function to define how 'squared' should behave
            public void squared(decimal first)
            {
                result = first * first;
            }
            //22. add print statements to calculator_app file
    
            //27. add 'cubed' function to define how 'cubed' should behave
            public void cubed(decimal first)
            {
                result = first * first * first;
            }
            //28. add print statements to calculator_app file

            //33. add 'divide' function to define how 'divide' should behave
            public void divide(decimal first, decimal second)
            {
                if (second == 0)
                {
                    result = decimal.Parse(Console.WriteLine("Cannot divide by zero");
                }

                else
                {
                    result = first / second;
                }

            }
            //34. add print statements to calculator app file
    
            //40. having imported 'math', define a method for how 'factorial' should behave
            public double factorial_recursion(double first)
            {
                if (first == 1)
                {
                    result = 1;
                }

                else
                {
                    result = first * factorial_recursion(first - 1);
                }
                    
            }

            //41. add print statements to the calculator app file

            //46. add 'sqroot' function to define how 'sqroot' should behave
            public void sqroot(decimal first)
            {
                result = Math.Sqrt(first);
            }
            //47. add print statements to the calculator app file
    
            //52. add 'power' function to define how 'power' should behave
            public void power(decimal first, decimal second)
            {
                result = Math.Pow(first, second);
            }
            //53. add print statements to the calculator app file
    
            //58. add 'ten to the Power of' function to define how 'tenPower' should behave
            public void tenPower(decimal first)
            {
                result = Math.Pow(10, first);
            }
            //59. add print statements to the calculator app file

            }

            // 60. what can the user do?    
            public void menu()
            {
                Console.WriteLine("");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Welcome to the Calculator");
                Console.WriteLine("-------------------------");
                Console.WriteLine("");
                Console.WriteLine("This caculator performs the following operations:");
                Console.WriteLine("Add -- Press '+");
                Console.WriteLine("Subtract -- Press '-'");
                Console.WriteLine("Multiply -- Press '*'");
                Console.WriteLine("Squared -- Press 'S'");
                Console.WriteLine("Cubed -- Press 'C'");
                Console.WriteLine("Divide -- Press '/'");
                Console.WriteLine("Factorial -- Press 'F'");
                Console.WriteLine("Square Root -- Press 'R'");
                Console.WriteLine("To the Power Of -- Press 'P'");
                Console.WriteLine("Ten To the Power Of -- Press 'T'");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Enter/Return to 'equals'");
                Console.WriteLine("-------------------------");
                Console.WriteLine("Or, press 'E' to end.");
            }

            //63. define how 'run_calc' works
            public void run_calc(decimal store_inputA, string store_operation)
            {
            decimal store_inputA = ' ';
            string store_operation = " ";

            if (store_operation == '+')
            {
                string b = Console.ReadLine("Enter second number: ");
                decimal bb;
                decimal bbb = decimal.TryParse(b, out bb);
                result = self.add(store_inputA, b);
            }
            else (store_operation == '-')
            {

            }
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




            }








    }
}



    
    



        
        

    */
      