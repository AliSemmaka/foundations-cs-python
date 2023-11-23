# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 22:42:04 2023

@author: alise
"""
#assignment 5 part 1

# Capital letters are smaller than smaller letters
# Alphabetical order
def compare(str1, str2):
    # find the smaller string
    smallerString = str2
    if len(str1) < len(str2):
        smallerString = str1
    
    # Check if str1 is smaller than string two
    for i in range(len(smallerString)):
        if str1[i].lower() == str2[i].lower():
            if str1[i] > str2[i]: 
                return True
            elif str1[i] < str2[i]:
                return False
        elif str1[i].lower() < str2[i].lower():
            return True
        elif str1[i].lower() > str2[i].lower():
            return False
        
    # Remaining logic is:
    # if str1 is bigger than str2 in length then false
    # if str1 equals to str2 then it does not matter (we are returning true)
    # if str1 is smaller than str2 in length return true
    if len(str1) > len(str2):
        return False
    else: 
        return True
    
       

def selectionSort(list1): #O(n^2)
  border=0
  while border <len(list1)-1: #O(n), n being the length of the list
    minIndex=border 
    for i in range(border+1, len(list1)):
      # Compare function checks if list1[i] is smaller than list1[minIndex]
      if compare(list1[i], list1[minIndex]): #O(1), is the line that specifies the order
        minIndex=i
    #swap the two elements
    temp=list1[border] #O(1)
    list1[border]=list1[minIndex]
    list1[minIndex]=temp

    border=border+1
  print(list1)
  
selectionSort(['aA', 'b', 'BD', 'Bc','D', 'B', 'B', 'A'])



\

    