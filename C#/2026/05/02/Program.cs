using System;

namespace MyApp
{
    internal class Program
    {
        public static void Main()
        {

            new Program().SolveADice();
        }

        public void SolveADice()
        {
            var X = int.Parse(Console.ReadLine());
            string ans = "No";
            for (int i = 1; i < 7; i++)
            {
                for (int j = 1; j < 7; j++)
                {
                    for (int k = 1; k < 7; k++)
                    {
                        if (i + j + k == X)
                        {
                            ans = "Yes";
                        }
                    }
                }
            }
            Console.WriteLine(ans);
        }
    }
}