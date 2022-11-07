# Taking input from user
num1 = int(input("Please Enter First Number: "))
num2 = int(input("Please Enter Second Number: "))
num3 = int(input("Please Enter Third Number: "))

#Logic to find greatest number
if (num1 >= num2) & (num1 >= num3):
    print("Greatest Number is: ",num1)
elif (num2 >= num1) & (num2 >= num3):
    print("Greatest Number is: ",num2)
else:
    print("Greatest Number is: ",num3)