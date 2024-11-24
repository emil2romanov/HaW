import pandas as pd

# Mock health data
data = {
    "user_id": [1, 2, 3, 4, 5],
    "age": [25, 34, 45, 52, 60],
    "bmi": [22.5, 27.8, 31.0, 29.5, 33.2],  # Body Mass Index
    "steps_per_day": [12000, 8000, 4000, 3000, 2000],
    "sleep_hours": [7, 6, 5, 4.5, 6],
    "heart_rate": [65, 78, 85, 90, 95],  # Resting heart rate
}

# Create a DataFrame
df = pd.DataFrame(data)

# Analysis Criteria
def analyze_user(row):
    risk_factors = []

    # Age risk
    if row["age"] > 50:
        risk_factors.append("Age > 50")
    
    # BMI risk
    if row["bmi"] >= 30:
        risk_factors.append("BMI >= 30")
    
    # Low activity level
    if row["steps_per_day"] < 5000:
        risk_factors.append("Low activity (<5000 steps/day)")
    
    # Low sleep
    if row["sleep_hours"] < 6:
        risk_factors.append("Sleep < 6 hours")
    
    # High resting heart rate
    if row["heart_rate"] > 85:
        risk_factors.append("High resting heart rate (>85 bpm)")
    
    # Flagging users for health insurance review
    flagged = len(risk_factors) >= 3  # Flag if 3 or more risk factors
    
    return {
        "risk_factors": ", ".join(risk_factors),
        "flagged": flagged
    }

# Apply analysis to each user
df_analysis = df.apply(analyze_user, axis=1, result_type="expand")
df = pd.concat([df, df_analysis], axis=1)

# Display flagged users
flagged_users = df[df["flagged"]]

# Output Results
print("User Profiles and Risk Analysis:")
print(df)

print("\nFlagged Users for Health Insurance Review:")
print(flagged_users)

# Save results to an Excel file
df.to_excel("health_insurance_analysis.xlsx", index=False)




