import csv
import statistics as stat
import numpy as np

#Function to define the Grade and GPA bands
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
        gpa = 3.2
        return letter_grade, gpa
    elif score >= 60:
        letter_grade = "C+"
        gpa = 3.0
        return letter_grade, gpa
    elif score >= 55:
        letter_grade = "C"
        gpa = 2.8
        return letter_grade, gpa
    elif score >= 50:
        letter_grade = "C-"
        gpa = 2.6
        return letter_grade, gpa
    elif score >= 45:
        letter_grade = "D+"
        gpa = 2.4
        return letter_grade, gpa
    elif score >= 40:
        letter_grade = "D"
        gpa = 2.2
        return letter_grade, gpa
    elif score >= 0 and score < 40:
        letter_grade = "F"
        gpa = 0
        return letter_grade, gpa
    else:
        print("Please check your file. Student grades must be between 0 and 100")


        
#Function to calculate the students statistics, such as GPA, Lowest grade, score, Grade, etc


def student_stats(studentname, student_grades, grades_name):
     
     #Lowest Score
     lowest_score = min(student_grades)
     lowest_grade  = grades_name[(student_grades.index(lowest_score))]
     
     #Highest Score
     highest_score = max(student_grades)
     highest_grade  = grades_name[(student_grades.index(highest_score))]
    
     # Letter Grade
     average_score = int(sum(student_grades) / len(student_grades))
     letter_grade, _ = calculate_grade(average_score)


     # Getting the Individual GPA per Module and calculating the average GPA 
     students_gpas= []
     for grades in student_grades:
         _, individual_gpa = calculate_grade(grades)
         students_gpas.append(individual_gpa)

     student_gpa = round(float(sum(students_gpas)/len(students_gpas)), 2)
     

     
     # Median Value  - https://www.w3schools.com/python/ref_stat_median.asp#:~:text=median()%20method%20calculates%20the,in%20a%20set%20of%20data.
     median = stat.median(student_grades)
     
     # Standard Deviation
     stdeviation = round(np.std(student_grades),2)


     # Finding the how far their gpa is from the nearest high tier.
     
     gpa_list = [0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2]

     def find_next_higher_gpa(gpa_list, gpa):
         gpa_list = [0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2]
         next_higher = min([x for x in gpa_list if x >= gpa])
         return next_higher

     nearest_high_gpa = round(find_next_higher_gpa(gpa_list, student_gpa) - student_gpa, 2)
         

     # Printing the result with the student information
     print("-------------------------------")
     print("Student name: ", studentname,"\n" 
              "GPA:", student_gpa, "\n" 
              "Highest Scoring Module:", highest_grade,"\n"
              "Lowest Scoring Module:", lowest_grade,"\n"
              "Score Standard Deviation: ", stdeviation,"\n"
              "Score Median Value:", median,"\n" 
              "Student is ",nearest_high_gpa,"points away from the next GPA tier","\n"
              "Letter Grade is:", letter_grade, "\n")
        

###########


# Reading from file.

def read_from_file():
    
    
    with open('MPPSample.csv') as file:
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
                program_menu()
            
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
                program_menu()

            # Error handling for modules without names or containing empty strings
            if any(not module_name or module_name.isspace() for module_name in grades_name):
                print(f"Error: Some modules have blank names.")
                program_menu()

            student_stats(studentname, student_grades, grades_name)
            
            











#########################

def input_values():
    students = {}

    while True:
        
        while True:
            try:
                name = input("Enter student name (or 'quit' to exit): ")
                if name == "":
                    raise ValueError("Invalid Student name. Please enter a valid student name.")
                break  # Break out of the loop if the input is valid
            except ValueError as e:
                print(e)


        if name.lower() == "quit":
            break
        
        ### Checking if Module name is not blank. 

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

        # We are creating these lists to pass it to the function
        for name in students:
            grades_name = students[name]["modules"]
            student_grades = students[name]["scores"]
            studentname = name
            student_stats(studentname, student_grades, grades_name)





def program_menu():
    while True:
        print("------ Main Menu ------")
        print("1. Press ''1'' to read the student information from a file")
        print("2. Press ''2'' to enter the student information manually")
        print("3. Press ''3'' to Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            read_from_file()
        elif choice == "2":
            input_values()
        elif choice == "3":
            print("Quitting the program...")
            break
        else:
            print("\n" "Invalid choice. Please enter a valid option." "\n")

# Run the main menu
program_menu()

