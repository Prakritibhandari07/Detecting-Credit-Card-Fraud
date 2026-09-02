import streamlit as st
import requests
import numpy as np

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳"
)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter the 30 transaction features to check whether the transaction is legitimate or fraudulent.")

API_URL = "https://detecting-credit-card-fraud.onrender.com/predict"

input_text = st.text_area(
    "Enter 30 feature values separated by commas",
    placeholder="Example: -1.3598,-0.0727,2.5363,..."
)

if st.button("🔍 Predict"):

    if not input_text.strip():
        st.warning("Please enter the feature values.")
    else:
        try:
            values = [
                float(x.strip())
                for x in input_text.split(",")
                if x.strip()
            ]

            if len(values) != 30:
                st.error(
                    f"Please enter exactly 30 feature values. "
                    f"You entered {len(values)}."
                )
            else:
                with st.spinner("Analyzing transaction..."):
                    response = requests.post(
                        API_URL,
                        json={"features": values},
                        timeout=60
                    )

                if response.status_code == 200:
                    result = response.json()

                    if result["prediction"] == 0:
                        st.success("✅ Legitimate Transaction")
                    else:
                        st.error("🚨 Fraudulent Transaction")

                    st.write(
                        f"Fraud Probability: "
                        f"**{result['fraud_probability'] * 100:.2f}%**"
                    )

                else:
                    st.error(
                        f"API Error: {response.status_code}"
                    )

        except ValueError:
            st.error("Please enter only numeric values separated by commas.")

        except requests.exceptions.Timeout:
            st.error(
                "The API is taking too long to respond. "
                "The Render free service may be waking up."
            )

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the API: {e}")

