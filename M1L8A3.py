# Program to find the corrected mean of 40 numbers

# Store the given values
average = 38
incorrect_value = 36
actual_value = 56
count = 40

# Calculate the original total
original_total = average * count
print("Original sum of the numbers:", original_total)

# Correct the total by replacing the incorrect value
updated_total = original_total - incorrect_value + actual_value
print("Corrected sum of the numbers:", updated_total)

# Calculate and display the new mean
new_average = updated_total / count
print("Corrected mean:", new_average)
