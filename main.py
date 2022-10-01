import re
import time
current_time = time.ctime()

user_input = input("Add or remove or search or change : ").lower()

if user_input == "add":
    print("________________________________________")
    print("                                         ")
    print("You are in user add section")
    print("________________________________________")
    print("                                         ")
    to_add = input("Enter the name u want to add in membership : ")
    print(f"Added {to_add} to membership")
    with open("membership.txt","a") as f:
        f.write(f"{to_add}\n")
    with open("All_logs.txt","a") as lg:
        current_time = time.ctime()
        lg.write(f"Added {to_add} in time {current_time} from program main.py \n")
        lg.write("-------------------------------------------------------------------------------------------------------------------------- \n")


if user_input == "remove":
    print("________________________________________")
    print("                                         ")
    print("You are in user remove section")
    print("________________________________________")
    print("                                         ")
    to_remove = input("Enter the name u want to remove in membership : ")
    fh = open("membership.txt", "r+")
    s = " "
    count = 1
    while s:
        s = fh.readline()
        L = s.split()
        if to_remove in L:
            string = open("membership.txt").read()
            new_str = re.sub(to_remove,'',string)
            open("membership.txt","w").write(new_str)
        count += 1
    print("Removed user if it was present")

    with open("All_logs.txt","a") as lg:
        current_time = time.ctime()
        lg.write(f"removed {to_remove} in time {current_time} from program main.py \n")
        lg.write("-------------------------------------------------------------------------------------------------------------------------- \n")
        
if user_input == "search":
    is_yes = ""
    foundin = 0
    print("________________________________________")
    print("                                         ")
    print("You are in user search section")
    print("________________________________________")
    print("                                         ")
    to_remove = input("Enter the name u want to searc in membership : ")
    fh = open("membership.txt", "r+")
    s = " "
    count = 1
    while s:
        s = fh.readline()
        L = s.split()
        if to_remove in L:
            print(f"Found user {to_remove} in membership file in line {count}")
            foundin +=1
        count += 1
    if foundin == 0:
        print("Couldnt find the user")
    with open("All_logs.txt","a") as lg:
        if foundin > 0:
            is_yes = "Found the user"
        if foundin == 0:
            is_yes == "Could not find the user"
        current_time = time.ctime()
        lg.write(f"searched {to_remove} in time {current_time} from program main.py and the result was {is_yes} \n")
        lg.write("-------------------------------------------------------------------------------------------------------------------------- \n")

if user_input == "change":
    print("________________________________________")
    print("                                         ")
    print("You are in user change section")
    print("________________________________________")
    print("                                         ")
    acctuall_name = input("Enter the name u want to change in membership : ")
    to_change = input("Enter the name u want to change of the user : ")
    fh = open("membership.txt", "r+")
    s = " "
    count = 1
    while s:
        s = fh.readline()
        L = s.split()
        if acctuall_name in L:
            string = open("membership.txt").read()
            new_str = re.sub(acctuall_name,to_change,string)
            open("membership.txt","w").write(new_str)
        count += 1
    print("Changed user if it was present")

    with open("All_logs.txt","a") as lg:
        current_time = time.ctime()
        lg.write(f"changed {acctuall_name} to {to_change} in time {current_time} from program main.py \n")
        lg.write("-------------------------------------------------------------------------------------------------------------------------- \n")
        
