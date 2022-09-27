import re   
user_input = input("Add or remove or search: ").lower()

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

if user_input == "search":
    print("________________________________________")
    print("                                         ")
    print("You are in user search section")
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
            print(f"Found user {to_remove} in membership file in line {count}")
        count += 1    
    else:
        print("couldnt find the user")