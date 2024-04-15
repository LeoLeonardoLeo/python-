print("this is a python test")
# uses hash for comments

# python does not use semicolons ;
# variables

#integers
age = 20  # dont need a declaration like int or string
print("age is:", age)  #uses a comma instead of a +
print(f"age is {age}")  #f string
negative = -50
print(f"you are {negative} years old")

# floats
price = 5.55
print(f"the price is ${price}")

# string
name = "Leo"
print(f"Name is {name}")

# boolean - true or false
isTrue = True  #capital always
isFalse = False

print(f"is this true or false? {isTrue}")
print(f"is this true or false? {isFalse}")

# user input
name = input("What is your name: ")
print(f"hello {name}")

# adding 2 user input numbers
number1 = input("enter number 1: ")
number1 = int(number1)  #making this into an int (number)

number2 = input("enter number 2: ")
number2 = int(number2)

addedNum = number1 + number2
print(addedNum)

# if we dont add the int() then both numbers would be combined instead of added
# if we input 5 and 5 it would be 55 not 10
# the int fixes this

# mini calculator that finds average of 3 numbers
cal_number1 = int(input("enter first number: "))
cal_number2 = int(input("enter second number: "))
cal_number3 = int(input("enter third number: "))
avg = (cal_number1 + cal_number2 + cal_number3) / 3
print(f"average of {cal_number1}, {cal_number2}, {cal_number3} is {avg}")