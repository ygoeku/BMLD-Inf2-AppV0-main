import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Yasemin Gökuguz (goekuyas@students.zhaw.ch)
- Elena Avkova (avkovele@students.zhaw.ch)

Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)

Autorinnen - Yasemin Gökuguz (goekuyas@students.zhaw.ch) und Elena Avkova (avkovele@students.zhaw.ch)
"""
import streamlit as st

# Titel der App
st.title("🏋️‍♂️ BMI-Rechner (Body-Mass-Index)")

# Beschreibung
st.write("""
Der **Body-Mass-Index (BMI)** ist eine einfache Methode zur Einschätzung des Körpergewichts in Relation zur Körpergröße. 

Die Formel lautet:

\[
BMI = \frac{\text{Gewicht (kg)}}{\text{Größe (m)}^2}
\]

Gib deine Daten unten ein, um deinen BMI zu berechnen.
""")

# Eingabe für Größe in cm
height_cm = st.number_input("📏 Körpergröße in cm eingeben:", min_value=50, max_value=250, step=1, format="%d")

# Eingabe für Gewicht in kg
weight_kg = st.number_input("⚖️ Körpergewicht in kg eingeben:", min_value=10, max_value=300, step=1, format="%d")

# Berechnung des BMI
if height_cm > 0 and weight_kg > 0:
    height_m = height_cm / 100  # Umrechnung von cm in m
    bmi = weight_kg / (height_m ** 2)
    st.subheader(f"📊 Dein BMI: **{bmi:.2f}**")

    # Interpretation des BMI
    if bmi < 18.5:
        st.warning("⚠️ **Untergewicht** – Ein höheres Körpergewicht könnte gesundheitlich vorteilhaft sein.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ **Normalgewicht** – Dein BMI liegt im gesunden Bereich!")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ **Übergewicht** – Achte auf eine gesunde Ernährung und Bewegung.")
    else:
        st.error("⚠️ **Adipositas** – Ein hoher BMI kann gesundheitliche Risiken mit sich bringen.")
else:
    st.info("Bitte gültige Werte für Größe und Gewicht eingeben.")


