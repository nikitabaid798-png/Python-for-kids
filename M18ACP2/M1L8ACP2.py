# Program to swap two numbers entered by the user

# Take two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display numbers before swapping
print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swap the values using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Display numbers after swapping
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
