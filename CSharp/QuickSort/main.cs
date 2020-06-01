using System;

class MainClass 
{
  public static void Main (string[] args) 
  {
     int[] arr = new int[10] { 56, 1, 99, 67, 89, 23, 44, 12, 78, 34 };

      var copy = arr.CreateCopy();
      QuickSort(copy, 0, copy.Length - 1);

      foreach(var element in sortedArray)
      {
        Console.Write("{0} ", element);
      }
  }

  private static void QuickSort(int[] array, int left, int right)
  {
    if(left >= right)
    {
      return;
    }

    var pivot = array[new Random().Next(left, right)];
    var partition = Partition(array, left, right, pivot);

    QuickSort(array, left, partition - 1);
    QuickSort(array, partition, right);
  }

  private static int Partition(int[] array, int leftStart, int rightEnd, int pivot)
  {
    int left = leftStart;
    int right = rightEnd;

    while(array[left] < pivot)
    {
      left++;
    }

    while(array[right] > pivot)
    {
      right--;
    }

    if(left <= right)
    {
      var temp = array[left];
      array[left] = array[right];
      array[right] = temp;
      left++;
      right--;
      
    }

    return left;


  }
}