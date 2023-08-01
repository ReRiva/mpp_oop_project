#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

 struct Student{
    char name[100];
    char** modules;
    float* scores;
    int count;
};


calculate_grade(float score, const char** letter_grade, float* gpa) {
    if (score >= 90 && score <= 100) {
        *letter_grade = "A+";
        *gpa = 4.2;
        return *letter_grade, *gpa;
    } else if (score >= 85) {
        *letter_grade = "A";
        *gpa = 4.0;
        return *letter_grade, *gpa;
    } else if (score >= 80) {
        *letter_grade = "A-";
        *gpa = 3.8;
        return *letter_grade, *gpa;
    } else if (score >= 75) {
        *letter_grade = "B+";
        *gpa = 3.6;
        return *letter_grade, *gpa;;
    } else if (score >= 70) {
        *letter_grade = "B";
        *gpa = 3.4;
        return *letter_grade, *gpa;
    } else if (score >= 65) {
        *letter_grade = "B-";
        *gpa = 3.4;
        return *letter_grade, *gpa;
    } else if (score >= 60) {
        *letter_grade = "C+";
        *gpa = 3.2;
        return *letter_grade, *gpa;
    } else if (score >= 55) {
        *letter_grade = "C";
        *gpa = 3.0;
        return *letter_grade, *gpa;
    } else if (score >= 50) {
        *letter_grade = "C-";
        *gpa = 2.8;
        return *letter_grade, *gpa;
    } else if (score >= 45) {
        *letter_grade = "D+";
        *gpa = 2.6;
        return *letter_grade, *gpa;
    } else if (score >= 40) {
        *letter_grade = "D";
        *gpa = 2.4;
        return *letter_grade, *gpa;
    } else if (score >= 0 && score < 40) {
        *letter_grade = "F";
        *gpa = 0;
        return *letter_grade, *gpa;
    } else {
        printf("Please check your file. Student grades must be between 0 and 100\n");
    }
}




void student_stats(const char* studentname, float* student_grades, char** grades_name, int count, Student student) {
    


    // Lowest Score
    float lowest_score = student_grades[0];
    char* lowest_grade = grades_name[0];
    for (int i = 1; i < count; i++) {
        if (student_grades[i] < lowest_score) {
            lowest_score = student_grades[i];
            lowest_grade = grades_name[i];
        }
    }

    // Highest Score
    float highest_score = student_grades[0];
    char* highest_grade = grades_name[0];
    for (int i = 1; i < count; i++) {
        if (student_grades[i] > highest_score) {
            highest_score = student_grades[i];
            highest_grade = grades_name[i];
        }
    }

    // Getting the Individual GPA per Module and calculating the average GPA
    float student_gpas[student.count];
    for (int i = 0; i < student.count; i++) {
        const char* letter_grade;
        calculate_grade(student_grades[i], &letter_grade, &student_gpas[i]);
    }

    float student_gpa = 0.0;
    for (int i = 0; i < student.count; i++) {
        student_gpa += student_gpas[i];
    }
    student_gpa /= student.count;

    // All the disciplines have the same weight. Checking if there is a value over 100%
    float average_score = 0.0;
    for (int i = 0; i < student.count; i++) {
        average_score += student_grades[i];
    }
    average_score /= student.count;

    if (average_score > 100) {
        printf("Please check your file. %s grades must be between 0 and 100\n", studentname);
        printf("******** Exiting program*******\n");
        return;
    }

    // Median Value
    float median;
    if (student.count % 2 == 0) {
        median = (student_grades[student.count / 2 - 1] + student_grades[student.count / 2]) / 2.0;
    } else {
        median = student_grades[student.count / 2];
    }

    // Standard Deviation
    float stdeviation = 0.0;
    float mean = average_score;
    for (int i = 0; i < student.count; i++) {
        stdeviation += pow(student_grades[i] - mean, 2);
    }
    stdeviation = sqrt(stdeviation / student.count);

    // Finding how far their GPA is from the nearest high tier
    const float gpa_list[] = {0.0, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2};
    float nearest_high_gpa = gpa_list[0];
    for (int i = 1; i < sizeof(gpa_list) / sizeof(gpa_list[0]); i++) {
        if (gpa_list[i] >= student_gpa) {
            nearest_high_gpa = gpa_list[i];
            break;
        }
    }
    nearest_high_gpa -= student_gpa;

    // Printing the result with the student information
    printf("-------------------------------\n");
    printf("%s GPA is: %.2f, their highest scoring Module is: %s, their lowest scoring Module is: %s\n",
           studentname, student_gpa, highest_grade, lowest_grade);
    printf("Their score standard deviation is %.2f, the median value of their score is %.2f\n",
           stdeviation, median);
    printf("How far from the next GPA tier: %.2f\n", nearest_high_gpa);
}









