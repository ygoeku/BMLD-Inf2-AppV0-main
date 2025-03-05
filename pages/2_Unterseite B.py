import streamlit as st
import datetime
import pytz

# Titel mit Emoji und Farbgebung
st.title("🩺 MCH und Hämatokrit Berechnung")

# Zeitzone und aktuelle Uhrzeit berechnen
timezone = 'Europe/Zurich'  # Beispiel: Setze die Zeitzone auf Zürich
tz = pytz.timezone(timezone)
now = datetime.datetime.now(tz).strftime('%d.%m.%Y %H:%M:%S')
st.write(f"**Aktuelle Uhrzeit (in {timezone}):** {now} ⏰")

# Abfrage des Geschlechts
geschlecht = st.selectbox("👤 Wählen Sie Ihr Geschlecht:", ["Wählen Sie aus", "Männlich", "Weiblich"])

# Eingabefelder für Hämoglobin (g/dl) und Erythrozytenanzahl (Millionen/µl)
hgb = st.number_input("🩸 Hämoglobin (g/dl):", min_value=0.0, step=0.1)
erythrozyten = st.number_input("🔬 Erythrozytenanzahl (Millionen/µl):", min_value=0.0, step=0.1)

# Berechnung des MCH, wenn alle Eingaben gültig sind
if hgb > 0 and erythrozyten > 0:
    mch = (hgb / erythrozyten) * 10  # Berechnung des MCH-Werts
    st.write(f"**Der MCH-Wert beträgt:** {mch:.2f} pg ")

    # Geschlechtsspezifische Hinweise für den MCH-Wert
    if geschlecht == "Männlich":
        st.write("<p style='color:black;'>Für Männer liegt der normale MCH-Wert typischerweise zwischen 27.5 und 33 pg.</p>", unsafe_allow_html=True)
        # Überprüfung, ob der MCH-Wert im Referenzbereich für Männer liegt
        if 27.5 <= mch <= 33:
            st.write("<p style='color:green;'>✅ Der MCH-Wert liegt im Referenzbereich für Männer (27.5 - 33 pg).</p>", unsafe_allow_html=True)
        else:
            st.write("<p style='color:red;'>❌ Der MCH-Wert liegt NICHT im Referenzbereich für Männer (27.5 - 33 pg).</p>", unsafe_allow_html=True)
    elif geschlecht == "Weiblich":
        st.write("<p style='color:black;'>Für Frauen liegt der normale MCH-Wert typischerweise zwischen 26 und 32.5 pg.</p>", unsafe_allow_html=True)
        # Überprüfung, ob der MCH-Wert im Referenzbereich für Frauen liegt
        if 26 <= mch <= 32.5:
            st.write("<p style='color:green;'>✅ Der MCH-Wert liegt im Referenzbereich für Frauen (26 - 32.5 pg).</p>", unsafe_allow_html=True)
        else:
            st.write("<p style='color:red;'>❌ Der MCH-Wert liegt NICHT im Referenzbereich für Frauen (26 - 32.5 pg).</p>", unsafe_allow_html=True)
else:
    st.write("<p style='color:red;'> Bitte geben Sie gültige Werte für Hämoglobin und Erythrozytenanzahl ein.</p>", unsafe_allow_html=True)

# Eingabefeld für den Hämatokritwert
haematokrit = st.slider('Wählen Sie den Hämatokritwert (in %):', min_value=0.0, max_value=100.0, value=45.0, step=0.1)
st.write(f'**Der ausgewählte Hämatokritwert ist:** {haematokrit}% 🩸')

# Überprüfung, ob der Hämatokritwert im Referenzbereich liegt
if geschlecht == "Männlich":
    if 40 <= haematokrit <= 53:
        st.write("<p style='color:green;'>✅ Der Hämatokritwert liegt im Referenzbereich für Männer (40-53%).</p>", unsafe_allow_html=True)
    else:
        st.write("<p style='color:red;'>❌ Der Hämatokritwert liegt NICHT im Referenzbereich für Männer (40-53%).</p>", unsafe_allow_html=True)
elif geschlecht == "Weiblich":
    if 35 <= haematokrit <= 47:
        st.write("<p style='color:green;'>✅ Der Hämatokritwert liegt im Referenzbereich für Frauen (35-47%).</p>", unsafe_allow_html=True)
    else:
        st.write("<p style='color:red;'>❌ Der Hämatokritwert liegt NICHT im Referenzbereich für Frauen (35-47%).</p>", unsafe_allow_html=True)





