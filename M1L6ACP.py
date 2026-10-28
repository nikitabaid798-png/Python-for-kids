# Program to check whether a character is an alphabet

# Take a character as input from the user
char = input("Enter a character: ")

# Check if the character is an alphabet
if char.isalpha() and len(char) == 1:
    print("It is an alphabet.")
else:
    print("It is not an alphabet.")
