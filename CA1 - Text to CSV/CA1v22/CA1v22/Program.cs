using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;


namespace CA1v22
{
    class Program
    {

        static void Main(string[] args)
        {

            //Read the file into an array. Declare where the parsed results will be stored (in a list).
            string[] lines = File.ReadAllLines(@"C:\Users\David Doyle\Documents\AdvProg\CA1 - Text to CSV\commit_changes.txt");
            List<string> output = new List<string>();
            string csvFile = @"C:\Users\David Doyle\Documents\AdvProg\CA1 - Text to CSV\output.csv";

            //Each 'section' of the file is separated by a line of 72 hyphens and also contains a blank line
            string mainSeparator = new string('-', 72);


            //Begin parsing. Find starting point, then while it is less than the length of the array (-1 for index), 
            //loop
            int startAt = Array.IndexOf(lines, mainSeparator);

            while (startAt < lines.Length - 1)
            {

                //Find the relevant points within each section, i.e. the last set of hyphens,
                //and the empty line in the middle

                int middle = Array.IndexOf(lines, String.Empty, startAt + 1);
                int endAt = Array.IndexOf(lines, mainSeparator, startAt + 1);
                
                //start of section
                if (lines[startAt] == mainSeparator)
                {
                    //get rid of any commas in the middle of lines I want to keep to make it easier to send
                    //to CSV when that time comes. Then splt this part of the section by pipe.
                    string[] parts = lines[startAt + 1].Replace(",", "").Split(new[] { " | " }, StringSplitOptions.None);
                    foreach (string part in parts)
                    {
                        output.Add(part);
                    }

                    // middle of section
                    int i = 3;
                    string midString = "";

                    while (startAt + i < middle)
                    {
                        
                        midString = midString + string.Join(";;", lines[startAt + i].Replace(",", "").Trim());
                        i += 1;
                        
                    }

                    output.Add(midString);

                    //end of section
                    int j = 1;
                    string endString = "";
                    while (middle + j < endAt)
                    {
                        endString = endString + string.Join(";;", lines[middle + j].Replace(",", "").Trim());
                        j += 1;
                    }

                    output.Add(endString);

                }

                startAt += 1;

            }

            StreamWriter sw = File.AppendText(csvFile);
            for (int x = 0; x <= output.Count-6; x = x+6)
            {
                sw.WriteLine(output[x] + "," + output[x + 1] + "," + output[x + 2] + "," + output[x + 3] + "," + output[x + 4]+ "," + output[x+5]);
                
            }
        }
    }
}