void input_values() {
    
    Student students[100];

    int num_students = 0; // Number of students entered

    while (1) {
        char name[100];
        printf("Enter student name (or 'quit' to exit): ");
        scanf("%s", name);
        
        if (strcmp(name, "quit") == 0) {
            break;
        }

        char module[100];
        printf("Enter student module: ");
        scanf("%s", module);

        float score;
        printf("Enter student score: ");
        scanf("%f", &score);

        // Check if student name already exists in the array
        int existing_index = -1;
        for (int i = 0; i < num_students; i++) {
            if (strcmp(students[i].name, name) == 0) {
                existing_index = i;
                break;
            }
        }

        if (existing_index != -1) {
            // If the name exists, append the module and score to the existing lists
            int count = students[existing_index].count;
            students[existing_index].modules[count] = strdup(module);
            students[existing_index].scores[count] = score;
            students[existing_index].count++;
        } else {
            // If the name doesn't exist, create a new entry in the array
            strcpy(students[num_students].name, name);
            students[num_students].modules = (char**)malloc(sizeof(char*) * 100);
            students[num_students].scores = (float*)malloc(sizeof(float) * 100);
            students[num_students].modules[0] = strdup(module);
            students[num_students].scores[0] = score;
            students[num_students].count = 1;
            num_students++;
        }
    }

    // Process student statistics
    for (int i = 0; i < num_students; i++) {
        Student student = students[i];
        student_stats(student.name, student.scores, student.modules, student.count, student);
    }


}





//////// Set up the read from file funcction


void read_from_file() {
    
    Student students[100];

    int num_students = 0; // Number of students entered

    while (1) {
        char name[100];
        printf("Enter student name (or 'quit' to exit): ");
        scanf("%s", name);
        
        if (strcmp(name, "quit") == 0) {
            break;
        }

        char module[100];
        printf("Enter student module: ");
        scanf("%s", module);

        float score;
        printf("Enter student score: ");
        scanf("%f", &score);

        // Check if student name already exists in the array
        int existing_index = -1;
        for (int i = 0; i < num_students; i++) {
            if (strcmp(students[i].name, name) == 0) {
                existing_index = i;
                break;
            }
        }

        if (existing_index != -1) {
            // If the name exists, append the module and score to the existing lists
            int count = students[existing_index].count;
            students[existing_index].modules[count] = strdup(module);
            students[existing_index].scores[count] = score;
            students[existing_index].count++;
        } else {
            // If the name doesn't exist, create a new entry in the array
            strcpy(students[num_students].name, name);
            students[num_students].modules = (char**)malloc(sizeof(char*) * 100);
            students[num_students].scores = (float*)malloc(sizeof(float) * 100);
            students[num_students].modules[0] = strdup(module);
            students[num_students].scores[0] = score;
            students[num_students].count = 1;
            num_students++;
        }
    }

    // Process student statistics
    for (int i = 0; i < num_students; i++) {
        Student student = students[i];
        student_stats(student.name, student.scores, student.modules, student.count, student);
    }


}













////////////////////////////////////////////

void program_menu() {
    char choice[2];
    while (1) {
        printf("------ Main Menu ------\n");
        printf("1. Press '1' to read the student information from a file\n");
        printf("2. Press '2' to enter the student information manually\n");
        printf("3. Press '3' to Quit\n");

        printf("Enter your choice (1-3): ");
        scanf("%1s", choice);

        if (strcmp(choice, "1") == 0) {
            printf("1111111111");
        } else if (strcmp(choice, "2") == 0) {
            input_values();
        } else if (strcmp(choice, "3") == 0) {
            printf("Quitting the program...\n");
            break;
        } else {
            printf("Invalid choice. Please enter a valid option.\n");
        }
    }
}








int main() {
    program_menu();
    return 0;
}