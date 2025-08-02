import numpy as np

def take_user_input():
    students = int(input("Enter the number of students: "))
    subjects = int(input("Enter the number of subjects: "))
    print("Enter the marks row wise (one row one students ):")
    data=[]
    for _ in range(students):
        row = list(map(int, input().split()))
        if len(row)!= subjects:
            print("Invalid input. Please enter marks for all subjects.")
            return take_user_input
        else:
           data.append(row)
    marks = np.array(data)
    return marks

def display_data(marks):
   print("----marks matrix----")
   print(marks)
   total_per_student = np.sum(marks , axis=1)
   avg_per_student = np.mean(marks , axis=1)
   highest_in_each_subject = np.max(marks , axis=0)
   top_student= np.argmax(total_per_student)


   print("Total marks per student:", total_per_student)
   print("Average marks per student:", avg_per_student)
   print("Highest marks in each subject:", highest_in_each_subject)
   print(f"Top student is {top_student +1} with total {total_per_student[top_student]}")

marks_matrix = take_user_input()
display_data(marks_matrix)
