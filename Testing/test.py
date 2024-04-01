class Room:

    def __init__(self, description, north, south, west, east):

        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east


def main():

    room_list = []

    room = Room("\nYou are now in the living room. There are doors to your north, west and south. ", 3, 2, 1, None)
    room_list.append(room)

    room = Room("\nYou are now in the kitchen. There is a door to your east. ", None, None, None, 0)
    room_list.append(room)

    room = Room("\nYou are now in the Guest bedroom. There is a door to your north. ", 0, None, None, None)
    room_list.append(room)

    room = Room("\nYou are now in the Master room. There are doors to your south and east. ", None, 0, None, 4)
    room_list.append(room)

    room = Room("\nYou are now in the Bathroom. There is a door to your west. ", None, None, 3, None)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:

        print(room_list[current_room].description)

        user_input = input("What would you like to do? ")

        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("\nYou can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("\nYou can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("\nYou can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("\nYou can't go that way.")
            else:
                current_room = next_room
                print(room_list[current_room].description)

        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("\nGoodbye!! Thank you for playing.")
            done = True

        else:
            print("\nI am sorry, I can't understand that. Please Try Again. ")


main()
