// Bubble sort
  // Iterate each element of the array
  // look at the next element
  // if next element is smaller than current element, swap them
  // move to next element of the array
  // When there are no more swaps in an iteration, array is sorted

using System;

class MainClass 
{
  public static void Main (string[] args) 
  {
    int[] arr = new int[10] { 56, 1, 99, 67, 89, 23, 44, 12, 78, 34 };
    var sortedArray = BubbleSort(arr);

    foreach(var element in sortedArray)
    {
      Console.Write("{0} ", element);
    }
  }

  private static int[] BubbleSort(int[] numbers)
  {
    var swapped = true;

    while(swapped)
    {
      swapped = false;
      for (int i = 0; i < numbers.Length -1; i++)
      {
        var nextElementIndex = i + 1;
        if (numbers[i] > numbers[nextElementIndex])
        {
          var temp = numbers[i];
          numbers[i] = numbers[nextElementIndex];
          numbers[nextElementIndex] = temp;
          swapped = true;
        }
      }
    }

    return numbers;
  }
}