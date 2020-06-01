// mergeSort(array)
// if array.length <= 1 then
// return array 
// left = new array
// right = new array 
// mid = left+ right/2
// mergeSort(left)
// mergeSort(right)
// merge(left, right)

using System;
using System.Collections.Generic;

class MainClass 
{
  public static void Main (string[] args) 
  {
    int[] arr = { 56, 1, 99, 67, 89, 23, 44, 12, 50 };
    //Console.Write("Unsorted Array: ");
    foreach(var element in arr)
    {
      //Console.Write("[{0}] ", element);
    }
    
    var sortedArray = MergeSort(arr);
    Console.WriteLine();
    //Console.Write("Sorted Array:   ");
    foreach(var element in sortedArray)
    {
      //Console.Write("[{0}] ", element);
    }
    Console.WriteLine();
  }

  private static int[] MergeSort(int[] array)
  {
    if (array.Length <= 1)
    {
      return array;
    }

    int middle = array.Length / 2;
    int[] left = new int[middle];
    int[] right = new int[array.Length - middle];
    
    for(int i = 0; i< middle; i++)
    {
      left[i] = array[i];
    }

    int x = 0;
    for(int i = middle; i< array.Length; i++)
    {
      right[x] = array[i];
      x++;
    }
    
    left = MergeSort(left);
    right = MergeSort(right);
    return Merge(left, right);
  }

  private static int[] Merge(int[] left, int[] right)
  {
    int[] result = new int[left.Length + right.Length];
    
    int leftIndex = 0;
    int rightIndex = 0;
    int resultIndex = 0;

    while(leftIndex < left.Length || rightIndex < right.Length)
    {
      if (leftIndex < left.Length && rightIndex < right.Length)
      {
        if(left[leftIndex] <= right[rightIndex])
        {
          result[resultIndex] = left[leftIndex];
          leftIndex++;
          resultIndex++;
        }
        else
        {
          result[resultIndex] = right[rightIndex];
          rightIndex++;
          resultIndex++;
        }
      }
      else if (leftIndex < left.Length)
      {
        result[resultIndex] = left[leftIndex];
        leftIndex++;
        resultIndex++;
      }
      else if (rightIndex < right.Length)
      {
        result[resultIndex] = right[rightIndex];
        rightIndex++;
        resultIndex++;
      }
    }

    return result;
  }
}