import datetime
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 16:
        category = "Severely Underweight"
    elif 16 <= bmi < 17:
        category = "Moderately Underweight"
    elif 17 <= bmi < 18.5:
        category = "Mildly Underweight"
    elif 18.5 <= bmi < 25:
        category = "Healthy Weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 30 <= bmi < 35:
        category = "Obese (Class 1)"
    elif 35 <= bmi < 40:
        category = "Obese (Class 2)"
    else:
        category = "Severely Obese"
    
    return round(bmi, 2), category

# Function to calculate daily calorie requirement
def calculate_calories(age, weight, height, activity_level, gender):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    activity_multipliers = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9
    }
    
    return int(bmr * activity_multipliers.get(activity_level, 1.2))

# Function to determine macronutrient breakdown
def macronutrient_distribution(calories):
    protein = int(0.3 * calories / 4)
    carbs = int(0.5 * calories / 4)
    fats = int(0.2 * calories / 9)
    return protein, carbs, fats

# Function to suggest exercises based on BMI
def suggest_exercise(bmi):
    if bmi < 18.5:
        return ["Strength training (3-4x per week)", "Yoga for flexibility", "High-calorie diet"]
    elif 18.5 <= bmi < 25:
        return ["Cardio & Strength mix (30-45 mins/day)", "Cycling, jogging, or swimming"]
    elif 25 <= bmi < 30:
        return ["Low-impact cardio (walking, cycling)", "Strength training (2-3x per week)", "HIIT workouts"]
    else:
        return ["Brisk walking (30-40 mins/day)", "Water aerobics", "Bodyweight exercises"]

# Function to give diet suggestions based on BMI category
def suggest_diet(category):
    diets = {
        "Severely Underweight": "Increase calorie intake with protein-rich foods, nuts, dairy, and healthy fats.",
        "Moderately Underweight": "Focus on high-protein meals and complex carbs with good fats.",
        "Mildly Underweight": "Eat nutrient-dense foods like lean meat, whole grains, and dairy.",
        "Healthy Weight": "Maintain balanced meals with proteins, carbs, and essential fats.",
        "Overweight": "Reduce processed foods and include more fiber and lean proteins.",
        "Obese (Class 1)": "Limit sugars, increase fiber, and maintain portion control.",
        "Obese (Class 2)": "Follow a calorie-deficit diet with whole foods.",
        "Severely Obese": "Consider medical consultation for a structured weight loss plan."
    }
    
    return diets.get(category, "Maintain a well-balanced diet.")

# Function to calculate recommended daily water intake
def calculate_water_intake(weight):
    return round(weight * 0.033, 2)

# === User Input Section ===
st.title("🥗 Balanced Diet & Exercise Planner 🏋️")
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
weight = st.number_input("Enter your weight (kg):", min_value=10.0, max_value=300.0, value=70.0)
height = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, value=170.0)
activity_level = st.selectbox("Enter your activity level:", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
gender = st.radio("Enter your gender:", ["Male", "Female"])

# === Processing User Inputs ===
bmi, category = calculate_bmi(weight, height)
daily_calories = calculate_calories(age, weight, height, activity_level, gender)
protein, carbs, fats = macronutrient_distribution(daily_calories)
exercise_plan = suggest_exercise(bmi)
diet_recommendation = suggest_diet(category)
water_intake = calculate_water_intake(weight)

# === Displaying Results ===
st.subheader("📊 Health Analysis")
st.write(f"**BMI:** {bmi} ({category})")
st.write(f"🔥 **Daily Calorie Requirement:** {daily_calories} kcal")

st.subheader("💧 Hydration Recommendation")
st.write(f"You should drink approximately **{water_intake}L** of water daily.")

st.subheader("🍽 Macronutrient Breakdown")
st.write(f"🥩 **Protein:** {protein}g | 🍞 **Carbs:** {carbs}g | 🥑 **Fats:** {fats}g")

st.subheader("🥦 Personalized Diet Suggestion")
st.write(diet_recommendation)

st.subheader("🏋️ Recommended Exercise Plan")
for exercise in exercise_plan:
    st.write(f"✅ {exercise}")

# === BMI Trend Graph ===
st.subheader("📈 BMI Trend Over Time")
# Example data (Replace with actual tracking data)
data = {
    "Date": pd.date_range(start="2023-01-01", periods=5, freq="6M"),
    "BMI": [22.1, 22.3, 22.7, 23.0, 23.4]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.plot(df["Date"], df["BMI"], marker="o", linestyle="-", color="b", label="BMI Trend")
ax.set_title("BMI Trend Over Time", fontsize=14)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("BMI", fontsize=12)
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)
