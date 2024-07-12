import os

os.system("cls") 

students = []


with open("students.txt", "r") as file:
    data = file.read().split("\n")
    
    for line in data:
        if line.strip():  
            parts = line.split("|")
            name = parts[0].strip()
            age = int(parts[1].strip())
            ball_scores = [int(score.strip()) for score in parts[2].strip()[1:-1].split(',')]  
            student = {
                'name': name,
                'age': age,
                'ball': ball_scores
            }
            students.append(student)

total_ball = sum(sum(student['ball']) for student in students)
average_ball = total_ball / len(students)


with open("highachievers.txt", "w") as highachieversFile:
    for student in students:
        if sum(student['ball']) / len(student['ball']) > 70: 
            highachieversFile.write(f"{student['name']}|{student['age']}|{sum(student['ball']) / len(student['ball'])}\n")



