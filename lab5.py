# 1.1
# try:
#     word = input("Write words with whitespace:")
#     if not word:
#         print("Input is empty!!!")
#
#     wordlist = list(word.lower())
#     print(wordlist)
# except ValueError:
#     print("Wrong value!!!")
# 1.2
# try:
#     word = input("Write words:  ")
#     if not word:
#         print("Input is empty!!!")
#
#     wordlist = list(word.lower())
#
#     count = {}
#     for element in wordlist:
#         if element in count:
#             count[element] += 1
#         else:
#             count[element] = 1
#
#     result = [(key, value) for key, value in count.items()]
#     print("Result: ")
#     print(result)
#
# except ValueError:
#     print("Wrong value!!!")
# 1.3
# try:
#     word = input("Write words:  ")
#     if not word:
#         print("Input is empty!!!")
#
#     wordlist = list(word.lower())
#
#     vow_list = []
#     cons_list = []
#     symbol_list = []
#
#     for element in wordlist:
#         if element in 'aeiou':
#             vow_list.append(element)
#         elif element.isalpha():
#             cons_list.append(element)
#         else:
#             symbol_list.append(element)
#
#     print("Vowels: ", vow_list)
#     print("Consonants: ", cons_list)
#     print("Symbols: ", symbol_list)
#
# except ValueError:
#     print("Wrong value!!!")
# 1.4
# try:
#     list_A = input("Write a list of numbers separated by commas: ")
#     if not list_A:
#         print("Input is empty!!!")
#
#     number_list = [int(x) for x in list_A.split(',')]
#     number_list.sort()
#
#     num = len(number_list)
#     q1 = number_list[:num // 4]
#     q2 = number_list[num // 4:num // 2]
#     q3 = number_list[num // 2:3 * num // 4]
#     q4 = number_list[3 * num // 4:]
#
#     print("q1 =", q1)
#     print("q2 =", q2)
#     print("q3 =", q3)
#     print("q4 =", q4)
#
# except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!! ")
# 2.1
# try:
#     student_name = input("Write the student's name: ")
#     assignment_scores = input("Write scores for assignments: ").split(",")
#     lab_scores = input("Write scores for labs: ").split(",")
#     test_scores = input("Write scores for tests: ").split()
#
#     assignment_scores = [int(score) for score in assignment_scores]
#     lab_scores = [float(score) for score in lab_scores]
#     test_scores = [int(score) for score in test_scores]
#
#     student = {
#         'name': student_name,
#         'assignment': assignment_scores,
#         'lab': lab_scores,
#         'test': test_scores
#     }
#
#     print("Student information:")
#     print(student)
#
# except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!! ")
# 2.2
# try:
#     student_name = input("Write student's name: ")
#
#     assignment_scores = list(map(int, input("Write assignment scores: ").split(',')))
#     lab_scores = list(map(float, input("Write lab scores: ").split(',')))
#     test_scores = list(map(int, input("Write test scores: ").split(',')))
#
#     submission_check = {}
#
#     total_submissions = len(assignment_scores) + len(lab_scores) + len(test_scores)
#
#     if total_submissions == 8:
#         submission_check[student_name] = total_submissions
#     else:
#         submission_check[student_name] = 0
#
#     print("Submission Check:")
#     print(submission_check)
#
# except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!! ")
# 2.3
# try:
#     def calculate_final_grade(grades):
#         return 0.3 * (sum(grades['assignment'])/len(grades['assignment'])) + 0.5 * (sum(grades['lab'])/len(grades['lab'])) + 0.2 * (sum(grades['test'])/len(grades['test']))
#
#     students = {}
#
#     num_students = int(input("Write the number of students: "))
#
#     for _ in range(num_students):
#         name = input("Write student name: ")
#         assignment = [int(score) for score in input("Write assignment scores: ").split(',')]
#         test = [int(score) for score in input("Write test scores: ").split(',')]
#         lab = [float(score) for score in input("Write lab scores: ").split(',')]
#
#         submission_rate = int(input("Write the submission rate: "))
#
#         student = {'name': name, 'assignment': assignment, 'test': test, 'lab': lab}
#
#         if submission_rate >= 4:
#             student['final_grade'] = calculate_final_grade(student)
#         else:
#             student['final_grade'] = 0
#
#         students[name] = student
#
#     for student in students.values():
#         print(student)
#
# except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!! ")
# 2.4
# try:
#     students = {}
#
#     name1 = input("Write the name of the 1st student: ")
#     assignment1 = [int(score) for score in input("Write assignment scores: ").split(',')]
#     test1 = [int(score) for score in input("Write test scores: ").split(',')]
#     lab1 = [float(score) for score in input("Write lab scores: ").split(',')]
#     final_grade1 = float(input("Write the final grade: "))
#
#     students[name1] = {'assignment': assignment1, 'test': test1, 'lab': lab1, 'final_grade': final_grade1}
#
#     name2 = input("Write the name of the 2st student: ")
#     assignment2 = [int(score) for score in input("Write assignment scores: ").split(',')]
#     test2 = [int(score) for score in input("Write test scores: ").split(',')]
#     lab2 = [float(score) for score in input("Write lab scores: ").split(',')]
#     final_grade2 = float(input("Write the final grade: "))
#
#     students[name2] = {'assignment': assignment2, 'test': test2, 'lab': lab2, 'final_grade': final_grade2}
#
#     print("students =", students)
#
# except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!!")

# 3.1
# try:
#     transactions = []
#
#     user_stats = {}
#
#     while True:
#         user_id = int(input("Write user ID (0 to stop): "))
#         if user_id == 0:
#             break
#         transaction_type = int(input("Write transaction (1-comment, 2-like, 3-share): "))
#
#         transactions.append((user_id, transaction_type))
#
#     for user_id, transaction_type in transactions:
#         if user_id not in user_stats:
#             user_stats[user_id] = {1: 0, 2: 0, 3: 0}
#
#         user_stats[user_id][transaction_type] += 1
#
#     for user_id, stats in user_stats.items():
#         most_frequent = max(stats, key=stats.get)
#         least_frequent = min(stats, key=stats.get)
#         stats['mft'] = most_frequent
#         stats['lft'] = least_frequent
#
#     for user_id, stats in user_stats.items():
#         print(f"User ID: {user_id}, Statistics: {stats}")
#
# except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!!")







