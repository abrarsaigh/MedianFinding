# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:23:26 2023

@author: Noha
"""
import heapq


#==============================================================================

# quicksort
def quickSort(arr):
    min_heap = []
    max_heap = []

    for i in range(len(arr)):
        if i < len(arr) // 2:
            heapq.heappush(max_heap, -arr[i])
        else:
            heapq.heappush(min_heap, arr[i])

        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    # median_finding
    if len(min_heap) == len(max_heap):
        median = (min_heap[0] - max_heap[0]) / 2
    else:
        median = min_heap[0]

    return median
#==============================================================================
# Function to find the median of stream of data
# Python code to find the median of a given array 
# using heapify data structure

def heapifyy(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
  
 # See if left child of root exists and is
 # greater than root
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
 # See if right child of root exists and is
 # greater than root
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
 # Change root, if needed
  
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
  
  # Heapify the root.
  
        heapifyy(arr, n, largest) 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
  
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
  
    for i in range(n // 2 - 1, -1, -1):
        heapifyy(arr, n, i)
  
 # One by one extract elements
  
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapifyy(arr, i, 0)
#==============================================================================

# medain finding  
def median_finding(dataset):
     max_heap = [] # Create an empty max-heap
     for element in dataset:
         heapq.heappush(max_heap, -element) # Insert elements in max heap

     for i in range(len(dataset)//2):
         heapq.heappop(max_heap) # Extract max element from heap
         

     median = -heapq.heappop(max_heap) # Extract the final max element, which is the median
     return median


 
# Driver code to test above

# heapSort(arr)
# n = len(arr)


# print(streamMed(myArray1,n))
# print(time.process_time())