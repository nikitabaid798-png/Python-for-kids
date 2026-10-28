# Part 1: Import the keyword module
import keyword

# Part 2: Ask the user for information
name = input("Enter your name: ")
skill = input("Enter a Python skill you want to learn: ")
target_month = input("Enter your target month: ")

# Part 3: Store 30 in daily_minutes
daily_minutes = 30

# Part 4: Print a heading with a blank line above and below
print("\nMY PYTHON LEARNING PLAN\n")

# Part 5: Print four labelled lines of the plan
print("Name:", name)
print("Skill to learn:", skill)
print("Target month:", target_month)
print("Daily practice time:", daily_minutes, "minutes")

# Part 6: Print two messages on the same line using end=
print("Keep practising! ", end="")
print("You can do it!")

# Part 7: Print Python's reserved keyword list
print("\n\nPython reserved keywords:")
print(keyword.kwlist)
