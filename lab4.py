# 1.1
# try:
#     user_input = input("Enter a string without whitespaces: ")
#     if user_input.replace(" ", "").isalpha():  # Check if input contains only alphabetic characters
#         result_tuple = tuple(user_input)
#         print("Created tuple is:")
#         print(result_tuple)
#     else:
#         print("Invalid input. Please enter a string with alphabetic characters and no whitespaces.")
# except ValueError:
#     print(f"Wrong value!!!")

# Explanation 1.1
# try: Код находится в блоке try для обработки исключений.
# user_input = input("Enter a string without whitespaces: "): Программа запрашивает пользователя ввести строку без пробелов и сохраняет введенное значение в переменной user_input.
# if user_input.replace(" ", "").isalpha(): Эта строка проверяет, что введенная строка содержит только буквенные символы и не содержит пробелов. Для этого выполняется следующее:
# user_input.replace(" ", "") - метод replace удаляет все пробелы из введенной строки.
# .isalpha() - метод isalpha() проверяет, состоит ли строка только из буквенных символов (букв).
# Если введенная строка соответствует условиям (состоит только из буквенных символов и не содержит пробелов), программа выполняет следующие действия:
# result_tuple = tuple(user_input): Строка преобразуется в кортеж с помощью функции tuple(), и этот кортеж сохраняется в переменной result_tuple.
# print("Created tuple is:"): Программа выводит сообщение "Created tuple is:", чтобы указать, что она создала кортеж.
# print(result_tuple): Затем программа выводит сам кортеж, который был создан из введенной строки.
# Если введенная строка не соответствует условиям (содержит пробелы или не является буквенной строкой), программа выводит сообщение "Invalid input. Please enter a string with alphabetic characters and no whitespaces."
# except ValueError:: Этот блок обрабатывает исключение типа ValueError. В случае возникновения исключения, оно перехватывается, и программа выводит сообщение "Wrong value!!!".
# 1.2
# tuple_input = input("Enter a tuple as a string ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n'): ")
# try:
#     tuple_input = eval(tuple_input)
#     if isinstance(tuple_input, tuple):
#         result_string = ''.join(tuple_input)
#         print("The string is:", result_string)
#     else:
#         print("Input is not a valid tuple.")
# except NameError:
#     print("Input is not a valid tuple.")
# Explanation 1.2
# tuple_input = input("Enter a tuple as a string ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n'): "): Программа запрашивает пользователя ввести кортеж в виде строки, например: "('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')".
# try:: Код находится в блоке try для обработки исключений.
# tuple_input = eval(tuple_input): Эта строка использует функцию eval для попытки преобразовать введенную строку в кортеж. Если введенная строка соответствует формату кортежа, она будет преобразована в кортеж.
# if isinstance(tuple_input, tuple):: Эта строка проверяет, является ли tuple_input кортежем с помощью функции isinstance. Если tuple_input является кортежем, программа выполняет следующие действия:
# result_string = ''.join(tuple_input): Здесь кортеж преобразуется обратно в строку с помощью метода join. В данном случае, элементы кортежа объединяются в одну строку.
# print("The string is:", result_string): Программа выводит сообщение "The string is:" и преобразованную строку.
# Если tuple_input не является кортежем, программа выводит сообщение "Input is not a valid tuple."
# except NameError:: Этот блок обрабатывает исключение типа NameError. Если возникает исключение, программа выводит сообщение "Input is not a valid tuple."
# 1.3
# try:
#     tuple_A = eval(input("Enter tuple_A as a tuple (1, 2, 3, 4, 5, 6, 7): "))
#     tuple_B = eval(input("Enter tuple_B as a tuple (5, 6, 7, 9, 7, 1, 10, 10): "))
#     if isinstance(tuple_A, tuple) and isinstance(tuple_B, tuple):
#         midpoint_A = len(tuple_A) // 2
#         midpoint_B = len(tuple_B) // 2
#         result_tuple = tuple_A[:midpoint_A] + tuple_B[midpoint_B:]
#         print(result_tuple)
#     else:
#         print("Input is not valid tuples.")
# except (SyntaxError, NameError):
#     print("Invalid input. Please enter valid tuples.")
# Explanation 1.3
# try:: Код находится в блоке try для обработки исключений.
# tuple_A = eval(input("Enter tuple_A as a tuple (1, 2, 3, 4, 5, 6, 7): ")): Программа запрашивает пользователя ввести кортеж tuple_A, например: (1, 2, 3, 4, 5, 6, 7). eval используется для попытки преобразовать введенную строку в кортеж.
# tuple_B = eval(input("Enter tuple_B as a tuple (5, 6, 7, 9, 7, 1, 10, 10): ")): Аналогично, программа запрашивает пользователя ввести кортеж tuple_B, например: (5, 6, 7, 9, 7, 1, 10, 10).
# if isinstance(tuple_A, tuple) and isinstance(tuple_B, tuple):: Эта строка проверяет, что tuple_A и tuple_B являются кортежами.
# midpoint_A = len(tuple_A) // 2 и midpoint_B = len(tuple_B) // 2: Эти строки вычисляют индексы, разделяющие кортежи tuple_A и tuple_B пополам.
# result_tuple = tuple_A[:midpoint_A] + tuple_B[midpoint_B:]: Здесь программа объединяет первую половину tuple_A с второй половиной tuple_B. Таким образом, создается новый кортеж result_tuple.
# print(result_tuple): Программа выводит полученный кортеж result_tuple.
# Если введенные tuple_A и tuple_B не являются кортежами, программа выводит сообщение "Input is not valid tuples."
# except (SyntaxError, NameError):: Этот блок обрабатывает исключения типов SyntaxError и NameError. Если введенные данные не могут быть преобразованы в кортежи или происходит ошибка, программа выводит сообщение "Invalid input. Please enter valid tuples."
# 1.4
# def count_elements_occurrences(input_tuple):
#     element_count = {}  # Create a dictionary to store element counts
#     for element in input_tuple:
#         if element in element_count:
#             element_count[element] += 1
#         else:
#             element_count[element] = 1
#     result_list = [(key, value) for key, value in element_count.items()]
#     return tuple(result_list)
#
# input1 = input("Enter a tuple as a string (e.g., (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)): ")
# input2 = input("Enter a tuple as a string (e.g., ('55', '6', '777', 54, 6, 7777, 9, 777, 6)): ")
# input3 = input("Enter a tuple as a string (e.g., ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))): ")
#
# try:
#     input1 = eval(input1)
#     input2 = eval(input2)
#     input3 = eval(input3)
#
#     output1 = count_elements_occurrences(input1)
#     output2 = count_elements_occurrences(input2)
#     output3 = count_elements_occurrences(input3)
#
#     print("\nElements and their occurrences (Input 1):")
#     print(output1)
#
#     print("\nElements and their occurrences (Input 2):")
#     print(output2)
#
#     print("\nElements and their occurrences (Input 3):")
#     print(output3)
#
# except SyntaxError:
#     print("Invalid input. Please enter a valid tuple as a string.")
# Explanation 1.4
# У вас есть функция count_elements_occurrences(input_tuple), которая принимает кортеж input_tuple в качестве аргумента и подсчитывает, сколько раз каждый элемент встречается в этом кортеже. Результатом является кортеж пар (элемент, количество повторений элемента).
# Затем вы запрашиваете у пользователя ввод трех разных кортежей в виде строк input1, input2 и input3. Например, ввод может выглядеть так: (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6). Вы используете функцию eval, чтобы преобразовать эти строки в фактические кортежи.
# После этого, для каждого из этих кортежей (input1, input2, input3) вы вызываете функцию count_elements_occurrences, чтобы подсчитать количество повторений элементов в каждом кортеже. Результаты сохраняются в переменных output1, output2 и output3.
# Наконец, вы выводите результаты на экран. Для каждого из трех кортежей вы печатаете элементы и количество их повторений в формате пар (элемент, количество).
# В блоке try идет обработка исключений. Если введенный текст не может быть преобразован в кортеж с помощью eval, будет сгенерировано исключение SyntaxError. Если происходит другая ошибка, она будет обработана в блоке except Exception as e, и сообщение об ошибке будет выведено на экран.

