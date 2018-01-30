using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace CA3calculator
{
    class calculator_app
    {

        calculator my_calc = new Calculator();

        //#61. print the menu for the user when the program starts
        return my_calc.menu();

        string a;

        //#62. ask the user for their first number
        while a != 'E'
    
             Console.WriteLine(Console.ReadLine("Enter the first number: "));
      
            if (a == 'E')
            {

                Console.WriteLine("Goodbye. Call Again");
            }
            else (a.isdigit())
            {
                store_inputA = float(a)
                print store_inputA
                o = raw_input("Enter the operation you want: ")
                store_operation = o
                Console.WriteLine("Answer: " + str(my_calc.run_calc(store_inputA, store_operation)));
            }
            else:
               Console.WriteLine( "That wasn't a number. Try again: ");

            //#63. run - error comes back saying my_calc has no instance attribute of 'run_calc' method. therefore go to calculator file and define it.






    }
}







