# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:15:18 2023

@author: alise
"""


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Delete the node at a given position
    def deleteNodeAtGivenPosition(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("Index is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(" %d " % (temp.data), end=" ")
            temp = temp.next


# Assuming you have a Node class defined somewhere in your code
# For example:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List: ")
llist.printList()

user_input = int(input("\nEnter the position of the node you want to delete: "))
llist.deleteNodeAtGivenPosition(user_input)
print("\nLinked List after Deletion at position ", user_input)
llist.printList()
