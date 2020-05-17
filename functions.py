#
def createItem(leak):
    answer = "Y"
    while answer == "Y":
        key = input("Set key: ")
        leak[key] = [
            input("Set e-mail: "),
            input("Set password: ")
        ]
        answer = input("Do you wish to proceed with another registration? Y/N").upper()

#
def readItem(leak):
    for key, value in leak.items():
        print("\nKey........", key)
        print("E-mail.....", value[0])
        print("Password...", value[1])

#
def updateItem(leak):
    key = input("Which item do you wish to update?")

    if key in leak.keys(): 
        value = leak.get(key)
        value[0] = input("Set new e-mail: ")
        value[1] = input("Set new password: ")
        leak[key] = [value[0], value[1]]
        
        print(key + " has been successfully updated!")
        print("Key.........", key)
        print("E-mail......", value[0])
        print("Password....", value[1])
    else:
        print("Item not found. Try again!")

# 
def deleteItem(leak):
    key = input("Which item do you wish to delete?")
    if key in leak.keys(): 
        del leak[key]
        print(key + " has been successfully deleted.")
    else:
        print("Item not found. Try again!")

# 
def fetchItem(leak):
    key = input("Which item do you wish to fetch?")
    if key in leak.keys(): 
        value = leak.get(key)
        print("Key.........", key)
        print("E-mail......", value[0])
        print("Password....", value[1])
    else:
        print("Item not found. Try again!")




     

    # if key != None:
    #     value = key.values()
    #     value[0] = input("Set new e-mail: ")
    #     value[1] = input("Set new password: ")
    #     leak[key] = [value[0], value[1]]
    # else: 
    #     print("No key found. Try again.")

    # print("${key} has been updated successfully")
    # print("Key.........", key)
    # print("E-mail......", value[0])
    # print("Password....", value[1])

#

