grades = [[5,3,3,5,4] , [2,2,2,3] , [4,5,5,2] , [4,4,2] , [5,5,5,4,5]]
students = {'Johnny' , 'Bildo' , 'Steve' , 'Khendrik' , 'Aaron'}
students = sorted(students)
grades_sred = [sum(grades) / len(grades) for grades in grades]
a = dict(zip(students, grades_sred))

print(a)
