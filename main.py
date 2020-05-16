from functions import * 

leak = {
    "Ana":["ana@email.com", "asdfg"], 
    "Bia":["bia@email.com", "zxcvb"], 
    "Carol":["carol@email.com", "qwert"]
    }

answer = "Y"

while answer == "Y":
    print("\nSelecting Menu Options:")
    print("Enter 1 for data registration.")
    print("Enter 2 for data list.")
    print("Enter 3 to update data.")
    print("Enter 4 to delete data.")
    print("Enter 5 to fetch an specific data.")
    print("Enter 6 to quit.")
   
    menu = int(input("Menu: "))
    if menu == 1:
        createItem(leak)
    elif menu == 2:
        readItem(leak)
    elif menu == 3:
        updateItem(leak)
    elif menu == 4:
        deleteItem(leak)
    elif menu == 5:
        fetchItem(leak)
    elif menu == 6:
        answer = "N"
    else:
        print("Invalid option, try again! ")
        answer = input("Do you wish to proceed? Y/N").upper()




