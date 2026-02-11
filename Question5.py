import pandas as pd

# Import the student dataset
student_data = pd.read_csv("student.csv")

# Assign each student to a performance category
def assign_band(score):
    if score <= 9:
        return "Low"
    elif score <= 14:
        return "Medium"
    else:
        return "High"

student_data["grade_band"] = student_data["grade"].apply(assign_band)

# Build a summary table by grade category
band_summary = (
    student_data
    .groupby("grade_band")
    .agg(
        student_count=("grade", "count"),
        mean_absences=("absences", "mean"),
        internet_access_rate=("internet", "mean")
    )
)

# Convert internet access rate to a percentage
band_summary["internet_access_rate"] = band_summary["internet_access_rate"] * 100

# Save the results
band_summary.to_csv("student_bands.csv")

# Output the table
print(band_summary)
