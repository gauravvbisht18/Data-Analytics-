import streamlit as st

def calculate_bmi(weight_kg, height_cm):
    # Convert height to meters
    height_m = height_cm / 100.0

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    st.title("BMI Calculator")

    # Input fields
    weight_kg = st.number_input("Enter your weight (in kilograms)", min_value=0.0)
    height_cm = st.number_input("Enter your height (in centimeters)", min_value=0.0)

    if st.button("Calculate BMI"):
        bmi_result = calculate_bmi(weight_kg, height_cm)
        st.write(f"Your BMI: {bmi_result:.2f}")

        # Interpretation
        if bmi_result < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi_result < 24.9:
            st.success("Normal weight")
        elif 25.0 <= bmi_result < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")

if __name__ == "__main__":
    main()
