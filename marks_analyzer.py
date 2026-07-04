# # PROJECT 1
# # STUDENT MARKS ANALYSER

import numpy as np
students = []
names = []
subjects = ['physics','chemistry','maths','computer','fine arts']
for i in range(10):#LOOP FOR STUDENT NUM
    marks = []
    print(f'student {i+1}:')
    name = input('student name is : ')
    names.append(name)
    for j in range(len(subjects)):#LOOP FOR SUBJECT 
        mar = int(input(f"{subjects[j]} marks : "))
        marks.append(mar)
    students.append(marks)
mark_arr = np.array(students)
print('array of marks')
print(mark_arr)

# CALCULATING SUM OF MARKS OF EACH STUDENT

total = np.sum(mark_arr,axis = 1)
print(f'total marks of each student is {total}')
# now percentage
print('percentage of each student is :')
max_marks = len(subjects) * 100
per = (total/max_marks) * 100
for i in range(len(per)):
    print(f'name : {names[i]}')
    print(f'percentage: {per[i]:.2f}%')
    if per[i]>=90 :
        print('Grade : A')
    elif per[i]>=80:
        print('Grade :  B')
    elif per[i]>=70:
        print('Grade : C')
    elif per[i]>=60:
        print('Grade : D')
    else:
        print('Grade : F')
    if per[i]>=33:
        print(' Status : pass')
    else:
        print('Status : fail')
    print("-" * 30)


# NOW FINDING HIGHEST AND LOWEST SCORER OF THE CLASS
high = np.argmax(total)
low = np.argmin(total)

# HIGHEST MARK

print(f'highest marks: {names[high]}')
print(f'total marks of {names[high]}: {total[high]}')
print(f'percentage : {per[high]:.2f}%')


# LOWEST MARK

print(f'lowest marks: {names[low]}')
print(f'total marks of {names[low]}: {total[low]}')
print(f'percentage : {per[low]:.2f}%')
print('average performance of the class is : ')
print(f'{np.mean(per):.2f}%')

# NOW SUBJECT WISE TOPPER

high_mark = np.argmax(mark_arr,axis = 0)
for i in range(len(subjects)):
    print(f'{subjects[i]} topper : {names[high_mark[i]]} ({mark_arr[high_mark[i],i]})')

