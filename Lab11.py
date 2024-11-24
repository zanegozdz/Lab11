import matplotlib.pyplot as plt
import os

def main():
    file_path = "C:\\Users\\Zmgoz\\OneDrive\\Documents\\UF\\Fall 2024\\COP3502C\\PycharmProjects\\COP3502C\\Labs\\11-Module14LabGradeCalculator\\data\\submissions"
    while True:
        print("1. Student grade\n2. Assignment statistics\n3. Assignment graph")
        option = int(input("\nEnter your selection: "))
        if option == 1:
            student_name = input("What is the student's name: ")
            submissions = []
            students_info = {}
            student_id = ""
            assignment_code = ""
            student_code = ""
            grade_percentage = ""
            points_earned = 0
            total_points = 0
            max_points = 0
            with open("data/students.txt", "r") as f:
                lines = f.readlines()
                students = []
                for line in lines:
                    students.append(line.strip())
                for student in students:
                    if student_name in student:
                        student_id = student[0:3]
                        students_info[student_name] = student_id

            submissions_check = []
            for files in os.listdir("data/submissions"):
                submissions_file = os.path.join(file_path, files)
                with open(submissions_file, "r") as f:
                    submissions = f.readline().split("|")
                    submissions_check.append(submissions)
                    student_code = submissions[0]
                    assignment_code = submissions[1]
                    grade_percentage = submissions[2]
                if student_code == student_id:
                    with open("data/assignments.txt", "r") as f:
                        lines = []
                        for line in f.readlines():
                            lines.append(line.strip())
                        for i in range(len(lines)):
                            if lines[i] == assignment_code:
                                max_points = int(lines[i+1])
                                total_points += int(lines[i+1])
                                points_earned += (int(grade_percentage) / 100) * int(max_points)
            if student_name not in submissions_check:
                print("Student not found")
                break
            print(f"{round((points_earned/total_points) * 100)}%")

        elif option == 2:
            min_grade = 0
            max_grade = 0
            average_grade = 0
            assignment_code = ""
            percentages = []
            assignment = input("What is the assignment name: ")
            with open("data/assignments.txt", "r") as f:
                lines = []
                for line in f.readlines():
                    lines.append(line.strip())
                for i in range(len(lines)):
                    if lines[i] == assignment:
                        assignment_code = lines[i+1]
            submissions_check = []
            for files in os.listdir("data/submissions"):
                submissions_file = os.path.join(file_path, files)
                with open(submissions_file, "r") as f:
                    submissions = f.readline().split("|")
                    submissions_check.append(submissions)
                    if submissions[1] == assignment_code:
                        percentages.append(int(submissions[2]))
            if assignment_code not in submissions_check:
                print("Assignment not found")
                break
            min_grade = int(min(percentages))
            max_grade = int(max(percentages))
            average_grade = int(sum(percentages) / len(percentages))
            print(f"Min: {min_grade}%\nAvg: {average_grade}%\nMax: {max_grade}%")
        else:
            assignment_code = ""
            percentages = []
            submissions_check = []
            assignment = input("What is the assignment name: ")
            with open("data/assignments.txt", "r") as f:
                lines = []
                for line in f.readlines():
                    lines.append(line.strip())
                for i in range(len(lines)):
                    if lines[i] == assignment:
                        assignment_code = lines[i + 1]
            for files in os.listdir("data/submissions"):
                submissions_file = os.path.join(file_path, files)
                with open(submissions_file, "r") as f:
                    submissions = f.readline().split("|")
                    submissions_check.append(submissions)
                    if submissions[1] == assignment_code:
                        percentages.append(int(submissions[2]))
            plt.hist(percentages, bins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
            plt.show()
            if assignment_code not in submissions_check:
                print("Assignment not found")
                break
if __name__ == "__main__":
    main()









