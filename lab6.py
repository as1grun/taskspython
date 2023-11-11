# Task 1
# def get_keys_with_value_true(input_dict):
#     return [key for key, value in input_dict.items() if value == True]
# input_dict = {}
# try:
#     n = int(input("Write the number of k-v: "))
#     for _ in range(n):
#         key = input("Write a key: ")
#         value = input("Write a value True or False: ").lower()
#         input_dict[key] = value == "true"
#     result = get_keys_with_value_true(input_dict)
#     print(result)
#
# except ValueError:
#     print("wrong value!!!")
# except KeyError as e:
#     print("Key not found!!!")

# Task 2
# def get_unique_elements(input_list):
#     unique_elements = [x for x in input_list if input_list.count(x) == 1]
#     return unique_elements
# try:
#     input_list = input("write the nums:").split()
#     input_list = [int(x) for x in input_list]
#     result = get_unique_elements(input_list)
#     print(result)
# except ValueError:
#     print("wrong value!!!")

# Task 3
# def get_date_in_format(date):
#     try:
#         parts = date.split(".")
#         changed_date = f"{parts[2]}.{parts[1]}.{parts[0]}"
#         return changed_date
#     except IndexError:
#         print("write in the format 'yyyy.mm.dd'.")
# date = input("Write the date: ")
# result = get_date_in_format(date)
# print(result)


# Task 4
# def get_elements_with_no_more_than_two_occurrences(input_list):
#     try:
#         result = [x for x in input_list if input_list.count(x) <= 2]
#         return result
#     except ValueError:
#         print("wrong value!!!")
# input_list = input("write the nums: ").split()
# try:
#     input_list = [int(x) for x in input_list]
#     result = get_elements_with_no_more_than_two_occurrences(input_list)
#     print(result)
# except ValueError:
#     print("wrong value!!!")


# Task5
# def get_words_from_string(input_string):
#     try:
#         words = input_string.split()
#         return words
#     except ValueError:
#         print("wrong value!!!")
# input_string = input("Write the string: ")
# result = get_words_from_string(input_string)
# print(" ", result)


# Task 6
# def get_unique_elements_with_count(input_list):
#     try:
#         dict_count = {}
#         for item in input_list:
#             dict_count[item] = dict_count.get(item, 0) + 1
#         return dict_count
#
#     except ValueError:
#         print("wrong value!!!")
#
# input_list = input("Write the nums").split()
# try:
#     input_list = [int(x) for x in input_list]
#
#     result = get_unique_elements_with_count(input_list)
#     print(result)
#
# except ValueError:
#     print("wrong value!!!")
#
# # Task 7
# def get_prime_numbers(n):
#     try:
#         prime_numbers = []
#         for num in range(2, n + 1):
#             is_prime = True
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 prime_numbers.append(num)
#         return prime_numbers
#
#     except ValueError:
#         print("wrong value!!!")
#
# n = int(input("Write a number (n): "))
# try:
#     result = get_prime_numbers(n)
#     print(" ", result)
#
# except ValueError:
#     print("wrong value!!!")
#
# # Task 8
# def is_prime(num):
#     try:
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     except ValueError:
#         print("wrong value!!!")
#
# def get_prime_numbers_in_list(input_list):
#     try:
#         prime_numbers = [x for x in input_list if is_prime(x)]
#         return prime_numbers
#
#     except ValueError:
#         print("wrong value!!!")
#
# input_list = input("Write the nums ").split()
# try:
#     input_list = [int(x) for x in input_list]
#
#     result = get_prime_numbers_in_list(input_list)
#     print(" ", result)
#
# except ValueError:
#     print("wrong value!!!")
#
# # Task 9
# from datetime import datetime
#
# def get_difference_between_dates(date1, date2):
#     try:
#         date_format = "%Y.%m.%d"
#         date1_obj = datetime.strptime(date1, date_format)
#         date2_obj = datetime.strptime(date2, date_format)
#         delta = date2_obj - date1_obj
#         return delta.days
#
#     except ValueError:
#         print("wrong value!!!")
#
# date1 = input("Write the first date : ")
# date2 = input("Write the second date: ")
# try:
#     result = get_difference_between_dates(date1, date2)
#     print(result)
#
# except ValueError:
#     print("write  in the format yyyy.mm.dd")

# # Task 10
# def get_decimal_number_from_binary_string(binary_string):
#     try:
#         decimal = int(binary_string, 2)
#         return decimal
#
#     except ValueError:
#         print("wrong value!!!")
#
# binary_string = input("Write a binary string: ")
# try:
#     result = get_decimal_number_from_binary_string(binary_string)
#     print(result)
#
# except ValueError:
#     print("write a binary string.")
#
# # Task 11
# def is_expression_true(expression):
#     try:
#         numbers = [int(num) for num in expression.split(', ')]
#         perfect_square = all(int(num ** 0.5) ** 2 == num for num in numbers)
#         return perfect_square
#
#     except ValueError:
#         print("wrong value!!!")
#
# expression = input("write nums: ")
# try:
#     result = is_expression_true(expression)
#     print(result)
#
# except ValueError:
#     print("wrong value!!!")
#
# # Task 12
# def get_price(item):
#     return item["price"]
#
# def sort_by_price(shopping_list):
#     try:
#         sorted_list = sorted(shopping_list, key=get_price)
#         return sorted_list
#
#     except ValueError:
#         print("wrong value!!!")
#
# shopping_list = []
# n = int(input("amount of items"))
# try:
#     for i in range(n):
#         item_name = input("write name: ")
#         item_price = float(input("write price: "))
#         shopping_list.append({"name": item_name, "price": item_price})
#
#     result = sort_by_price(shopping_list)
#     print(result)
#
# except ValueError:
#     print("wrong value!!!")
#
# # Task 13
# def get_words_starting_with_vowel(words):
#     try:
#         vowel_starting_words = [word for word in words if word[0].lower() in ['a', 'e', 'i', 'o', 'u']]
#         return vowel_starting_words
#
#     except ValueError:
#         print("Wrong value!!!")
#
# words = input("Write a words:").split()
# try:
#     result = get_words_starting_with_vowel(words)
#     print(result)
#
# except IndexError:
#     print("wrong index!!!")
