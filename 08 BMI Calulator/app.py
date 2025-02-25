import streamlit as st

# Title of the app
st.title("BMI Calculator By Ahmed Ali")

# Input fields for weight and height (Height in cm)
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height_cm = st.number_input("Enter your height (cm):", min_value=10.0, step=0.1)

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    if height_cm > 0:
        height_m = height_cm / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # Interpret BMI result
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")
