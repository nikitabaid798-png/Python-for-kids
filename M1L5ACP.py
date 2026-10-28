# Program to plan your afternoon

# Ask the user how many hours homework will take
homework_hours = float(input("How many hours will your homework take? "))

# Check how much time homework will take
if homework_hours > 0:
    print("First, complete your homework.")

else:
    print("Your homework is done! Enjoy your free time.")

# Remind the user to enjoy free time only if some is available
if homework_hours < 3 and homework_hours > 0:
    print("You will have some free time. Enjoy it!")

elif homework_hours >= 3:
    print("Focus on your homework first. Enjoy your free time when you finish!")
