import matplotlib.pyplot as plt

name = []
grade = []

n = int(input(" enter the number of students "))

for i in range(n):
    name.append(input(" enter the name of the studemt "))
    grade.append(int(input(" enter the grade of the student ")))


color = ["red", "green", "blue", "yellow"]

plt.bar(name, grade, color=color)
plt.show()
