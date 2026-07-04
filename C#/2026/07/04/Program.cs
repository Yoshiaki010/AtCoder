using System;
using System.ComponentModel.Design;
using System.Runtime.CompilerServices;

namespace Solve0704
{
    public class Solver()
    {
        public static void Main(string[] args)
        {
            Console.WriteLine(args.ToString());
            var solver = new Solver();
            solver.SolveA();
        }

        private void SolveB()
        {
        }
        private void SolveA()
        {
            var input = Console.ReadLine();
            List<int> lis = In(input);

            var A = lis[0];
            var B = lis[1];

            var ans = "Uknow";
            if (A > B * 2 / 3)
            {
                ans = "Yes";
            }
            else
            {
                ans = "No";
            }

            Console.WriteLine(ans);
        }

        private List<int> In(string? input)
        {
            if (input == null)
            {
                return new List<int>();
            }

            var lis = new List<int>();
            var oneChr = "";
            for (var i = 0; i < input.Length; i++)
            {
                oneChr += input[i];

                if (input[i] == ' ')
                {
                    if (oneChr != "")
                    {
                        lis.Add(int.Parse(oneChr));
                        oneChr = "";
                    }
                    else
                    {
                        oneChr = "";
                    }
                }
            }
            if (oneChr != "")
            {
                lis.Add(int.Parse(oneChr));
            }
            return lis;
        }
    }
}