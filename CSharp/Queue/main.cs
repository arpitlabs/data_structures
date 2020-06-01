using System;

class MainClass {
  public static void Main (string[] args) {

    var queue = new Queue();
    queue.Add(3);
    queue.Add(2);
    queue.Add(1);

    Console.WriteLine(queue.Remove().Data);
    Console.WriteLine(queue.Remove().Data);
    Console.WriteLine(queue.Remove().Data);
    

    Console.ReadLine();
  }
}