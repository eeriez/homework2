grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average = [1, 2, 3, 4, 5]
average[0] = round(sum(grades[0]) / len(grades[0]), 2)
average[1] = round(sum(grades[1]) / len(grades[1]), 2)
average[2] = round(sum(grades[2]) / len(grades[2]), 2)
average[3] = round(sum(grades[3]) / len(grades[3]), 2)
average[4] = round(sum(grades[4]) / len(grades[4]), 2)

students = list(students)
students.sort()

grade_sheet = dict(zip(students, average))
print(grade_sheet)
