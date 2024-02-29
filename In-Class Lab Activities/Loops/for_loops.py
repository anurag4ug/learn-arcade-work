#Print 'Hi' 10 times

#for i in range(10):
#   print("Hi!")

#Print 'Hello' 5 Times and 'There' once

#for i in range(5):
#    print('Hello')
#print("There")

#Print 'Hello' and 'There' 5 times on different lines

#for i in range(5):
#    print('Hello')
#    print('There')

#print 0 to 9

#for i in range(10):
#   print(i)

#two ways to print 1 to 10

#for i in range(10):
#   print(i+1)

#for i in range(1,11):
#   print(i)

#two ways to print even numbers 2 to 10

#for i in range(2,12,2):
#    print(i)

#for i in range(5):
#    print((i+1)*2)

#Count down from 10 down to 1(not zero)

#for i in range(10,0,-1):
#    print(i)

#print numbers out of a list

#for i in(2,4,7,1,6,4,11):
#    print(i)

#for while loop

# print 0 to 9

#i = 0
#while i < 10:
#    print(i)
#    i=i+1

#multiples of 2
#i = 1
#while i<=2**32:
#    print(i)
#    i*=2

#until the user says no

keep_going = 'yes'

while keep_going == 'yes':
    a = input("would you like to try again?").lower()
    if a == "no":
        keep_going = a
    else:
        print("Ok, let's keep going" )