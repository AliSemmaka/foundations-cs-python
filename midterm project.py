# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 00:54:18 2023

@author: alise
"""

#title
#URL
#which tab is open
# tabs=[]
# tab={title:"google", url:"https://www.bing.com", tabs=[]}


def mainMenu(): 
 choice = -99  
 while choice != 9:
    print("Enter: ")
    print("1. To open tab")
    print("2. To close tab")
    print("3. To switch tab")
    print("4. To display all tabs")
    print("5. To open nested tabs")
    print("6. To sort all tabs")
    print("7. To save tabs")
    print("8. To import tabs")
    print("9. To exit")



    
    choice = int(input("Choice: "))
    
    
    if choice==1:
        open_tab()
    elif choice==2:
        close_tab()
    elif choice==3:
        switch_tab()
    elif choice==4:
        display_all_tabs()
    elif choice==5:
        open_nested_tabs()
    elif choice==6:
        sort_all_tabs()
    elif choice==7:
        save_tabs()
    elif choice==8:
        import_tabs()
    elif choice==9:
        break
    else:
        print("Invalid choice, please insert a valid option.")
        
    
mainMenu()


