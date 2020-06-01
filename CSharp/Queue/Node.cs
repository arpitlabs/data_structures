public class Node
{
  public object Data {get; private set;}
  public Node Next {get;set;}
  public Node(object data)
  {
    this.Data = data;
  }
}

public class Queue
{
  public Node First {get; set;}
  public Node Last {get;set;}

  public void Add(object item)
  {
    var node = new Node(item);

    if(this.Last == null)
    {
      this.First = node;
      this.Last = node;
    }
    else
    {
      this.Last.Next = node;
      this.Last = node;
    }
  }

  public Node Remove()
  {
    // remove from begining
    if (this.First == null)
    {
      return null;
    }

    var removedNode = this.First;
    this.First = this.First.Next;
    return removedNode;
  }

}