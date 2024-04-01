import random

# defining main function
def main():

# Introduction to the game

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your \ndesert trek and out run the natives.\n")

# Vital Stats

    done = False
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    drinks_left = 3

# Game options

    while not done:

        print("A. Drink water from your bottle.")
        print("B. Go in moderate speed.")
        print("C. Go in full speed.")
        print("D. Take rest for the night.")
        print("E. Status Check.")
        print("Q. Quit game.\n")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == 'Q':
            print("Game Over.")
            break

        elif user_choice.upper() == 'E':
            print("\nMiles Covered:" + str(miles_travelled))
            print("Drinks Left:" + str(drinks_left))
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.")
            print("Camel tiredness:" + str(camel_tiredness))
            print("Thirst :" + str(thirst))

        elif user_choice.upper() == 'D':
            print("\nYou took a rest for the night.")
            print("Your camel is happy.")
            natives_distance = natives_distance + random.randrange(7,14)
            camel_tiredness = 0
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")


        elif user_choice.upper() == 'C':
            thirst = thirst + 1
            print("\nYour camel ran like a train.")
            miles_travelled = miles_travelled + random.randrange(10,20)
            camel_tiredness = camel_tiredness + random.randrange(1,3)
            natives_distance = natives_distance + random.randrange(7, 14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

            if random.randint(1,20) == 1:
                print("lucky you! You found an Oasis.You took a rest, clenched your thirst and refilled your bottle.\n")
                camel_tiredness = 0
                drinks_left = 3
                thirst = 0

            else:
                pass


        elif user_choice.upper() == 'B':

            thirst = thirst + 1
            print("\nYour camel ran calmly.")
            miles_travelled = miles_travelled + random.randrange(5,12)
            camel_tiredness = camel_tiredness + 1
            natives_distance = natives_distance + random.randrange(7, 14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

            if random.randint(1, 20) == 1:
                print("lucky you! You found an Oasis.\n")
                camel_tiredness = 0
                drinks_left = 3
                thirst = 0

            else:
                pass


        elif user_choice.upper() == "A":
            if drinks_left > 0:
                thirst = 0
                drinks_left = drinks_left - 1
                print("\nThat was good.\n")
            else:
                print("\nYou are out of drinks.\n")

# Consequences of chosen options

        if thirst > 6:
            print("Your camel died of thirst. Oops!\n")
            done = True
            break
        elif thirst > 4:
            print("Your camel is thirsty. Drink water!\n")

        if camel_tiredness > 8:
            print("Your camel died of tiredness.\n")
            done = True
            break
        elif camel_tiredness > 5:
            print("Take rest. Your camel is getting tired.\n")

        if natives_distance >= miles_travelled:
            print("You got caught. You lost.\n")
            done = True
            break
        elif miles_travelled - natives_distance <= 15:
            print("Hurry! The natives are getting closer.\n")

        if miles_travelled >= 200:
            print("Congratulations! You made it.\n")
            done = True
            break


main()