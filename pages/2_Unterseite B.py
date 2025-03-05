import streamlit as st

st.title("Unterseite B")

st.write("Diese Seite ist eine Unterseite der Startseite.")


st.title("MCH Berechnung")

# Eingabefelder für Hämoglobin (g/dl) und Erythrozytenanzahl (Millionen/µl)
hgb = st.number_input("Hämoglobin (g/dl):", min_value=0.0, step=0.1)
erythrozyten = st.number_input("Erythrozytenanzahl (Millionen/µl):", min_value=0.0, step=0.1)

# Auswahlfeld für das Geschlecht
geschlecht = st.selectbox("Geschlecht:", ["Wählen Sie aus", "Männlich", "Weiblich"])

# Berechnung des MCH, wenn alle Eingaben gültig sind
if hgb > 0 and erythrozyten > 0 and geschlecht != "Wählen Sie aus":
    mch = (hgb / erythrozyten) * 10
    st.write(f"Der MCH-Wert beträgt: {mch:.2f} pg")
    
    # Geschlechtsspezifische Hinweise für den MCH-Wert
    if geschlecht == "Männlich":
        st.write("Für Männer liegt der normale MCH-Wert typischerweise zwischen 27.5 und 33 pg.")
        # Überprüfung, ob der MCH-Wert im normalen Bereich liegt
        if 27.5 <= mch <= 33:
            st.write("Der MCH-Wert liegt im normalen Bereich für Männer.")
        else:
            st.write("Der MCH-Wert liegt nicht im normalen Bereich für Männer.")
    else:
        st.write("Für Frauen liegt der normale MCH-Wert typischerweise zwischen 26 und 32.5 pg.")
        # Überprüfung, ob der MCH-Wert im normalen Bereich liegt
        if 26 <= mch <= 32.5:
            st.write("Der MCH-Wert liegt im normalen Bereich für Frauen.")
        else:
            st.write("Der MCH-Wert liegt nicht im normalen Bereich für Frauen.")
else:
    st.write("Bitte geben Sie gültige Werte für Hämoglobin, Erythrozytenanzahl und Geschlecht ein.")