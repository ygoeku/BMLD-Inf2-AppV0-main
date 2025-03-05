import streamlit as st

# Titel
st.title("MCH und Hämatokrit Berechnung")

# Abfrage des Geschlechts
geschlecht = st.selectbox("Geschlecht:", ["Wählen Sie aus", "Männlich", "Weiblich"])

# Eingabefelder für Hämoglobin (g/dl) und Erythrozytenanzahl (Millionen/µl)
if geschlecht != "Wählen Sie aus":
    hgb = st.number_input("Hämoglobin (g/dl):", min_value=0.0, step=0.1)
    erythrozyten = st.number_input("Erythrozytenanzahl (Millionen/µl):", min_value=0.0, step=0.1)

    # Berechnung des MCH, wenn alle Eingaben gültig sind
    if hgb > 0 and erythrozyten > 0:
        mch = (hgb / erythrozyten) * 10
        st.write(f"Der MCH-Wert beträgt: {mch:.2f} pg")
        
        # Geschlechtsspezifische Hinweise für den MCH-Wert
        if geschlecht == "Männlich":
            st.write("Für Männer liegt der normale MCH-Wert typischerweise zwischen 27.5 und 33 pg.")
            if 27.5 <= mch <= 33:
                st.write("Der MCH-Wert liegt im Referenzbereich für Männer.")
            else:
                st.write("Der MCH-Wert liegt nicht im Referenzbereich für Männer.")
        else:
            st.write("Für Frauen liegt der normale MCH-Wert typischerweise zwischen 26 und 32.5 pg.")
            if 26 <= mch <= 32.5:
                st.write("Der MCH-Wert liegt im Referenzbereich für Frauen.")
            else:
                st.write("Der MCH-Wert liegt nicht im Referenzbereich für Frauen.")
    
    else:
        st.write("Bitte geben Sie gültige Werte für Hämoglobin und Erythrozytenanzahl ein.")

    # Eingabefeld für den Hämatokritwert
    haematokrit = st.slider('Wählen Sie den Hämatokritwert (in %):', 
                            min_value=0.0, 
                            max_value=100.0, 
                            value=45.0, 
                            step=0.1)
    st.write('Der ausgewählte Hämatokritwert ist:', haematokrit, '%')

    # Geschlechtsspezifische Hinweise für den Hämatokritwert
    if geschlecht == "Männlich":
        if 40 <= haematokrit <= 53:
            st.write("Der Hämatokritwert liegt im normalen Bereich für Männer.")
        else:
            st.write("Der Hämatokritwert liegt nicht im normalen Bereich für Männer.")
    else:
        if 35 <= haematokrit <= 47:
            st.write("Der Hämatokritwert liegt im normalen Bereich für Frauen.")
        else:
            st.write("Der Hämatokritwert liegt nicht im normalen Bereich für Frauen.")
else:
    st.write("Bitte wählen Sie ein Geschlecht aus.")

