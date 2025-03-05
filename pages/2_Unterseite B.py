import streamlit as st
import datetime
import pytz

# Titel mit Emoji und Farbgebung
st.title("🩺 MCH und Hämatokrit Berechnung")

# Zeitzone und aktuelle Uhrzeit berechnen
timezone = 'Europe/Berlin'  # Beispiel: Setze die Zeitzone auf Berlin
tz = pytz.timezone(timezone)
now = datetime.datetime.now(tz).strftime('%d.%m.%Y %H:%M:%S')
st.markdown(f"**Aktuelle Uhrzeit (in {timezone}):** {now} ⏰", unsafe_allow_html=True)

# Abfrage des Geschlechts
geschlecht = st.selectbox("👤 Wählen Sie Ihr Geschlecht:", ["Wählen Sie aus", "Männlich", "Weiblich"])

# Nur wenn das Geschlecht ausgewählt ist, sollen die Eingabefelder angezeigt werden
if geschlecht != "Wählen Sie aus":
    # Eingabefelder für Hämoglobin (g/dl) und Erythrozytenanzahl (Millionen/µl)
    hgb = st.number_input("🩸 Hämoglobin (g/dl):", min_value=0.0, step=0.1)
    erythrozyten = st.number_input("🔬 Erythrozytenanzahl (Millionen/µl):", min_value=0.0, step=0.1)

    # Berechnung des MCH, wenn alle Eingaben gültig sind
    if hgb > 0 and erythrozyten > 0:
        mch = (hgb / erythrozyten) * 10  # Berechnung des MCH-Werts
        st.markdown(f"**Der MCH-Wert beträgt:** {mch:.2f} pg 🧪", unsafe_allow_html=True)
        
        # Geschlechtsspezifische Hinweise für den MCH-Wert
        if geschlecht == "Männlich":
            st.markdown("<p style='color:blue;'>Für Männer liegt der normale MCH-Wert typischerweise zwischen 27.5 und 33 pg.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:magenta;'>Für Frauen liegt der normale MCH-Wert typischerweise zwischen 26 und 32.5 pg.</p>", unsafe_allow_html=True)
    
    else:
        st.markdown("<p style='color:red;'>❌ Bitte geben Sie gültige Werte für Hämoglobin und Erythrozytenanzahl ein.</p>", unsafe_allow_html=True)

    # Eingabefeld für den Hämatokritwert
    haematokrit = st.slider('💉 Wählen Sie den Hämatokritwert (in %):', 
                            min_value=0.0, 
                            max_value=100.0, 
                            value=45.0, 
                            step=0.1)
    st.markdown(f'**Der ausgewählte Hämatokritwert ist:** {haematokrit}% 🩸', unsafe_allow_html=True)

    # Überprüfung, ob der Hämatokritwert im Referenzbereich liegt
    if geschlecht == "Männlich":
        if 40 <= haematokrit <= 53:
            st.markdown("<p style='color:green;'>✅ Der Hämatokritwert liegt im Referenzbereich für Männer (40-53%).</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:red;'>❌ Der Hämatokritwert liegt NICHT im Referenzbereich für Männer (40-53%).</p>", unsafe_allow_html=True)
    else:
        if 35 <= haematokrit <= 47:
            st.markdown("<p style='color:green;'>✅ Der Hämatokritwert liegt im Referenzbereich für Frauen (35-47%).</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:red;'>❌ Der Hämatokritwert liegt NICHT im Referenzbereich für Frauen (35-47%).</p>", unsafe_allow_html=True)

else:
    st.markdown("<p style='color:red;'>❓ Bitte wählen Sie ein Geschlecht aus.</p>", unsafe_allow_html=True)

