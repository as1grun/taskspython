# 1 task
# name = input("What is your name? ")
#
# while True:
#     yourSalary = input(f"{name},how many salary you want? ")
#     try:
#         salary = int(yourSalary)
#         break
#     except ValueError:
#         print("write in digital format!!!")
# tax = salary * 0.2
# print(f"{name}, the tax level you will pay with the salary {salary} is {tax}")
#
# 2 task
# addition = lambda x, y: x + y
# multiplication = lambda x, y: x * y
# division = lambda x, y: x / y
# exponentiation = lambda x, y: x ** y
#
# operations = {
#     1: addition,
#     2: multiplication,
#     3: division,
#     4: exponentiation
# }
# print(choose the task you want to perform:")
# print("1. Addition\n2. Multiplication\n3. Division\n4. Exponentiation")
# choice = int(input("User Input: "))
#
# if choice not in operations:
#     print("Invalid operation!!!")
# else:
#     operation = operations[choice]
#     if choice == 4:
#         numbers = input("Write the separated numbers ").split(',')
#         if len(numbers) != 2:
#             print("Write two numbers:)
#         else:
#             x, y = map(float, numbers)
#             result = operation(x, y)
#             print(result)
#     else:
#         numbers = input("Write the two numbers ").split(',')
#         if len(numbers) != 2:
#             print("Write two numbers separated by a comma.")
#         else:
#             x, y = map(float, numbers)
#             result = operation(x, y)
#             print(result)
# 3 task
# length = int(input("Write the length:  "))
# fsequence = [1, 1]
# for i in range(2, length):
#     next_number = fsequence[i - 1] + fsequence[i - 2]
#     fsequence.append(next_number)
# print(f"The Fibonacci lenght {length} is")
# print(", ".join(map(str, fsequence)))
# 4 task
# uni_items = set()
# not_uni_items = []
# while True:
#     print(choose the task you want to perform:")
#     print("1. Enter items")
#     print("2. Exit")
#     choice = int(input("User Input: "))
#
#     if choice == 1:
#         items_input = input("Write items separated by a comma: ")
#         items = [item.strip() for item in items_input.split(',')]
#         uni_items.update(items)
#
#         for item in set(items):
#             count = items.count(item)
#             if count > 1:
#                 not_uni_items.append((item, count))
#
#         print("Items are saved")
#     elif choice == 2:
#         break
#     else:
#         print("Invalid choice.")
#
# print("Unique items:", uni_items)
# print("Not unique items:", tuple(not_uni_items))
# 5 task
list_for_task = []
completed_tasks = []
while True:
    print("Choose the task you want to perform:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")
    choice = int(input("User Input: "))

    if choice == 1:
        task = input("Enter the task: ")
        list_for_task.append(task)
        print(f"The task '{task}' was added to the todo list.")
    elif choice == 2:
        print("All Tasks:")
        for i, task in enumerate(list_for_task, 1):
            print(f"{i}. {task}")
    elif choice == 3:
        task = input("Write the name of the task: ")
        if task in list_for_task:
            list_for_task.remove(task)
            completed_tasks.append(task)
            print(f"The task '{task}' is marked as completed.")
        else:
            print(f"The task '{task}' was not found in the list for .")
    elif choice == 4:
        print("Completed Tasks:")
        for i, task in enumerate(completed_tasks, 1):
            print(f"{i}. {task}")
    elif choice == 5:
        break
    else:
        print("Invalid choice!!!")
