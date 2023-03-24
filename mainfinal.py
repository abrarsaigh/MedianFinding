# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:24:17 2023

@author: Noha
"""
import time
import linked
import Array
import Heap
"******************************************************************************"
"---------------------- readData of LinkedList----------------------"
def readData(): 
  with open("bb.txt", 'r') as f:
      llist = linked.LinkedList()
      for number  in f:
         llist.addNode(int(number))
  return llist

llist = readData()
N = llist.head
while (N.next != None):
   N = N.next
"---------------------- readData of Array----------------------"
def readlist(): #opening file
    myFile = open("bb.txt","r")
    numbers = []
    for number in myFile:
        numbers.append(int(number))  
    myFile.close()
    return numbers

numb = readlist()
size = len(numb)
"******************************************************************************"
"----------------------Choice-----------------------"
def Choice():
    print("\n------------------------")
    print('Choose the algorithm you want\n' +
          '1- Quick sort algorithm using linked list\n'+'2- Quick sort algorithm using Array\n'+'3- Quick sort algorithm using Heap\n'+
          '4- Selection sort algorithm using linked list\n'+'5- Selection sort algorithm using Array\n'+'6-Selection sort algorithm using Heap\n' +
          ' to exit print 0')
    print("------------------------")
Choice()
option_1 = int(input('Enter your choice: '))


"---------------------------------------------"

while option_1 != 0:
    #check1 what choice was entered and act accordingly
    if option_1 == 1:
             start_time=time.perf_counter() #START
             linked.LinkedList().QuickSort(llist.head,N) #call QuickSort function of linked list
             llist.printMedian()#call medianfinding function Of linked list
             print("\n* Time taken to finding median With Quick Sort using linked list is: ",time.perf_counter() - start_time,"sec *")
             
             Choice()
             option_1 = int(input('Enter your choice: '))
            
    elif option_1 == 2:
            start_time=time.perf_counter()
            Array.quickSort(numb,0,(size-1)) #call QuickSort function of Array
            Array.FindingMidean(numb,size)#call medianfinding function of Array
            print("* Time taken to finding median With Quick Sort using Array is: ",time.perf_counter() - start_time,"sec *")
            
            Choice()
            option_1 = int(input('Enter your choice: '))
    elif option_1 == 3:
             start_time=time.perf_counter() 
             x=Heap.quickSort(numb)
             print("Median of Heap is",x)
             print("\n* Time taken to finding median With Quick Sort using Heap is: ",time.perf_counter() - start_time,"sec *")
             
              
             Choice()
             option_1 = int(input('Enter your choice: '))

        
    elif option_1 == 4:
            start_time=time.perf_counter() 
            linked.selectionSort(llist.head) 
            llist.printMedian()
            print("* Time taken to finding median With Selection sort using linked list is: ",time.perf_counter() - start_time,"sec *")

            Choice()
            option_1 = int(input('Enter your choice: '))
            
    elif option_1 == 5:
            start_time=time.perf_counter() 
            Array.selectionSort(numb, size) #call selectionSort function of Array
            Array.FindingMidean(numb,size) #call medianfinding function of Array
            print("\n* Time taken to finding median With Selection sort using Array is: ",time.perf_counter() - start_time,"sec *")
             
            Choice()
            option_1 = int(input('Enter your choice: '))
            
    elif option_1 == 6:
            start_time=time.perf_counter() 
            Heap.heapSort(numb) #call selectionSort function of Heap
            print('Median of Heap by using selection sort: ', Heap.median_finding(numb))#call medianfinding function of Heap
            print("\n* Time taken to finding median With Selection sort using Heap is: ",time.perf_counter() - start_time,"sec *")
             
            Choice()
            option_1 = int(input('Enter your choice: '))
            
            
    else:
        print ('** Wrong choice. please enter a number between 0 and 6 **')
        Choice()
        option_1 = int(input('Enter your choice: '))