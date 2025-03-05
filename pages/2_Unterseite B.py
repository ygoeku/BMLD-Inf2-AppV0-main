import streamlit as st

st.title("Unterseite B")

st.write("Diese Seite ist eine Unterseite der Startseite.")

st.title("MCH Berechnung")

hgb = st.number_input("Hämoglobin (g/dl):", min_value=0.0, step=0.1)
hkt = st.number_input("Hämatokrit (%):", min_value=0.0, step=0.1)

# Debugging: Check the input values
st.write(f"Hämoglobin (hgb): {hgb}")
st.write(f"Hämatokrit (hkt): {hkt}")

# Ensure values are greater than 0 and valid
if hgb > 0 and hkt > 0:
    mch = (hgb / hkt) * 10
    st.write(f"Der MCH-Wert beträgt: {mch:.2f} pg")
else:
    if hgb == 0 or hkt == 0:
        st.write("Bitte geben Sie gültige Werte für Hämoglobin und Hämatokrit ein, die größer als 0 sind.")
    else:
        st.write("Bitte geben Sie gültige Werte für Hämoglobin und Hämatokrit ein.")