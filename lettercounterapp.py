#The Letter Counter App is a program that calculates the total number of occurences of an alphabet in an input

print("Welcome to the Letter Counter App\n")

name = input("What is your name: ")

print("Hello, " + name.title() + "!" + "\n")

print("I will count the number of times a specific letter appears in a message.")

message = input("\nPlease enter a message: ")

message = message.lower()

letter = input("Which letter would you like to count the occurences for: ")

letter = letter.lower()

letter_count = message.count(letter)

print(name.title() + ", your message has " + str(letter_count) + " " + letter + "'s" + " in it.")