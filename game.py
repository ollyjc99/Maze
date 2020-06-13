import os, sys, time
from items import *
from player import *
from gameparser import *
from map import rooms

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def list_of_items(items):

    s = ""
    for i in range(len(items)):
        s = s + items[i]["name"] + ", "
    return s[:-2]
    if s == 0:
        return None

def print_room_items(room):
	if room["items"] != []:
		print("There is " + list_of_items(room["items"]) + " here")

def print_inventory_items(inventory):
	if inventory != []:
		for item in inventory:
			print("DROP "+item["id"])

	print("\nYou have " + list_of_items(inventory),"\n")

def print_room(room):
    print("\n"+room["name"].upper()+"\n")
    print(room["description"]+"\n")

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):

    print("GO "+ direction.upper()+" to "+ leads_to + ".")

def print_menu(exits, room_items, inv_items):

    print_room_items(current_room)
    print("\nYou can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    print()
    if current_room["items"] != []:
        for item in current_room["items"]:
            print ("TAKE "+item["id"])
        print()

    print_inventory_items(inventory)
    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    choice = False
    for exit in exits:
        if exit == chosen_exit:
            choice = True
    return choice

def is_pickup_valid(inventory, item):
    return False

def execute_go(direction):
	global current_room
	if is_valid_exit(current_room["exits"], direction) == True:
		current_room = rooms[current_room["exits"][direction]]
	else:
		print("You cannot go there")

def execute_take(item_id):
    take_item = False
    for i in range(len(current_room["items"])):
        if current_room["items"][i]["id"] == item_id:
            take_item = True

            inventory.append(current_room["items"][i])
            current_room["items"].remove(current_room["items"][i])

            print(item_id, " added to inventory")

            return True

    if take_item == False:
        print("You cannot take that")
        return False

def execute_drop(item_id):
    drop_item = False
    for i in range(len(inventory)):
        if item_id == inventory[i]["id"]:
            drop_item = True

            current_room["items"].append(inventory[i])
            inventory.remove(inventory[i])
            print(item_id + " dropped")
            return True

    if drop_item == False:
        print("You cannot drop that")
        return False

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)

    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)
    return normalised_user_input

def move(exits, direction):

    return rooms[exits[direction]]

def main():
    while True:
        time.sleep(1.5)
        clear()
        print_room(current_room)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

if __name__ == "__main__":
    main()
