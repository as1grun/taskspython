# Task 1
# def relation(num):
# thousands = num // 1000
# hundreds = (num // 100) % 10
# tens = (num// 10) % 10
# units= num % 10
# if (thousands + units) == abs(tens - hundreds):
#    return "yes"
# else:
#    return "no"
# num = int(input("enter a four-digit number: "))
# print(relation(num))


# Task2
# def check_access(age):
#    if age >= 18:
#      return "access is allowed"
#   else:
#       return "access is prohibited"
# age = int(input("Введите возраст пользователя: "))
# print(check_access(age))


# Task3
# def check_progression(A,B,C):
#    return (B - A) == (C - B)
# A = int(input("введите первое число: "))
# B = int(input("введите второе число: "))
# C = int(input("Введите третье число: "))
# if check_progression(A,B,C):
#    print("Да")
# else:
#    print("Нет")


# Task4
# def can_king_move(col1, row1, col2, row2):

#     return abs(col1 - col2) <= 1 and abs(row1 - row2) <= 1


# col1, row1, col2, row2 = map(int, input().split())


# if can_king_move(col1, row1, col2, row2):
#     print("ДА")
# else:
#     print("НЕТ")


# 4Task 5
# def can_king_move(col1, row1, col2, row2):

#     diff_col = abs(col1 - col2)
#     diff_row = abs(row1 - row2)

#     return diff_col <= 1 and diff_row <= 1

# col1, row1, col2, row2 = map(int, input().split())

# # Проверяем возможность хода короля
# if can_king_move(col1, row1, col2, row2):
#     print("ДА")
# else:
#     print("НЕТ")


# Task6
# a = int(input())
# b = int(input())
# c = int(input())
# middle_num = a + b + c - min(a, b, c) - max(a, b, c)

# print( middle_num)

# task7
# month_ordinal = int(input("Enter the ordinal number of the month: "))
#
# days_in_month = {
#     1: 31,  # January
#     2: 28,  # February (non-leap year)
#     3: 31,  # March
#     4: 30,  # April
#     5: 31,  # May
#     6: 30,  # June
#     7: 31,  # July
#     8: 31,  # August
#     9: 30,  # September
#     10: 31, # October
#     11: 30, # November
#     12: 31  # December
# }
#
# if 1 <= month_ordinal <= 12:
#     num_days = days_in_month[month_ordinal]
#     print(f"Number of days in month {month_ordinal}: {num_days}")
# else:
#     print("Invalid month ordinal. Please enter a number between 1 and 12.")

# Task8
# weight = int(input("Введите вес боксера: "))

# if weight <= 60:
#    print("Малый вес")
# elif weight <= 64:
#    print("Первый полусредний вес")
# elif weight <= 69:
#    print("Полусредний вес")
# else:
#    print("Вы не соответствуете нашему весу")

# Task9
# def check_password(password1,password2):
#    return password1 == password2
# password1 = input("Введите пароль: ")
# password2 = input("Подтвердите пароль: ")
# if check_password(password1,password2):
#    print("Пароль принят")
# else:
#    print("Пароль не принят")


# Task10

# def check_even_odd(num):
#    if num % 2 == 0:
#       return "Четное"
#    else:
#        return "Нечетное"
# number = int(input("Введите целое число: "))
# result = check_even_odd(number)
# print(f"Число является {result}")

# Task11
# def find_minnum(num1, num2):
#    if num1 < num2:
#        return num1
#    else:
#        return num2
# num1 = int(input("Введите первое целое число: "))
# num2 = int(input("Введите второе целое число: "))
# min_number = find_minnum(num1, num2)
# print( min_number)

# Task12
# def determine_group(age):
#        return "детское"
#   elif 14 <= age <= 24:
#       return "молодежь"
#    elif 25 <= age <= 59:
#        return "зрелость"
#    else:
#        return "старость"
#
# age = int(input("Введите возраст: "))
# age_group = determine_group(age)
# print("Пользователь принадлежит к возрастной группе:", age_group)

# Task13

# def determine_type(a, b, c):
#     if a == b == c:
#         return "Равносторонний"
#     elif a == b or b == c or a == c:
#         return "Равнобедренный"
#     else:
#         return "Универсальный"

# a = int(input("Введите длину первой стороны: "))
# b = int(input("Введите длину второй стороны: "))
# c = int(input("Введите длину третьей стороны: "))

# type_triangle_ = determine_type(a, b, c)
# print(type_triangle)