import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('Random_Forest_Model.joblib')

# Config Page
st.set_page_config(page_title="🎓 Student Status Predictor", page_icon="🎓", layout="wide")

# Header
st.title("🎓 Student Status Prediction")
st.markdown("""
Selamat datang di aplikasi prediksi status mahasiswa.  
Masukkan data akademik di form berikut, lalu klik **Prediksi** untuk melihat status mahasiswa:
- **Dropout**
- **Enrolled/Graduated**
""")

# Sidebar
st.sidebar.title("ℹ️ Tentang Aplikasi")
st.sidebar.write("""
Aplikasi ini menggunakan **Random Forest Classifier** untuk memprediksi status mahasiswa berdasarkan data akademik.
""")

# Form Input
with st.form("student_data_form"):
    st.subheader("📑 Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        Marital_status = st.radio('Marital Status', [0, 1], format_func=lambda x: 'Menikah' if x == 1 else 'Belum Menikah')
        Application_mode = st.number_input('Application Mode', min_value=0)
        Previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0.0)
        Admission_grade = st.number_input('Admission Grade', min_value=0.0)
        Displaced = st.radio('Displaced', [0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
        Debtor = st.radio('Debtor', [0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
        Tuition_fees_up_to_date = st.radio('Tuition Fees Up to Date', [0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
        Gender = st.radio('Gender', [0, 1], format_func=lambda x: 'Laki-laki' if x == 1 else 'Perempuan')
        Scholarship_holder = st.radio('Scholarship Holder', [0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
        Age_at_enrollment = st.number_input('Age at Enrollment', min_value=0)

    with col2:
        Curricular_units_1st_sem_enrolled = st.number_input('1st Sem - Enrolled Units', min_value=0)
        Curricular_units_1st_sem_approved = st.number_input('1st Sem - Approved Units', min_value=0)
        Curricular_units_1st_sem_grade = st.number_input('1st Sem - Grade', min_value=0.0)
        Curricular_units_2nd_sem_enrolled = st.number_input('2nd Sem - Enrolled Units', min_value=0)
        Curricular_units_2nd_sem_evaluations = st.number_input('2nd Sem - Evaluations', min_value=0)
        Curricular_units_2nd_sem_approved = st.number_input('2nd Sem - Approved Units', min_value=0)
        Curricular_units_2nd_sem_grade = st.number_input('2nd Sem - Grade', min_value=0.0)
        Curricular_units_2nd_sem_without_evaluations = st.number_input('2nd Sem - Without Evaluations', min_value=0)

    submitted = st.form_submit_button("🔮 Prediksi")

    if submitted:
        features = np.array([[Marital_status, Application_mode, Previous_qualification_grade, Admission_grade, Displaced, Debtor,
                              Tuition_fees_up_to_date, Gender, Scholarship_holder, Age_at_enrollment,
                              Curricular_units_1st_sem_enrolled, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade,
                              Curricular_units_2nd_sem_enrolled, Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved,
                              Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations]])

        prediction = model.predict(features)
        status_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduated'}
        result = status_map.get(prediction[0], "Unknown")

        st.success(f"🎯 Prediksi Status Mahasiswa: **{result}**")