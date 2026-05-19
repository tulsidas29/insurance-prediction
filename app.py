import streamlit as st
import pandas as pd
import joblib

model = joblib.load("insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")

age = st.number_input("Age", 18, 100)

sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.number_input(
    "BMI",
    10.0,
    50.0
)

children = st.number_input(
    "Children",
    0,
    10
)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.selectbox(
    "Region",
    [
        "northwest",
        "northeast",
        "southwest",
        "southeast"
    ]
)

sex = 0 if sex == "Male" else 1

smoker = 1 if smoker == "Yes" else 0

region_northeast = 1 if region == "northeast" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

if bmi < 18.5:
    bmi_category = 0

elif bmi < 25:
    bmi_category = 1

elif bmi < 30:
    bmi_category = 2

else:
    bmi_category = 3

input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region_northeast': [region_northeast],
    'region_northwest': [region_northwest],
    'region_southeast': [region_southeast],
    'region_southwest': [region_southwest],
    'bmi_category': [bmi_category]
})

if st.button("Predict Insurance Cost"):

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Insurance Cost: ${prediction[0]:,.2f}"
    )                                                                                                                                                                    region_southeast = 1 if region == "southeast" else 0
                                                                                                                                                                    region_southwest = 1 if region == "southwest" else 0

                                                                                                                                                                    # BMI Category
                                                                                                                                                                    if bmi < 18.5:
                                                                                                                                                                        bmi_category = 0

                                                                                                                                                                        elif bmi < 25:
                                                                                                                                                                            bmi_category = 1

                                                                                                                                                                            elif bmi < 30:
                                                                                                                                                                                bmi_category = 2

                                                                                                                                                                                else:
                                                                                                                                                                                    bmi_category = 3

                                                                                                                                                                                    # Input DataFrame
                                                                                                                                                                                    input_data = pd.DataFrame({
                                                                                                                                                                                        'age': [age],
                                                                                                                                                                                            'sex': [sex],
                                                                                                                                                                                                'bmi': [bmi],
                                                                                                                                                                                                    'children': [children],
                                                                                                                                                                                                        'smoker': [smoker],
                                                                                                                                                                                                            'region_northeast': [region_northeast],
                                                                                                                                                                                                                'region_northwest': [region_northwest],
                                                                                                                                                                                                                    'region_southeast': [region_southeast],
                                                                                                                                                                                                                        'region_southwest': [region_southwest],
                                                                                                                                                                                                                            'bmi_category': [bmi_category]
                                                                                                                                                                                                                            })

                                                                                                                                                                                                                            # Prediction
                                                                                                                                                                                                                            if st.button("Predict Insurance Cost"):

                                                                                                                                                                                                                                prediction = model.predict(input_data)

                                                                                                                                                                                                                                    st.success(
                                                                                                                                                                                                                                            f"Estimated Insurance Cost: ${prediction[0]:,.2f}"
                                                                                                                                                                                                                                                )

                                                                                                                                                                                                                                                    if prediction[0] < 10000:
                                                                                                                                                                                                                                                            st.info("Low Insurance Cost")

                                                                                                                                                                                                                                                                elif prediction[0] < 30000:
                                                                                                                                                                                                                                                                        st.warning("Medium Insurance Cost")

                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                    st.error("High Insurance Cost")
