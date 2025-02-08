import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 16:
        rating = 1  # Severe Underweight
        category = "Severely Underweight"
    elif 16 <= bmi < 17:
        rating = 2  # Moderate Underweight
        category = "Moderately Underweight"
    elif 17 <= bmi < 18.5:
        rating = 3  # Mild Underweight
        category = "Mildly Underweight"
    elif 18.5 <= bmi < 25:
        rating = 8  # Normal Weight
        category = "Healthy Weight"
    elif 25 <= bmi < 30:
        rating = 5  # Overweight
        category = "Overweight"
    elif 30 <= bmi < 35:
        rating = 3  # Obese Class 1
        category = "Obese (Class 1)"
    elif 35 <= bmi < 40:
        rating = 2  # Obese Class 2
        category = "Obese (Class 2)"
    else:
        rating = 1  # Obese Class 3 (Severe)
        category = "Severely Obese"
    return round(bmi, 2), rating, category

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

def macronutrient_distribution(calories):
    protein = int(0.3 * calories / 4)  # 30% Protein (4 kcal/g)
    carbs = int(0.5 * calories / 4)  # 50% Carbs (4 kcal/g)
    fats = int(0.2 * calories / 9)  # 20% Fats (9 kcal/g)
    return protein, carbs, fats

def suggest_exercise(bmi):
    plans = {
        "Underweight": ["Strength training (3-4x per week)", "Yoga for flexibility", "High-calorie diet"],
        "Healthy Weight": ["Cardio & Strength mix (30-45 mins/day)", "Cycling, jogging, or swimming"],
        "Overweight": ["Low-impact cardio (walking, cycling)", "Strength training (2-3x per week)", "HIIT workouts"],
        "Obese": ["Brisk walking (30-40 mins/day)", "Water aerobics", "Bodyweight exercises"]
    }
    if bmi < 18.5:
        return plans["Underweight"]
    elif 18.5 <= bmi < 25:
        return plans["Healthy Weight"]
    elif 25 <= bmi < 30:
        return plans["Overweight"]
    else:
        return plans["Obese"]

def suggest_diet(bmi_category):
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
    return diets.get(bmi_category, "Maintain a well-balanced diet.")

# Streamlit UI
st.title("🥗 Balanced Diet & Exercise Planner")

age = st.number_input("Enter your age:", min_value=10, max_value=100, value=16)
weight = st.number_input("Enter your weight (kg):", min_value=20.0, max_value=200.0, value=72.0)
height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=180.0)
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
gender = st.radio("Select your gender:", ["Male", "Female"])

if st.button("Calculate"):
    bmi, rating, category = calculate_bmi(weight, height)
    daily_calories = calculate_calories(age, weight, height, activity_level, gender)
    protein, carbs, fats = macronutrient_distribution(daily_calories)
    exercise_plan = suggest_exercise(bmi)
    diet_recommendation = suggest_diet(category)

    st.subheader("📊 Health Analysis")
    st.write(f"**BMI:** {bmi} ({category}) | **Health Rating:** {rating}/10")
    st.write(f"🔥 **Daily Calorie Requirement:** {daily_calories} kcal")
    
    st.subheader("🍽 Macronutrient Breakdown")
    st.write(f"🥩 **Protein:** {protein}g | 🍞 **Carbs:** {carbs}g | 🥑 **Fats:** {fats}g")
    
    st.subheader("🥦 Personalized Diet Suggestion")
    st.write(f"{diet_recommendation}")
    
    st.subheader("🏋️ Recommended Exercise Plan")
    for exercise in exercise_plan:
        st.write(f"✅ {exercise}")
