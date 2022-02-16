#The Letter Counter App is a program that calculates the total number of occurences of an alphabet in an input

print("Welcome to the Letter Counter App\n")

name = input("What is your name: ")
print("Hello, " + name + "!" + "\n")

print("I will count the number of times a specific letter appears in a message.\n")

message = input("Please enter a message: ")

letter = input("Which letter would you like to count the occurences for: ")

letter_count = message.lower().count(letter)

print("There are " + str(letter_count) + " '" +letter + "' " +"in " + name + ".")