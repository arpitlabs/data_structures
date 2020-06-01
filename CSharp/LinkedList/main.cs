using System;

class MainClass {
  public static void Main (string[] args) {

    var node2 = new Node("test 2");
    var node1 = new Node("test 1");
    node1.NextNode = node2;
    var linkedList = new LinkedList(node1);



    Console.WriteLine (linkedList.Read(1));
    Console.WriteLine (linkedList.IndexOf("test 1"));

    Console.WriteLine (linkedList.Length);
    linkedList.InsertAt(2, "test 3");
    Console.WriteLine (linkedList.Read(2));

  }
}

class Node
{
  public Node(object data)
  {
    this.Data = data;
  }

  public object Data {get;private set;}
  public Node NextNode {get; set;}
}

class LinkedList
{
  private  Node firstNode;
  private int length;

  public LinkedList(Node firstNode)
  {
    this.firstNode = firstNode;
  }

  public object Read(int index)
  {
    if(index >= this.Length)
    {
      throw new InvalidOperationException("Index out of range");
    }

    var currentNode = this.firstNode;
    var currentIndex = 0;

    while (currentIndex < index)
    {
      currentNode = currentNode.NextNode;
      currentIndex ++;
    }
    return currentNode.Data;
  }

  public int IndexOf(object data)
  {
    var currentNode = this.firstNode;
    var currentIndex = 0;

    while(currentNode != null)
    { 
      if(currentNode.Data == data)
      {
        return currentIndex;
      }

      currentNode = currentNode.NextNode;
      currentIndex ++;
    }

    return -1;
  }

  public void InsertAt(int index, object data)
  {
    if(index > this.Length)
    {
      throw new InvalidOperationException("Index out of range");
    }

    var newNode = new Node(data);
    
    if(index == 0)
    {
      this.firstNode = newNode;
      return;
    }

    var currentNode = this.firstNode;
    var currentIndex = 0;

    while(currentIndex < index - 1)
    {
      currentNode = currentNode.NextNode;
      currentIndex++;
    }

    newNode.NextNode = currentNode.NextNode;
    currentNode.NextNode = newNode;

  }

  public int Length 
  {
    get
    {
      var currentNode = this.firstNode;
      var currentIndex = 0;

      while(currentNode.NextNode != null)
      {
         currentNode = currentNode.NextNode;
          currentIndex++;
      }

      return currentIndex + 1;
    }
  }
}
