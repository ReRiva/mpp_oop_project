import csv
import statistics as stat
import numpy as np

####### Need to make some adjustment to the code



class Student:
    def __init__(self, name, modules, scores):
        self.name = name
        self.modules = modules
        self.scores = scores







class GradeCalculator:
 
    def calculate_grade(score):
        if score >= 90 and score <=100:
            letter_grade = "A+"
            gpa = 4.2
            return letter_grade, gpa
        elif score >= 85:
            letter_grade = "A"
            gpa = 4.0
            return letter_grade, gpa
        elif score >= 80:
            letter_grade = "A-"
            gpa = 3.8
            return letter_grade, gpa
        elif score >= 75:
            letter_grade = "B+"
            gpa = 3.6
            return letter_grade, gpa
        elif score >= 70:
            letter_grade = "B"
            gpa = 3.4
            return letter_grade, gpa
        elif score >= 65:
            letter_grade = "B-"
            gpa = 3.4
            return letter_grade, gpa
        elif score >= 60:
            letter_grade = "C+"
            gpa = 3.2
            return letter_grade, gpa
        elif score >= 55:
            letter_grade = "C"
            gpa = 3.0
            return letter_grade, gpa
        elif score >= 50:
            letter_grade = "C-"
            gpa = 2.8
            return letter_grade, gpa
        elif score >= 45:
            letter_grade = "D+"
            gpa = 2.6
            return letter_grade, gpa
        elif score >= 40:
            letter_grade = "D"
            gpa = 2.4
            return letter_grade, gpa
        elif score >= 0 and score < 40:
            letter_grade = "F"
            gpa = 0
            return letter_grade, gpa
        else:
            print("Please check your file. Student grades must be between 0 and 100")



class StatisticsCalculator:

    def calculate_lowest_grade(modules, scores):
        lowest_score = min(scores)
        lowest_grade = modules[scores.index(lowest_score)]
        return lowest_grade

   
    def calculate_highest_grade(modules, scores):
        highest_score = max(scores)
        highest_grade = modules[scores.index(highest_score)]
        return highest_grade

    def calculate_student_gpa(scores):
        student_gpas = []
        for score in scores:
            letter_grade, individual_gpa = GradeCalculator.calculate_grade(score)
            student_gpas.append(individual_gpa)
        student_gpa = round(sum(student_gpas) / len(student_gpas), 2)
        return student_gpa

    
    def calculate_nearest_high_gpa(student_gpa):
        gpa_list = [0, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2]
        next_higher = min([x for x in gpa_list if x >= student_gpa])
        return round(next_higher - student_gpa, 2)

    
    def calculate_student_stats(name, modules, scores):
        lowest_grade = StatisticsCalculator.calculate_lowest_grade(modules, scores)
        highest_grade = StatisticsCalculator.calculate_highest_grade(modules, scores)
        student_gpa = StatisticsCalculator.calculate_student_gpa(scores)
        nearest_high_gpa = StatisticsCalculator.calculate_nearest_high_gpa(student_gpa)
        average_score = int(sum(scores) / len(scores))
        median = stat.median(scores)
        stdeviation = round(np.std(scores), 2)
        letter_grade, _ = GradeCalculator.calculate_grade(average_score)

        print("-------------------------------")
        print(name, "GPA is:", student_gpa, ",their highest scoring Module is:", highest_grade,
              ",their lowest scoring Module is:", lowest_grade, ",their score standard deviation is", stdeviation,
              ",the median value of their score is", median, ",how far from the next GPA tier",
              nearest_high_gpa, "the letter grade is:", letter_grade, "\n")





class Menu:

    def read_from_file():
        with open('MPPSample.csv') as file:
            students = csv.reader(file)
            header = next(students)  # Skipping the header
            modules = header[1:]  # List of module names

            for row in students:
                name = row[0]
                scores = list(map(int, row[1:]))
                student = Student(name, modules, scores)
                StatisticsCalculator.calculate_student_stats(student.name, student.modules, student.scores)

    def input_values():
        students = {}

        while True:
            name = input("Enter student name (or 'quit' to exit): ")

            if name.lower() == "quit":
                break

            module = input("Enter student module: ")
            score = float(input("Enter student score: "))

            if name in students:
                students[name]["modules"].append(module)
                students[name]["scores"].append(score)
            else:
                students[name] = {"modules": [module], "scores": [score]}

        for name, data in students.items():
            student = Student(name, data["modules"], data["scores"])
            StatisticsCalculator.calculate_student_stats(student.name, student.modules, student.scores)

    def program_menu():
        while True:
            print("------ Main Menu ------")
            print("1. Press '1' to read the student information from a file")
            print("2. Press '2' to enter the student information manually")
            print("3. Press '3' to Quit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                Menu.read_from_file()
            elif choice == "2":
                Menu.input_values()
            elif choice == "3":
                print("Quitting the program...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Run the main menu
Menu.program_menu()