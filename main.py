#
# Task1.1
# sequence = [4, 8, 15, 16, 23, 42]
#
# for number in sequence:
#         print(f"{number}",end=' ')
# Task1.2
# sequence = [4, 8, 15, 16, 23, 42]
#
# for number in sequence:
#         print(f"{number}")
# Task1.3
# try:
#     number = int(input("Write the number: "))
#
#     print(f"{number}, {number+1}, {number+2}")
#     # while number<number + 2:
#     #
#     #         number += 1
#     #         print(f"{number}")
#     #         break
# except ValueError:
#     print("another input")
#
# Task1.4
#
# num1 = int(input("Write the number 1: "))
# num2 = int(input("Write the number 2: "))
# num3 = int(input("Write the number 3: "))
# print(f"{num1+num2+num3}")
# Task1.5
# num = int(input("Write the number: "))
# v = num*num*num
# p = 6*num*num
# print(f"{v}")
# print(f"{p}")
#
# Task2.1
# try:
#     students = int(input("Write the number of students: "))
#     fruits = int(input("Write the number of fruits: "))
#
#     amount = int(fruits//students)
#     ostatok = int(fruits-(students*amount))
#     print(f"{amount}")
#     print(f"{ostatok}")
#
# except ValueError:
#
#     print("Wrong value!!!")
#
# Task2.2
# try:
#     number = int(input("Enter a four-digit number: "))
#     if 1000 <= number <= 9999:
#
#         thousands = number // 1000
#         hundreds = (number // 100) % 10
#         tens = (number // 10) % 10
#         units = number % 10
#
#         print(f"The digit in the thousands place is {thousands}")
#         print(f"The digit in the hundreds place is {hundreds}")
#         print(f"The digit in the tens place is {tens}")
#         print(f"The digit in the units place is {units}")
#     else:
#         print("You entered a number that is not four digits.")
# except ValueError:
#     print("You entered an invalid value.")
#
# Task2.3
# try:
#     people = int(input("Enter the amount of people: "))
#     if people % 2 == 1:
#         vyzhyvshye = (people + 1) // 2
#     else:
#         vyzhyvshye = people // 2
#     print(vyzhyvshye)
# except ValueError:
#     print("You entered an invalid value.")
#
# Task2.4
# try:
#     num = int(input("Enter a number: "))
#
#     result = num << 1
#
#     if result == 0:
#         print("Warning!!! The result of << is zero.")
#     else:
#         print(f"The result of << is {result}")
#
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#
# Task2.5
try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    operation = input("Please choose the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please choose from +, -, *, /")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
