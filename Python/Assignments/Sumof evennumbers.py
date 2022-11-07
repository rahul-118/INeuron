# List of numbers which will used as input
numbers = [12, 75, 150, 180, 145, 525, 50]

# declaring a variable to calculate and store sum
sum = 0

#Logic for calculating sum of even numbers

for i in numbers:
    if i%2 ==0:
        sum = sum + i

# printing the output
print(sum)
