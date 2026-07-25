import numpy as np
import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title(" Credit Card Fraud Detection Model")
st.write(
    "This model checks whether a credit card transaction is likely fraudulent, "
    "based on 30 features: **Time**, **V1–V28** (anonymized PCA components), and **Amount**."
)

# Sample buttons for easy demoing
col1, col2 = st.columns(2)
with col1:
    if st.button(" Try a legitimate transaction"):
        st.session_state.txn_input = "0,-1.36,-0.07,2.54,1.38,-0.34,0.46,0.24,0.10,0.36,0.09,-0.55,-0.62,-0.99,-0.31,1.47,-0.47,0.21,0.03,0.40,0.25,-0.02,0.28,-0.11,0.07,0.13,-0.19,0.13,-0.02,149.62"
with col2:
    if st.button(" Try a fraudulent transaction"):
        st.session_state.txn_input = "406,-2.31,1.95,-1.61,3.99,-0.52,-1.43,-2.54,1.39,-2.77,-2.77,3.20,-2.90,-0.60,-4.29,0.38,-1.14,-2.83,-0.02,0.42,0.12,0.51,-0.03,-0.46,0.32,0.04,0.16,0.06,0.00"

input_df = st.text_area(
    "Enter Time, V1–V28, and Amount (comma-separated, 30 values total)",
    value=st.session_state.get("txn_input", ""),
    placeholder="e.g. 0, -1.36, -0.07, ..., 149.62",
    height=100
)

st.caption("Not sure what to enter? Click one of the sample buttons above.")

if st.button("Submit", type="primary"):
    if not input_df.strip():
        st.warning("Please enter transaction values first, or try a sample.")
    else:
        try:
            input_list = [x.strip() for x in input_df.split(',')]
            features = np.asarray(input_list, dtype=np.float64)

            if features.shape[0] != 30:
                st.error(f"Expected 30 values (Time, V1–V28, Amount), but got {features.shape[0]}. Please check your input.")
            else:
                prediction = model.predict(features.reshape(1, -1))

                try:
                    proba = model.predict_proba(features.reshape(1, -1))[0]
                    fraud_confidence = proba[1]
                except AttributeError:
                    fraud_confidence = None

                st.divider()
                if prediction[0] == 0:
                    if fraud_confidence is not None:
                        st.success(f" **Legitimate Transaction** — {fraud_confidence:.1%} fraud probability")
                    else:
                        st.success(" **Legitimate Transaction**")
                else:
                    if fraud_confidence is not None:
                        st.error(f" **Fraudulent Transaction** — {fraud_confidence:.1%} fraud probability")
                    else:
                        st.error(" **Fraudulent Transaction**")

        except ValueError:
            st.error("Couldn't parse the input. Make sure all 30 values are numbers separated by commas.")
