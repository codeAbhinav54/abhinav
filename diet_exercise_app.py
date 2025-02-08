import streamlit as st

def calculate_bmi(weight, height):
    """Calculates BMI and assigns a health rating (1-10)."""
    bmi = weight / ((height / 100) ** 2)

    if bmi < 16:
        rating = 1  # Severe Underweight
    elif 16 <= bmi < 17:
        rating = 2  # Moderate Underweight
    elif 17 <= bmi < 18.5:
        rating = 3  # Mild Underweight
    elif 18.5 <= bmi < 25:
        rating = 7  # Normal Weight
    elif 25 <= bmi < 30:
        rating = 5  # Overweight
    elif 30 <= bmi < 35:
        rating = 3  # Obese Class 1
    elif 35 <= bmi < 40:
        rating = 2  # Obese Class 2
    else:
        rating = 1  # Obese Class 3 (Severe)

    return round(bmi, 2), rating

def calculate_calories(age, weight, height, activity_level, gender):
    """Calculates daily calorie requirement using Mifflin-St Jeor Equation."""
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

def suggest_exercise(bmi):
    """Suggests an exercise plan based on BMI."""
    exercise_plan = {
        "Underweight": ["Strength training (3-4x per week)", "Yoga and flexibility exercises", "Moderate cardio (15-20 mins/day)"],
        "Normal Weight": ["Strength training & cardio (30-45 mins/day)", "Cycling, jogging, or swimming"],
        "Overweight": ["Low-impact cardio (walking, cycling)", "Strength training (2-3x per week)", "HIIT workouts"],
        "Obese": ["Brisk walking (30-40 mins/day)", "Water aerobics", "Bodyweight exercises"]
    }

    if bmi < 18.5:
        return exercise_plan["Underweight"]
    elif 18.5 <= bmi < 25:
        return exercise_plan["Normal Weight"]
    elif 25 <= bmi < 30:
        return exercise_plan["Overweight"]
    else:
        return exercise_plan["Obese"]

# Streamlit UI
st.title("💪 Balanced Diet & Exercise Planner")

age = st.number_input("Enter your age:", min_value=10, max_value=100, value=16)
weight = st.number_input("Enter your weight (kg):", min_value=20.0, max_value=200.0, value=72.0)
height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=180.0)
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
gender = st.radio("Select your gender:", ["Male", "Female"])

if st.button("Calculate"):
    bmi, rating = calculate_bmi(weight, height)
    daily_calories = calculate_calories(age, weight, height, activity_level, gender)
    exercise_plan = suggest_exercise(bmi)

    st.subheader("📊 Results")
    st.write(f"**BMI:** {bmi} | **Health Rating:** {rating}/10")
    st.write(f"🔥 **Daily Calorie Requirement:** {daily_calories} kcal")

    st.subheader("🏋️ Recommended Exercise Plan")
    for exercise in exercise_plan:
        st.write(f"✅ {exercise}")
