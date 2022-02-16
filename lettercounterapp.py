#The Letter Counter App is a program that calculates the total number of occurences of an alphabet in an input

print("Welcome to the Letter Counter App\n")

# User inputs section
name = input("What is your name: ").title().strip()
print("Hello, " + name + "!")
print("I will count the number of times a specific letter appears in a message.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurences for: ")

# Standardize to lower case
message = message.lower()
letter = letter.lower()

# Get the count and display results
letter_count = message.count(letter)
print("\n" + name.title() + ", your message has " + str(letter_count) + " " + letter + "'s in it.")