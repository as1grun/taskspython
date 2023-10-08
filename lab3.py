# Task1
# try:
#     N = int(input("Enter a positive integer N: "))
#     if N <= 0:
#         raise ValueError("N must be a positive integer")
#
#     i = 1
#     while i <= N:
#         if i % 2 == 0:
#             print(i)
#         i += 1
# except ValueError as e:
#     print(f"Error: {e}")
# Task2
# try:
#     N = int(input("Enter a positive integer N: "))
#     if N < 0:
#         raise ValueError("N must be a non-negative integer")
#
#     factorial = 1
#     i = 1
#     while i <= N:
#         factorial *= i
#         i += 1
#
#     print(f"The factorial of {N} is {factorial}")
# except ValueError as e:
#     print(f"Error: {e}")
# Task3
# try:
#     while True:
#         num = int(input("Enter a number (or 0 to quit): "))
#         if num == 0:
#             break
#         elif num == 42:
#             print("Number 42 found! Exiting.")
#             break
# except ValueError as e:
#     print(f"Error: {e}")
# Task4
# try:
#     user_input = input("Enter a string: ")
#     count = user_input.lower().count('a')
#     print(f"The number of 'a's in the string is: {count}")
# except Exception as e:
#     print(f"Error: {e}")
# Task5
# try:
#     num = input("Enter a number: ")
#     num = int(num)
#     if num < 0:
#         raise ValueError("Number must be non-negative")
#
#     digit_sum = sum(int(digit) for digit in str(num))
#     print(f"The sum of digits is: {digit_sum}")
# except ValueError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Error: {e}")
# Task6
# try:
#     N = int(input("Enter a positive integer N: "))
#     if N <= 0:
#         raise ValueError("N must be a positive integer")
#
#     a, b = 0, 1
#     count = 0
#     while count < N:
#         print(a)
#         a, b = b, a + b
#         count += 1
# except ValueError as e:
#     print(f"Error: {e}")
# Task7
# try:
#     user_input = input("Enter a string: ")
#     reversed_string = user_input[::-1]
#     print(f"The reversed string is: {reversed_string}")
# except Exception as e:
#     print(f"Error: {e}")
# Task8
# try:
#     sum_of_odd = 0
#     while True:
#         num = int(input("Enter a number (0 to quit): "))
#         if num == 0:
#             break
#         if num % 2 == 0:
#             continue
#         sum_of_odd += num
#     print(f"The sum of odd numbers is: {sum_of_odd}")
# except ValueError as e:
#     print(f"Error: {e}")
# Task9
# import random
#
# try:
#     target_number = random.randint(1, 100)
#     while True:
#         guess = int(input("Guess the number (1-100): "))
#         if guess < target_number:
#             print("Too small!")
#         elif guess > target_number:
#             print("Too large!")
#         else:
#             print("Congratulations! You guessed the number.")
#             break
# except ValueError as e:
#     print(f"Error: {e}")
# Task10
# try:
#     user_input = input("Enter a string: ")
#     user_input = user_input.lower().replace(" ", "")
#     if user_input == user_input[::-1]:
#         print("It's a palindrome!")
#     else:
#         print("It's not a palindrome.")
# except Exception as e:
#     print(f"Error: {e}")
# Task11
# try:
#     X = float(input("Enter the base number X: "))
#     Y = int(input("Enter the power Y: "))
#
#     result = 1
#     count = 0
#
#     while count < abs(Y):
#         result *= X
#         count += 1
#
#     if Y < 0:
#         result = 1 / result
#
#     print(f"{X} to the power of {Y} is: {result}")
# except ValueError as e:
#     print(f"Error: {e}")
# Task12
# try:
#     N = int(input("Enter a positive integer N: "))
#     if N <= 0:
#         raise ValueError("N must be a positive integer")
#
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     number = 1
#     while number <= N:
#         if is_prime(number):
#             print(number)
#         number += 1
# except ValueError as e:
#     print(f"Error: {e}")
# Task13
# try:
#     num = input("Enter a number: ")
#     reversed_num = num[::-1]
#     print(f"The reversed number is: {reversed_num}")
# except Exception as e:
#     print(f"Error: {e}")
# Task14
# try:
#     num = int(input("Enter a number: "))
#
#
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#
#     while True:
#         if is_prime(num):
#             print(f"{num} is a prime number.")
#             break
#         else:
#             print(f"{num} is not a prime number.")
#             num += 1
# except ValueError as e:
#     print(f"Error: {e}")
# Task15
try:
    text = input("Enter a string: ")
    shift = int(input("Enter the shift value N: "))


    def caesar_cipher(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = (ord(char.lower()) - ord('a') + shift) % 26
                encrypted_char = chr(ord(char) + shift_amount)
                if char.isupper():
                    encrypted_char = encrypted_char.upper()
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text


    encrypted_text = caesar_cipher(text, shift)
    print(f"The encrypted string is: {encrypted_text}")
except ValueError as e:
    print(f"Error: {e}")
