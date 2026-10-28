print("Enter a Number (Numerator): ")
num1 = int(input())
print("Enter a Number (denominator): ")
num2 = int(input())

if num1%num2==0:
  print("\n" +str(num1)+ " is divisible by " +str(num2))
else:
  print("\n" +str(num1)+ " is not divisible by " +str(num2))