# 1.5
# try:
#     sample_input = eval(input("Enter a sample input as a tuple (e.g., (55, 6, 777, 70.0, '7', 'A')): "))
#
#     if not isinstance(sample_input, tuple):
#         raise ValueError("Input must be a valid tuple.")
#
#     int_tuple = ()
#     float_tuple = ()
#     str_tuple = ()
#
#     for item in sample_input:
#         if isinstance(item, int):
#             int_tuple += (item,)
#         elif isinstance(item, float):
#             float_tuple += (item,)
#         elif isinstance(item, str):
#             str_tuple += (item,)
#
#     print("Integers:", int_tuple)
#     print("Floats:", float_tuple)
#     print("Strings:", str_tuple)
#
# except (SyntaxError, ValueError):
#     print("Invalid input. Please enter a valid tuple.")
# Explanation 1.5
# Сначала он пытается получить ввод от пользователя в виде кортежа, используя eval. Этот кортеж представляет собой sample_input.
# Затем код проверяет, является ли введенный sample_input действительным кортежем. Если это не так, генерируется исключение ValueError, указывая, что ввод должен быть действительным кортежем.
# Далее создаются три пустых кортежа: int_tuple, float_tuple и str_tuple. Эти кортежи будут использоваться для хранения элементов разных типов данных: целых чисел, чисел с плавающей запятой и строк.
# Затем код перебирает элементы в sample_input и в зависимости от их типа добавляет их в соответствующий кортеж: int_tuple для целых чисел, float_tuple для чисел с плавающей запятой и str_tuple для строк.
# Наконец, код выводит на экран содержимое каждого из кортежей: целые числа, числа с плавающей запятой и строки.
# В блоке try идет обработка исключений. Если введенный текст не может быть преобразован в кортеж с помощью eval, будет сгенерировано исключение SyntaxError. Если происходит другая ошибка, она будет обработана в блоке except (SyntaxError, ValueError), и будет выведено сообщение об ошибке.
# 2.1
# try:
#     user_input = input("Enter a string without whitespaces: ")
#     if not user_input:
#         raise ValueError("Input cannot be empty.")
#     result_set = {char for char in user_input}
#     print("Created set is:")
#     print(result_set)
# except ValueError:
#     print("Wrong value")
# Explanation 2.1
# Сначала он запрашивает ввод от пользователя в виде строки, используя input.
# Затем код проверяет, не пуст ли введенный текст, исключая случай, когда пользователь ввел пустую строку. Если введенная строка пуста, генерируется исключение ValueError с сообщением "Input cannot be empty".
# Если введенная строка не пуста, код создает множество (set) result_set, используя генератор множества, чтобы разбить введенную строку на отдельные символы.
# Наконец, код выводит на экран созданное множество result_set.
# В блоке try идет обработка исключений. Если пользователь ввел пустую строку, будет сгенерировано исключение ValueError, и будет выведено сообщение "Wrong value".
# 2.2
# try:
#     set_A = set(eval(input("Enter set_A as a set (e.g., {1, 2, 3, 4, 5}): ")))
#     set_B = set(eval(input("Enter set_B as a set (e.g., {5, 7, 8, 9, 2, 10}): ")))
#     if not isinstance(set_A, set) or not isinstance(set_B, set):
#       raise ValueError("Input must be valid sets.")
#
#     difference_set = set_A.difference(set_B)
#
#     print("The difference set is:")
#     print(difference_set)
#
# except (SyntaxError, ValueError):
#     print("Invalid input. Please enter valid sets.")
# Explanation 2.2
# Сначала он пытается получить ввод пользователя в виде двух множеств: set_A и set_B, используя eval. Эти множества представляют собой разницу между двумя множествами.
# Затем код проверяет, являются ли введенные set_A и set_B действительными множествами. Если это не так, генерируется исключение ValueError, указывая, что ввод должен быть действительными множествами.
# Далее, с использованием метода difference, код вычисляет разницу между set_A и set_B и сохраняет результат в переменной difference_set.
# Наконец, код выводит на экран разницу, то есть элементы, которые присутствуют в set_A, но отсутствуют в set_B.
# В блоке try идет обработка исключений. Если введенный текст не может быть преобразован в множества с помощью eval, будет сгенерировано исключение SyntaxError. Если происходит другая ошибка, она будет обработана в блоке except (SyntaxError, ValueError), и будет выведено сообщение об ошибке.

