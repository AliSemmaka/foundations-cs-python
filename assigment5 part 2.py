# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:41:33 2023

@author: alise
"""

#assignment 5 part 2

def mergeSort(list1,start,end): #O(n log n)
  # base case
  if start==end: 
    return
  mid=(start+end)//2 
  mergeSort(list1,start,mid) # dividing the list
  mergeSort(list1,mid+1,end)
  merge(list1,start,mid,end) # I am passing the division of the list

def merge(list1,start,mid,end): # to merge the two sublists into a sorted one, O(n), n being the length of the list
  new_list=[]
  ind1=start 
  ind2=mid+1 

  while ind1<=mid and ind2<=end: 
    if list1[ind1]>list1[ind2]:
      new_list.append(list1[ind1])
      ind1+=1
    else: # the element in my second sublist is smaller
      new_list.append(list1[ind2])
      ind2+=1
  # this means that the elements of sublist 1 OR sublist 2 are complete

  while ind1<=mid:
    new_list.append(list1[ind1])
    ind1+=1
    
  while ind2<=end: 
    new_list.append(list1[ind2])
    ind2+=1

  list1[start:end+1]=new_list


list1=[47,43,1,2,4,3,12,5,6,3,2,105,90,-2]
mergeSort(list1,0,len(list1)-1)
print(list1)