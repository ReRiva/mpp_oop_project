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



# Reading from file seems ok too
#  

def read_from_file():
    with open('MPPSample.csv') as file:
        students = csv.reader(file)
    
        # Escaping the header
        a = next(students)
        # List of modules names
        grades_name = a[1:]
        for row in students:
            studentname = row[0]
            #Converting the Grades from string to Int
            student_grades = list(map(int, row[1:len(row)]))
            student_stats(studentname, student_grades, grades_name)
           
            
        
#### OK ######


def student_stats(studentname, student_grades, grades_name):
     #Function to calculate the students statistics, such as GAP, Lowest grade, score, Grade, etc
     #Lowest Score
     lowest_score = min(student_grades)
     lowest_grade  = grades_name[(student_grades.index(lowest_score))]
     
     #Highest Score
     highest_score = max(student_grades)
     highest_grade  = grades_name[(student_grades.index(highest_score))]
     
     # Getting the Individual GPA per Module and calculating the average GPA 
     students_gpas= []
     for grades in student_grades:
         letter_grade, individual_gpa = calculate_grade(grades)
         students_gpas.append(individual_gpa)

     student_gpa = round(float(sum(students_gpas)/len(students_gpas)), 2)
     
     
     # All the diciplines have the same weight. Checking if ther if a value over 100% in the file.  
     average_score = int(sum(student_grades)/len(student_grades))
     if average_score > 100:
         print("Please check your file.", studentname, "grades must be between 0 and 100")
         print("******** Exiting program*******")
         #break
     
     
     # Median Value  - https://www.w3schools.com/python/ref_stat_median.asp#:~:text=median()%20method%20calculates%20the,in%20a%20set%20of%20data.
     median = stat.median(student_grades)
     
     # Standard Deviation
     stdeviation = round(np.std(student_grades),2)


     # Finding the how far their gpa is from the nearest high tier.
     
     gpa_list = [0, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2]

     ############################### Help from internet
     def find_next_higher_gpa(gpa_list, gpa):
         gpa_list = [0, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2]
         next_higher = min([x for x in gpa_list if x >= gpa])
         return next_higher

     nearest_high_gpa = round(find_next_higher_gpa(gpa_list, student_gpa) - student_gpa, 2)
         

     # Printing the result with the student information
     print("-------------------------------")
     print(studentname, "GPA is:", student_gpa, ",their highest scoring Module is:", highest_grade, ",their lowest scoring Module is:", lowest_grade, ",their score standard deviation is " ,stdeviation, ",the median value of their score is ", median,  ",how far from the next gpa tier", nearest_high_gpa, "the letter grade is:", letter_grade, "\n" )

        



#########################

def input_values():
    students = {}

    while True:
        name = input("Enter student name (or 'quit' to exit): ")
        
        if name.lower() == "quit":
            break
        
        module = input("Enter student module: ")
        score = float(input("Enter student score: "))
        
        
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
            print("Invalid choice. Please enter a valid option.")

# Run the main menu
program_menu()



##### Overall ok, check error handling and do the C version and OOP on