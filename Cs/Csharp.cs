using System;
public class Program{
    public static void Main(){
        //以下の２行は含めない
        var exStdIn = new System.IO.StreamReader("stdin.txt");
        System.Console.SetIn(exStdIn);

        Console.WriteLine("打ち上げたい回数を入力し、ENTERキーを入力してください。");
        int num = Console.ReadLine();
        Console.Write(num);
        num = int.Parse(num);

        for (int i = 0; i<=num;i++){
            Console.Write(i);
            Console.Write("回目の花火：＊");
        }
    }
}
