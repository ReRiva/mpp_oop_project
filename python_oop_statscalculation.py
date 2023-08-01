
import statistics as stat
import numpy as np

#Class holding a function that calculate the GPA and letter grade for each Module

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

    # individual functions to calculate each one of the requested students stats

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
        letter_grade, gpa = GradeCalculator.calculate_grade(average_score)

        print("-------------------------------")
        print("Student name: ", name,"\n" 
              "GPA:", student_gpa, "\n" 
              "Highest Scoring Module:", highest_grade,"\n"
              "Lowest Scoring Module:", lowest_grade,"\n"
              "Score Standard Deviation: ", stdeviation,"\n"
              "Score Median Value:", median,"\n" 
              "Student is ",nearest_high_gpa,"points away from the next GPA tier","\n"
              "Letter Grade is:", letter_grade, "\n")
        


