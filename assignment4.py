# -*1- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:37:11 2023

@author: alise
"""

cities=["Beirut", "Chtoura", "Zahle", "Saida", "Tripoli", "Byblos", "Dbaye", "Jounieh" ]
drivers={}
drivers["yousef"]=["dbaye", "jounieh"]
drivers["ali"]=["beirut", "chtoura", "zahle"]
drivers["tony"]=["chtoura"]
drivers["fadi"]=["byblos", "tripoli"]

def add_city():
    city_name= input("Write the name of the city: ")
    
    if city_name.strip() == "":
        print("City name can't be empty. Please enter a valid name.")
        return
    
    city_name_lower = city_name.lower()
    existing_cities_lower = [city.lower() for city in cities]

    if city_name_lower in existing_cities_lower:
        print(city_name + " is already in the list of cities.")
    else:
        cities.append(city_name)
        print(city_name + " added to the list of cities.")
    
    
    
def add_driver():
   driver_name= input("Write the name of the driver: ")
   #Checking if the user make empty input
   if driver_name.strip() == "":
       print("Driver name can't be empty. Please enter a valid name.")
       return
   
   driver_name_lower = driver_name.lower()
   existing_drivers_lower = [driver.lower() for driver in drivers.keys()]

   if driver_name_lower in existing_drivers_lower:
        print(driver_name + " is already in the list of drivers.")
   else:
        drivers[driver_name] = []  
        print(driver_name + " added to the list of drivers.")

   route = input("Enter the route for the driver (comma-separated cities): ").split(',')
    # Check if city exist
   for city in route:
       if city.lower() not in [drivers_city.lower() for drivers_city in drivers[driver_name]]:
           drivers[driver_name].append(city)
       else:
           continue
           
   print(f"{driver_name}'s route added successfully.")
   print(drivers)
   
   
    
def add_city_to_route():
    driver_name = input("Enter the name of the driver: ").lower()
    city_name = input("Enter the name of the city to add: ").lower()
    
    
    # Check if driver exist
    if driver_name.lower() not in [driver.lower() for driver in drivers.keys()]:
        print("driver does not exist")
        return
    
    # Check if city exist
    if city_name.lower() in [city.lower() for city in drivers[driver_name]]:
        print("city already exists.")
        return

    print(f"Options for adding {city_name} to {driver_name}'s route:")
    print("1. To add to the beginning of the route")
    print("-1. To add to the end of the route")
    print("#. To add to a specific index")

    index = input("Enter your option: ")
    
    if index == 1:
        drivers[driver_name].insert(0, city_name)
    elif index == -1:
        drivers[driver_name].append(city_name)
    elif index == '#':
        print(drivers[driver_name])
        chosen_index = int(input("Enter your index: "))
        if chosen_index > len(drivers[driver_name]) or chosen_index < 0:
            print("index not available")
        else:
            drivers[driver_name].insert(chosen_index, city_name)
            print(drivers[driver_name])
    else:
        print("not a valid option")

    print(f"{city_name} added to {driver_name}'s route.")
    
def remove_city_from_route():
    driver_name = input("Enter the name of the driver: ")
    city_name = input("Enter the name of the city to remove: ")
    
    if driver_name in drivers and city_name in drivers[driver_name]:
        drivers[driver_name].remove(city_name)
        print(drivers[driver_name])
        print(f"{city_name} removed from {driver_name}'s route.")
    else:
        print("Driver or city not found in the route.")
    
def check_deliverability():
    city_name = input("Enter the name of the city for delivery: ")
    #checking if the driver's name and city are available
    available_driver = []
    for driver in drivers.keys():
        if city_name.lower() in [city.lower() for city in drivers[driver]]:
            available_driver.append(driver)
        else:
             continue
    if len(available_driver) > 0:
        print(f"Drivers delivering to {city_name}: {', '.join(available_driver)}")
    else:
         print("no drivers available.")
    
def mainMenu(): 
 choice = -99  
 while choice != 6:
    print("Enter: ")
    print("0. To Exit")
    print("1. To add a city")
    print("2. To add a driver")
    print("3. To add a city to the route of a driver")
    print("4. Remove a city from a driver’s route")
    print("5. To check the deliverability of a package")
    
    choice = int(input("Choice: "))
    
    if choice==0:
        break
    elif choice==1:
        add_city()
    elif choice==2:
        add_driver()
    elif choice==3:
        add_city_to_route()
    elif choice==4:
        remove_city_from_route()
    elif choice==5:
        check_deliverability()
    else:
        print("Invalid choice, please insert a valid option.")
        
    
mainMenu()
    