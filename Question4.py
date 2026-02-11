import pandas as pd

# Read student data from CSV
students_df = pd.read_csv("student.csv")

# Select students who meet engagement criteria
engaged_students = students_df[
    (students_df["studytime"] >= 3) &
    (students_df["internet"] == 1) &
    (students_df["absences"] <= 5)
]

# Export the filtered dataset
engaged_students.to_csv("high_engagement.csv", index=False)

# Display summary statistics
total_students = len(engaged_students)
average_mark = engaged_students["grade"].mean()

print("Number of students:", total_students)
print("Average grade:", average_mark)
