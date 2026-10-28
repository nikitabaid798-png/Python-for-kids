# Program to create a personalized congratulation message

# Taking input from the user
name = input("Enter your name: ")
achievement = input("What have you achieved? ")
age = input("Enter your age: ")

# Typecasting: converting age from string to integer
age = int(age)

# Storing different data types in variables
message_count = 1       # Integer
success = True          # Boolean

# String operations: concatenation and repetition
greeting = "Congratulations, " + name + "!"
celebration = "Hip Hip Hurray! " * 2

# Printing the congratulation message
print("\n" + "=" * 35)
print(greeting)
print("You have successfully achieved: " + achievement + ".")
print("You are now " + str(age) + " years old.")
print(celebration)
print("Message number:", message_count)
print("Success:", success)
print("=" * 35)

# Displaying a final encouraging message
print("Keep up the great work, " + name + "!")
