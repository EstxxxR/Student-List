import csv
import re

def add_info():
    StudentID = input("Enter student ID: ")
    EnglishName = input("Enter student name in English: ")
    ChineseName = input("Enter student name in Chinese: ")
    MathGrade = int(input("Enter Math grade: "))
    EnglishGrade = int(input("Enter English grade: "))
    TotalScore = MathGrade + EnglishGrade
    return [StudentID, EnglishName, ChineseName, MathGrade, EnglishGrade, TotalScore]

def save_info(student_info):
    with open("students.csv", mode = "a", encoding = "utf-8", newline = "") as all_info:
        writer = csv.writer(all_info)
        writer.writerow(student_info)

def read_info():
    with open("students.csv", mode = "r", encoding = "utf-8") as all_info:
        reader = csv.reader(all_info)
        for row in reader:
            print(row)

def search():
    search_str = input("Enter student ID or name: ")
    with open("students.csv", mode = "r", encoding = "utf-8") as all_info:
        reader = csv.reader(all_info)
        for row in reader:
            if re.search(search_str, row[0], re.IGNORECASE) or re.search(search_str, row[1], re.IGNORECASE):
                print(row)

def modification():
    search_str = input("Enter student ID or English Name: ")
    with open("students.csv", mode = "r", encoding = "utf-8") as all_info:
        reader = csv.reader(all_info)
        rows = list(reader)
        for i, row in enumerate(rows):
            if re.search(search_str, row[0], re.IGNORECASE) or re.search(search_str, row[1], re.IGNORECASE):
                print(row)
                StudentID = input("Enter student ID: ")
                EnglishName = input("Enter student name in English: ")
                ChineseName = input("Enter student name in Chinese: ")
                MathGrade = int(input("Enter math grade: "))
                EnglishGrade = int(input("Enter English grade: "))
                TotalScore = MathGrade + EnglishGrade
                rows[i] = [StudentID, EnglishName, ChineseName, MathGrade, EnglishGrade, TotalScore]
                with open("students.csv", mode="w", newline="", encoding = "utf-8") as all_info:
                    writer = csv.writer(all_info)
                    writer.writerows(rows)
                break
        else:
            print("Student not found")

def delete():
    search_str = input("Enter student ID or name: ")
    with open("students.csv", mode = "r", encoding = "utf-8") as all_info:
        reader = csv.reader(all_info)
        rows = list(reader)
        for i, row in enumerate(rows):
            if re.search(search_str, row[0], re.IGNORECASE) or re.search(search_str, row[1], re.IGNORECASE):
                print(row)
                rows.pop(i)
                with open("students.csv", mode="w", newline="", encoding = "utf-8") as all_info:
                    writer = csv.writer(all_info)
                    writer.writerows(rows)
                break
        else:
            print("Student not found")

def sort():
    with open("students.csv", mode="r", encoding="utf-8") as all_info:
        reader = csv.reader(all_info)
        rows = list(reader)
    
    n = len(rows)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(rows[j][5]) < int(rows[j + 1][5]):
                rows[j], rows[j + 1] = rows[j + 1], rows[j]
    
    for row in rows:
        print(row)

while True:
    print("1. Input and store student information")
    print("2. Print all students’ information")
    print("3. Modify student’s information")
    print("4. Delete student information")
    print("5. Sort by student grades")
    print("6. Search for student information")
    print("7. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_info = add_info()
        save_info(student_info)
    elif choice == "2":
        read_info()
    elif choice == "3":
        modification()
    elif choice == "4":
        delete()
    elif choice == "5":
        sort()
    elif choice == "6":
        search()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")