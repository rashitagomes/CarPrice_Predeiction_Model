import streamlit as st
import pickle

# Encoding dictionaries
d1 = {'Comprehensive':0, 'Third Party insurance':1, 'Zero Dep':2, 'Not Available':3, 'Third Party':1}
d2 = {'Petrol':0,'Diesel':1,'CNG':2}
d3 = {'Manual':0,'Automatic':1}
d4 = {'First Owner':1,'Second Owner':2,'Third Owner':3,'Fifth Owner':5}

# Load model
final_model = pickle.load(open('final_model.pkl','rb'))

# Page config
st.set_page_config(page_title="Car Price Predictor", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}

/* Header */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: 600;
    color: #e2e8f0;
}

/* Section card */

/* Button */
.stButton>button {
    width: 100%;
    background-color: #38bdf8;
    color: black;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px;
}

/* Result box */
.result-box {
    background: #111827;
    border: 1px solid #334155;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

.result-text {
    font-size: 26px;
    color: #38bdf8;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🚗 Car Price Predictor</div>', unsafe_allow_html=True)
st.write("")

# ---------- INPUT SECTIONS ---------- #

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section">', unsafe_allow_html=True)

    insurance_validity = st.selectbox("Insurance Validity", list(d1.keys()))
    fuel_type = st.radio("Fuel Type", list(d2.keys()))

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section">', unsafe_allow_html=True)

    ownership = st.selectbox("Ownership", list(d4.keys()))
    transmission = st.radio("Transmission Type", list(d3.keys()))

    st.markdown('</div>', unsafe_allow_html=True)

# Full width section
st.markdown('<div class="section">', unsafe_allow_html=True)

kms_driven = st.number_input(
    "KMs Driven",
    min_value=0,
    max_value=500000,
    step=1000
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- BUTTON ----------
predict_btn = st.button("Predict Price")

# ---------- RESULT ----------
if predict_btn:
    try:
        insurance_validity_enc = d1[insurance_validity]
        fuel_type_enc = d2[fuel_type]
        ownership_enc = d4[ownership]
        transmission_enc = d3[transmission]

        test = [[
            insurance_validity_enc,
            fuel_type_enc,
            kms_driven,
            ownership_enc,
            transmission_enc
        ]]

        prediction = final_model.predict(test)[0]

        st.markdown(f"""
        <div class="result-box">
            <div>Estimated Price</div>
            <div class="result-text">₹ {round(prediction, 2)} Lakhs</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {e}")