import pandas as pd

# Load crime statistics dataset
crime_data = pd.read_csv("crime.csv")

# Label each area by crime intensity
crime_data["crime_level"] = crime_data["ViolentCrimesPerPop"].apply(
    lambda rate: "HighCrime" if rate >= 0.50 else "LowCrime"
)

# Compute mean unemployment by crime category
unemployment_means = crime_data.groupby("crime_level")["PctUnemployed"].mean()

# Display results in a readable format
print("Average Unemployment Rate:")
print("HighCrime:", unemployment_means["HighCrime"])
print("LowCrime:", unemployment_means["LowCrime"])
