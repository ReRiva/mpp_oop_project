# Importing the CSV module to read the CSV file
import csv

# Importing the file containing the Classes and functions to calculate the student statistics. 
from python_oop_statscalculation import StatisticsCalculator


# Student class containing the students data received by input from user or by file

class Student:
    def __init__(self, name, modules, scores):
        self.name = name
        self.modules = modules
        self.scores = scores
    def __repr__(self):
        return f' Name: {self.name}, Modules: {self.modules}, Score: {self.scores}'



# Ckass containing both function to receive the student data

class DataInput:


    # Reading the data from a file and checking from missing or incorrect values
    # For each student it creates a instance of the student class with their scores, modules and name

    def read_from_file():
        with open('MPPSample.csv') as file:
        #with open('MPPSample-scores.csv') as file:
            students = csv.reader(file)
            
            # Escaping the header
            a = next(students)
            # List of modules names
            grades_name = a[1:]
            for row in students:
                studentname = row[0]
                
                # Error handling for empty student name
                if studentname.isspace():
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
                StatisticsCalculator.calculate_student_stats(student.name, student.modules, student.scores)

        



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
                StatisticsCalculator.calculate_student_stats(student.name, student.modules, student.scores)


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
#print(Student)