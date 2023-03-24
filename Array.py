# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 01:13:44 2023

@author: Noha
"""

'''
The function which implements QuickSort.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''
import math 
 
def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot


	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
        
           
    #-----------------------------------------------------------------------
 
   # selectionSort 

def selectionSort(array, size):


    for ind in range(size):

         min_index = ind
 

         for j in range(ind + 1, size):

             # select the minimum element in every iteration

             if array[j] < array[min_index]:

                 min_index = j

          # swapping the elements to sort the array

         (array[ind], array[min_index]) = (array[min_index], array[ind])

        # Number of elements: 10,000 

#==============================================================================
#randomized finding medain  
def FindingMidean(array,n):
     if( (n%2) == 0 ):
            m1 = math.floor((n)/2)
            m2 = math.floor((n-1)/2)
            median=((array[m1] + array[m2])/2)
     else:
            median=(array[math.floor((n)/2)])
        # Printing result
     print("\n Median of Array is : " , median)   
       
#==============================================================================

#so the complexity we may get is: 
#spliting + select pivot + partitioning 
# O(n/5) + O(7n/10) + O(n)  = O(n)