# 2.3
# try:
#     set_A = set(eval(input("Enter set_A as a set (e.g., {1, 2, 3, 4, 5}): ")))
#     set_B = set(eval(input("Enter set_B as a set (e.g., {5, 7, 8, 9, 2, 10}): ")))
#
#     if not isinstance(set_B, set) or not isinstance(set_A, set):
#         raise ValueError("Input must be valid sets.")
#
#     # Remove elements from set A that are also in set B
#     for element in set_A:
#         if element in set_B:
#             set_B.remove(element)
#
#     print("Updated set_A:")
#     print(set_B)
#
# except (SyntaxError, ValueError):
#     print("Invalid input. Please enter valid sets.")
# Explanation 2.3
# Сначала он пытается получить ввод пользователя в виде двух множеств: set_A и set_B, используя eval. set_A представляет множество, из которого будут удалены элементы, находящиеся также в set_B.
# Затем код проверяет, являются ли введенные set_A и set_B действительными множествами. Если это не так, генерируется исключение ValueError, указывая, что ввод должен быть действительными множествами.
# Далее, код перебирает элементы в set_A и для каждого элемента проверяет, присутствует ли он также в set_B. Если элемент находится и в set_A, и в set_B, он удаляется из set_B с помощью метода remove.
# Наконец, код выводит на экран обновленное set_B, которое больше не содержит элементы, присутствующие в set_A.
# В блоке try идет обработка исключений. Если введенный текст не может быть преобразован в множества с помощью eval, будет сгенерировано исключение SyntaxError. Если происходит другая ошибка, она будет обработана в блоке except (SyntaxError, ValueError), и будет выведено сообщение об ошибке.
# 2.4
# try:
#     set_A = set(eval(input("Enter set_A as a set (e.g., {1, 2, 3, 4, 7}): ")))
#     set_B = set(eval(input("Enter set_B as a set (e.g., {8, 7, 9, 4, 2, 0, 10}): ")))
#     set_C = set(eval(input("Enter set_C as a set (e.g., {4, 0, 1}): ")))
#
#     if not isinstance(set_A, set) or not isinstance(set_B, set) or not isinstance(set_C, set):
#         raise ValueError("Input must be valid sets.")
#
#     for element in set_B:
#         if element in set_A:
#             set_C.add(element)
#
#     print("Updated set_C:")
#     print(set_C)
#
# except (SyntaxError, ValueError):
#     print("Invalid input. Please enter valid sets.")
# Explanation 2.4
# Сначала он пытается получить ввод пользователя в виде трех множеств: set_A, set_B и set_C, используя eval. set_A представляет множество, из которого будет удаляться элемент, если он также присутствует в set_C. set_B представляет множество, элементы которого могут быть добавлены в set_C.
# Затем код проверяет, являются ли введенные set_A, set_B и set_C действительными множествами. Если это не так, генерируется исключение ValueError, указывая, что ввод должен быть действительными множествами.
# Далее, код перебирает элементы в set_B и для каждого элемента проверяет, присутствует ли он в set_A. Если элемент присутствует в set_A, он добавляется в set_C с помощью метода add.
# Наконец, код выводит на экран обновленное set_C, которое теперь содержит элементы из set_B, которые также были в set_A.
# В блоке try идет обработка исключений. Если введенный текст не может быть преобразован в множества с помощью eval, будет сгенерировано исключение SyntaxError. Если происходит другая ошибка, она будет обработана в блоке except (SyntaxError, ValueError), и будет выведено сообщение об ошибке.

