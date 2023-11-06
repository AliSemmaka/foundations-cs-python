# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:58:12 2023

@author: alise
"""

items = [["small water", 0.3], ["chocolate", 0.7], ["juice", 1], ["chips", 0.8], ["pepsi can", 0.9], ["ketchup", 2], ["coal", 3]]
chosenItems = []
couponRate = 0/100

def addItem():
    index = 0
    for i in items:
        print("product name: " + i[0] + ", price: " + str(i[1]) + ", press: " + str(index))
        index += 1

    print("choose a product:")
    choice = int(input())

    if choice >= len(items) or choice < 0:
        print("Invalid input")
        return

    quantity = int(input("Enter the quantity: "))
    chosenItems.append([items[choice][0], items[choice][1], quantity])

def checkTotal():
    totalPrice = 0
    for i in chosenItems:
        totalPrice += i[1] * i[2]
    print("The total of your bill is ", totalPrice - totalPrice * couponRate)

def addCoupon():
    print("choose a coupon rate between 1 and 100:")
    rate = int(input())
    global couponRate
    couponRate = rate / 100

def checkout():
    print("Items bought and their quantities:")
    for item in chosenItems:
        print(f"{item[0]} - Quantity: {item[2]}, Price: ${item[1]:.2f}")


    total_without_coupons = sum(item[1] * item[2] for item in chosenItems)
    total_after_coupons = total_without_coupons - total_without_coupons * couponRate
    print(f"Total of the order (without coupons): ${total_without_coupons:.2f}")
    print(f"Total of the coupons: ${total_without_coupons * couponRate:.2f}")
    print(f"Total to pay: ${total_after_coupons:.2f}")

def newOrder():
    choice = -99
    while choice != 4:
        print()
        print("Enter")
        print("1. To add an item")
        print("2. To check total")
        print("3. To add a coupon")
        print("4. To checkout")

        choice = int(input())

        if choice == 1:
            addItem()
        elif choice == 2:
            checkTotal()
        elif choice == 3:
            addCoupon()
        elif choice == 4:
            checkout()
        else:
            print("Invalid input")


def mainMenu():
    choice = -99  
    while choice != 2:
        print("Enter")
        print("1. To start a new order")
        print("2. To close the program")

        choice = int(input())

        if choice == 1:
            print("starting a new order...")
            newOrder()
        elif choice == 2:
            print("bye bye :)")
        else:
            print("Invalid input")

mainMenu()