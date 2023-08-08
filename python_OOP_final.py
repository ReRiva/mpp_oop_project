# Importing the CSV module to read the CSV file
import csv

# Importing the file containing the Classes and methods to calculate the student statistics. 
from python_statscalculation_final import StatisticsCalculator
import statistics as stat
import numpy as np

# Student class containing the students data received by input from user or by file

class Student:
    def __init__(self, name, modules, scores ):
        self.name = name
        self.modules = modules
        self.scores = scores

    def __repr__(self):
        return f"Student(name='{self.name}', modules={self.modules}, scores={self.scores})"


# Class containing the Students Statistics data and data inherited from the Student Class

class StudentStats(Student):    
    def __init__(self, name, modules, scores, lowest_grade, highest_grade, gpa, nearest_high_gpa, median, stdeviation, letter_grade, average_score):
        super().__init__(name, modules, scores)

        self.lowest_grade = lowest_grade
        self.highest_grade = highest_grade
        self.gpa = gpa
        self.nearest_high_gpa = nearest_high_gpa
        self.median = median
        self.stdeviation = stdeviation
        self.letter_grade = letter_grade
        self.average_score = average_score

    # Method to organize and call the methods responsible for the calculation of all students statistics
    # The methods tha do the calculation are on the file 

    def calculate_student_stats(self):    
        lowest_grade = StatisticsCalculator.calculate_lowest_grade(self.modules, self.scores)
        highest_grade = StatisticsCalculator.calculate_highest_grade(self.modules, self.scores)
        average_score = int(sum(self.scores) / len(self.scores))
        average_gpa = StatisticsCalculator.calculate_student_gpa(self.scores)
        nearest_high_gpa = StatisticsCalculator.calculate_nearest_high_gpa(average_gpa)
        median = stat.median(self.scores)
        stdeviation = round(np.std(self.scores), 2)
        letter_grade, _ = StatisticsCalculator.calculate_grade(average_score)
        return StudentStats(self.name, self.modules, self.scores, lowest_grade, highest_grade, average_gpa, nearest_high_gpa, median, stdeviation, letter_grade, average_score)
    

    def __repr__(self):
        return f"\nStudent name: {self.name}\n GPA: {self.gpa}\n Highest Scoring Module: {self.highest_grade}\n Lowest Scoring Module: {self.lowest_grade}\n Score Standard Deviation: {self.stdeviation}\n Score Median Value: {self.median}\n Student is {self.nearest_high_gpa} points away from the next GPA tier\n Letter Grade is: {self.letter_grade}\n"
        









# Class containing both function to receive the student data

class DataInput:


    # Reading the data from a file and checking from missing or incorrect values
    # For each student it creates a instance of the student class with their scores, modules and name

    def read_from_file():
        with open('MPPSample-nonames.csv') as file:
        #with open('MPPSample-scores.csv') as file:
        #with open('MPPSample-noModuleNames.csv') as file:
        #with open('MPPSample-missingStudentsNames.csv') as file:
            students = csv.reader(file)
            
            # Escaping the header
            a = next(students)
            # List of modules names
            grades_name = a[1:]
            for row in students:
                studentname = row[0]
                
                # Error handling for empty student name
                if not studentname or studentname.isspace():
                    print("Student name cannot be empty. Returning to Main Menu")
                    Menu.program_menu()
                
                # Error handling for converting grades from string to float and checking their validity
                try:
                    student_grades = [float(grade) for grade in row[1:]]

                    # Check if grades are within the valid range of 0 to 100
                    if any(grade < 0 or grade > 100 for grade in student_grades):
                        raise ValueError("Grades must be between 0 and 100.")

                    # Check if any grade is blank
                    if any(grade == "" for grade in student_grades):
                        raise ValueError("Grades cannot be blank.")
                    
                except ValueError as e:
                    print(f"Error with grades for {studentname}: {e}")
                    Menu.program_menu()

                # Error handling for modules without names or containing empty strings
                if any(not module_name or module_name.isspace() for module_name in grades_name):
                    print(f"Error: Some modules have blank names.")
                    Menu.program_menu()
                student = Student(studentname, grades_name, student_grades)
                student_stats = StudentStats.calculate_student_stats(student)
                print(repr(student_stats))


        



    # Taking live input from a user and checking the data being inputed
    # For each student it creates a instance of the student class with their scores, modules and name

    def input_values():
        students = {}

        ### Checking if the student name is not blank.

        while True:
            
            while True:
                try:
                    name = input("Enter student name (or 'quit' to exit): ")
                    if name == "":
                        raise ValueError("Invalid Student name. Please enter a valid student name.")
                    break
                except ValueError as e:
                    print(e)


            if name.lower() == "quit":
                break
            
            ### Checking if the module name is not blank. 

            while True:
                try:
                    module = input("Enter student module: ")
                    if module == "":
                        raise ValueError("Invalid Module name. Please enter a valid module name.")
                    break  # Break out of the loop if the input is valid
                except ValueError as e:
                    print(e)
            
            ### Checking if score is between 0 and 100. 
            
            while True:
                try:
                    score = float(input("Enter student score: "))
                    if score < 0 or score > 100:
                        raise ValueError("Invalid score. Score must be between 0 and 100.")
                    break  # Break out of the loop if the input is valid
                except ValueError as e:
                    print(e)
            

            # Check if student name already exists in the dictionary
            if name in students:
                # If the name exists, append the module and score to the existing lists
                students[name]["modules"].append(module)
                students[name]["scores"].append(score)
            else:
                # If the name doesn't exist, create a new dictionary entry with the module and score lists
                students[name] = {"modules": [module], "scores": [score]}


                #Creating a instance of the class Student and calling the functions to calculate the student statistics

            for name, data in students.items():
                student = Student(name, data["modules"], data["scores"])
                StudentStats.calculate_student_stats(student)
                student_stats = StudentStats.calculate_student_stats(student)
                print(repr(student_stats))


class Menu:

    # Program Menu

    def program_menu():
        while True:
            print("------ Main Menu ------")
            print("1. Press '1' to read the student information from a file")
            print("2. Press '2' to enter the student information manually")
            print("3. Press '3' to Quit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                DataInput.read_from_file()
            elif choice == "2":
                DataInput.input_values()
            elif choice == "3":
                print("Quitting the program...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Run the main menu
Menu.program_menu()
