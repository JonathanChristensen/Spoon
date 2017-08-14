#This script presents a small user managment menu.

from sortedcontainers import SortedDict


def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a User')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
# switeched from int to text to allow a retry if a user enters a non-integer
while menu_choice is not ["5","4","3","2","1"] :
    # get menu choice from user
    menu_choice = (input("Type in a number (1-5): "))

    # view current entries
    if menu_choice == "1":
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == "2":
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username

    # remove an entry
    elif menu_choice == "3":
        print("Remove User")
        name = input("Name: ")
        #changed from if to while to allow for exeption handling
        while name not in usernames:
            name = input("I'm sorry, Dave, but I'm afraid I just can't delete that. Please try again ")
        if name in usernames:
          del usernames[name]
          print("{} has been removed".format(name))
          break


    # view user name
    elif menu_choice == "4":
        print("Lookup User")
        name = input("Name: ")
        # changed from if to while to allow for exeption handling
        while name not in usernames:
          name = input("I'm afraid there is no user by that name. Please try again. ")
        if name in usernames:
           print(usernames[name])
           break

    # is user enters something strange, show them the menu
    elif menu_choice is not "5":
        print_menu()
