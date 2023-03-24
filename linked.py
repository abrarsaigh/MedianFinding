# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:08:19 2023

@author: Noha
"""
#-----------------------------------------------
# Node class
class Node:
    def __init__(self, val): # Function to initialize the node objec
        self.data = val # Assign data
        self.next = None # Initialize next as null
#------------------------------------------------  
# Linked List class
class LinkedList:
   
    def __init__(self):# to initialize the Linked List object
        self.head = None
  
    def addNode(self, data): # Function to insert a new node
        if (self.head == None):
            self.head = Node(data)
            return
  
        curr = self.head
        while (curr.next != None):
            curr = curr.next
  
        newNode = Node(data)
        curr.next = newNode
        # Function to print the list  

    def printList(self, n):
         while (n != None):
             print(n.data, end=" ")
             n = n.next

#==============================================================================
    # Function to get the median
    # of the linked list   
    def printMedian(self):
    
       slow_ptr = self.head
       fast_ptr = self.head
        
       while (fast_ptr != None and
              fast_ptr.next != None):
           fast_ptr = fast_ptr.next.next
            
           # Previous of slow_ptr
           pre_of_slow = slow_ptr
           slow_ptr = slow_ptr.next
       # If the below condition is true
       # linked list contain odd Node
       # simply return middle element   
       if (fast_ptr):
           print("\n Median of LinkedList is :", (slow_ptr.data))
            
       # Else linked list contain even element
       else:
           print("\n Median of LinkedList is :", (slow_ptr.data +pre_of_slow.data) / 2)

#==============================================================================
  
    ''' takes first and last node,but do not
    break any links in the whole linked list'''
  
    def partitionLast(self, start, end):
        if (start == end or start == None or end == None):
            return start
  
        pivot_prev = start
        curr = start
        pivot = end.data
        
  
        '''iterate till one before the end, 
        no need to iterate till the end because end is pivot'''
  
        while (start != end):
            if (start.data < pivot):
  
                # keep tracks of last modified item
                pivot_prev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next
  
        '''swap the position of curr i.e. 
        next suitable index and pivot'''
  
        temp = curr.data
        curr.data = pivot
        end.data = temp
  
        ''' return one previous to current because 
        current is now pointing to pivot '''
        return pivot_prev
#==============================================================================
    def QuickSort(self, start,end):
        if(start == None or start == end or start == end.next):
            return
  
        # split list and partition recurse
        pivot_prev = self.partitionLast(start, end)
        self.QuickSort(start, pivot_prev)
  
        '''
        if pivot is picked and moved to the start,
        that means start and pivot is same 
        so pick from next of pivot
        '''
        if(pivot_prev != None and pivot_prev == start):
            self.QuickSort(pivot_prev.next, end)
  
        # if pivot is in between of the list,start from next of pivot,
        # since we have pivot_prev, so we move two nodes
        elif (pivot_prev != None and pivot_prev.next != None):
            self.QuickSort(pivot_prev.next.next, end)
            
    "-------------------------------------------------"
# Function to sort a linked list  
# using selection sort algorithm 
# by swapping the next pointers  

def selectionSort(head):  
        a = b = head  
        # While b is not the last node  
        while b.next:  
            c = d = b.next
            # While d is pointing to a valid node  
            while d:   
                if b.data > d.data:  
                    # If d appears immediately after b  
                    if b.next == d:  
                        # Case 1: b is the head  
                        # of the linked list  
                        if b == head:  
                            # Move d before b  
                            b.next = d.next
                            d.next = b  
                            # Swap b and d pointers  
                            b, d = d, b  
                            c = d  
                            # Update the head  
                            head = b  
                            # Skip to the next element  
                            # as it is already in order  
                            d = d.next
                        # Case 2: b is not the head  
                        # of the linked list  
                        else:  
                            # Move d before b  
                            b.next = d.next
                            d.next = b  
                            a.next = d  
                            # Swap b and d pointers  
                            b, d = d, b  
                            c = d  
                            # Skip to the next element  
                            # as it is already in order  
                            d = d.next
                        # If b and d have some non-zero  
                        # number of nodes in between them  
                    else: 
                         # Case 3: b is the head  
                         # of the linked list  
                         if b == head:  
                             # Swap b.next and d.next  
                             r = b.next
                             b.next = d.next
                             d.next = r  
                             c.next = b  
                             # Swap b and d pointers  
                             b, d = d, b  
                             c = d  
                             # Skip to the next element  
                             # as it is already in order  
                             d = d.next
                             # Update the head  
                             head = b  
                         # Case 4: b is not the head 
                         # of the linked list  
                         else:  
                             # Swap b.next and d.next  
                             r = b.next
                             b.next = d.next
                             d.next = r  
                             c.next = b  
                             a.next = d  
                             # Swap b and d pointers 
                             b, d = d, b  
                             c = d
                             # Skip to the next element  
                             # as it is already in order
                             d = d.next
                else: 
                   # Update c and skip to the next element
                   # as it is already in order 
                   c = d  
                   d = d.next
            a = b  
            b = b.next
        return head  


  
# Driver Code  

