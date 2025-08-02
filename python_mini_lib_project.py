#Creating a mini python library project using numpy, pandas, matplotlib and seaborn.
#Topic : creatibg nd analysing and visualizing a dataset Student performance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(34)
marks = np.random.randint(50, 99, size=(10, 4))

print(marks)
names = [f"Student{i}" for i in range(1, 11)]
subjects = ['Maths', 'Science', 'English', 'Social']
df = pd.DataFrame(marks, index=names, columns=subjects)
print(df)
#avg_marks_of_each_student = df.mean(axis=1)
#print(avg_marks_of_each_student)3
#total_marks_of_each_student = df.sum(axis=1)
#print(total_marks_of_each_student)
#subject_wies_topper = df.idxmax(axis=0)
#print(subject_wies_topper)
#subject_weakest = df.idxmin(axis=0)
#print(subject_weakest)
df['Total'] = df.sum(axis=1)
#topper = df['Total'].idxmax()
#print( "Topper of the class is ",topper)
#weakest = df['Total'].idxmin()
#print("Weakest student of the class is ",weakest)
#student_sorted_by_marks = df.sort_values(by='Total', ascending=False)
#print(student_sorted_by_marks)
#less_Scorers = df[df[subjects] <80].count()
#print(less_Scorers)
#sns.barplot(x=df.index, y=df['Total'], palette='Reds')
#plt.title("Total marks of each student")
#plt.xlabel("Students")
#plt.ylabel("Total marks")
#plt.tight_layout()
#plt.savefig("student_total_marks.png")

#print( "Plot saved as 'student_total_marks.png'. Click the file to view it.")
#plt.show()
#sns.boxplot(data=df[subjects],palette="Set3")
#plt.title("Box plot of marks")
#plt.xlabel("Subjects")
#plt.ylabel("Marks")
#plt.savefig("box_plot.png")
#print("Plot saved as 'box_plot.png'. Click the file to view it.")
#plt.show()
#plt.hist(df['Total'],color='blue',edgecolor='black')
#plt.title("Histogram of total marks")
#plt.xlabel("Total marks")
#plt.ylabel("Frequency")
plt.savefig("hist_plot.png")
print("Plot saved as 'hist_plot.png'. Click the file to view it.")
#plt.show()
sns.heatmap(df[subjects], annot=True, cmap='coolwarm')
plt.title("Heatmap of marks")
plt.savefig("heatmap_plot.png")
print("Plot saved as 'heatmap_plot.png'. Click the file to view it.")
plt.show()