# 2.5
# import itertools
#
# try:
#     A = set(eval(input("Enter superset A as a set (e.g., {1, 2, 3, 4, 5, 6}): ")))
#     n = int(input("Enter the size of each set (n): "))
#     m = int(input("Enter the number of sets to create (m): "))
#
#     if not isinstance(A, set) or not isinstance(n, int) or not isinstance(m, int) or n <= 0 or m <= 0:
#         raise ValueError("Invalid input. Please enter valid sets and positive integers.")
#
#     if n > len(A):
#         raise ValueError("The size of each set (n) cannot be greater than the size of the superset A.")
#
#     if m > len(list(itertools.combinations(A, n))):
#         raise ValueError("The number of sets to create (m) cannot be greater than the total possible combinations of A.")
#
#     combinations = list(itertools.combinations(A, n))
#     result_list = [set(combination) for combination in combinations[:m]]
#
#     print("Generated list of sets:")
#     print(result_list)
#
# except (SyntaxError, ValueError):
#     print("Invalid input. Please enter valid sets and positive integers.")
# Explanation 2.5
# Код начинается с блока try для обработки возможных ошибок.
# Пользователю предлагается ввести следующие данные:
# A: Надмножество, представленное в виде множества (например, {1, 2, 3, 4, 5, 6}).
# n: Желаемый размер каждого создаваемого набора.
# m: Количество наборов для генерации.
# Код выполняет проверку ввода:
# Проверяет, является ли A допустимым множеством, n и m - целыми числами, и что оба значения n и m положительны. Если не выполняются какие-либо из этих условий, код генерирует ValueError с соответствующим сообщением об ошибке.
# Проверяет, что значение n не превышает размер надмножества A. Если n больше размера A, то генерируется ValueError.
# Проверяет, что значение m не превышает общее количество возможных комбинаций надмножества A по n элементов. Для этого используется функция itertools.combinations. Если m превышает это ограничение, то генерируется ValueError.
# Если все проверки ввода проходят успешно, код переходит к созданию списка наборов:
# Он использует функцию itertools.combinations для генерации всех возможных комбинаций A, взятых по n элементов. Эти комбинации сохраняются в переменной combinations в виде кортежей.
# Затем создается result_list, преобразуя кортежи в combinations в наборы (множества). Рассматриваются только первые m наборов. Наборы создаются из комбинаций элементов из A.
# Наконец, код выводит созданный список наборов в консоль.
# Если в процессе проверки ввода возникают проблемы или если пользователь вводит недопустимые значения, код перехватывает и обрабатывает эти ошибки в блоке except. В этом случае будет выведено сообщение об ошибке, указывающее, что пользователь должен ввести допустимые множества и положительные целые числа.
# 3.1
# from itertools import groupby
#
# cars_list = []
#
# # Collect manufacturer and model data interactively with exception handling
# while True:
#     try:
#         manufacturer = input("Enter the manufacturer (or press Enter to finish): ")
#         if not manufacturer:
#             break
#         model = input("Enter the model: ")
#         cars_list.append((manufacturer, model))
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# # Sort the list by manufacturer
# sorted_cars_list = sorted(cars_list, key=lambda x: x[0])
#
# # Group the data by manufacturer
# for key, group in groupby(sorted_cars_list, key=lambda x: x[0]):
#     group_list = list(group)
#     print(key, len(group_list))
#     for model in group_list:
#         print("-", model[1])
# Explanation 3.1
# from itertools import groupby: Эта строка импортирует функцию groupby из модуля itertools, которая будет использоваться для группировки данных по имени производителя.
# cars_list = []: Эта строка инициализирует пустой список с именем cars_list, в котором будет храниться информация о производителе и модели автомобилей.
# Следующий раздел кода использует цикл while для интерактивного сбора данных о машинах. Он запрашивает у пользователя ввод имени производителя и модели для каждой машины:
# try:: Эта строка начинает блок try, чтобы обрабатывать возможные исключения.
# manufacturer = input("Введите имя производителя (или нажмите Enter для завершения): "): Здесь пользователю предлагается ввести имя производителя. Если пользователь нажимает Enter без ввода имени, цикл завершится, и ввод данных завершится.
# if not manufacturer:: Это условие проверяет, пусто ли поле ввода имени производителя (если пользователь нажал Enter).
# break: Если ввод имени производителя пуст, оператор break завершает цикл, завершая процесс ввода данных.
# model = input("Введите модель: "): Это приглашение пользователя ввести модель автомобиля.
# cars_list.append((manufacturer, model)): Эта строка добавляет кортеж, содержащий имя производителя и модель, в список cars_list.
# После завершения ввода данных код переходит к сортировке и группировке данных:
# sorted_cars_list = sorted(cars_list, key=lambda x: x[0]): Эта строка сортирует cars_list на основе имени производителя. Функция key извлекает первый элемент из каждого кортежа (имя производителя) для сортировки.
# Следующий раздел использует функцию groupby для группировки данных по имени производителя:
# for key, group in groupby(sorted_cars_list, key=lambda x: x[0]):: Этот цикл перебирает группы автомобилей по имени производителя.
# group_list = list(group): Эта строка преобразует группу автомобилей в список.
# print(key, len(group_list)): Здесь выводится имя производителя и количество моделей автомобилей для этого производителя.
# Вложенный цикл перебирает модели автомобилей в группе и выводит каждую из них в виде маркера:
# print("-", model[1]): Эта строка выводит название модели автомобиля, используя индекс [1] кортежа (название модели).
# Код обернут в блок try-except для обработки исключений во время ввода данных, предоставляя сообщения об ошибках в случае ошибок ввода или непредвиденных проблемах.

