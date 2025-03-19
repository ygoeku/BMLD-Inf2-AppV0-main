from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')
import streamlit as st
import datetime
import pytz
from functions.mch_calculator import calculate_mch

st.title("🩺 MCH Berechnung")


timezone = 'Europe/Zurich'  
tz = pytz.timezone(timezone)
now = datetime.datetime.now(tz).strftime('%d.%m.%Y %H:%M:%S')
st.write(f"**Aktuelle Uhrzeit (in {timezone}):** {now} ⏰")


geschlecht = st.selectbox("👤 Wählen Sie Ihr Geschlecht:", ["Wählen Sie aus", "Männlich", "Weiblich"])

hgb = st.number_input("🩸 Hämoglobin (g/dl):", min_value=0.0, step=0.1)
erythrozyten = st.number_input("🔬 Erythrozytenanzahl (Millionen/µl):", min_value=0.0, step=0.1)

if hgb > 0 and erythrozyten > 0:
    mch = (hgb / erythrozyten) * 10  
    st.write(f"**Der MCH-Wert beträgt:** {mch:.2f} pg ")

    
    if geschlecht == "Männlich":
        st.write("<p style='color:black;'>Für Männer liegt der normale MCH-Wert typischerweise zwischen 27.5 und 33 pg.</p>", unsafe_allow_html=True)
        if 27.5 <= mch <= 33:
            st.write("<p style='color:green;'>✅ Der MCH-Wert liegt im Referenzbereich für Männer (27.5 - 33 pg).</p>", unsafe_allow_html=True)
        else:
            st.write("<p style='color:red;'>❌ Der MCH-Wert liegt NICHT im Referenzbereich für Männer (27.5 - 33 pg).</p>", unsafe_allow_html=True)
    elif geschlecht == "Weiblich":
        st.write("<p style='color:black;'>Für Frauen liegt der normale MCH-Wert typischerweise zwischen 26 und 32.5 pg.</p>", unsafe_allow_html=True)
        if 26 <= mch <= 32.5:
            st.write("<p style='color:green;'>✅ Der MCH-Wert liegt im Referenzbereich für Frauen (26 - 32.5 pg).</p>", unsafe_allow_html=True)
        else:
            st.write("<p style='color:red;'>❌ Der MCH-Wert liegt NICHT im Referenzbereich für Frauen (26 - 32.5 pg).</p>", unsafe_allow_html=True)
else:
    st.write("<p style='color:red;'> Bitte geben Sie gültige Werte für Hämoglobin und Erythrozytenanzahl ein.</p>", unsafe_allow_html=True)

haematokrit = st.slider('Wählen Sie den Hämatokritwert (in %):', min_value=0.0, max_value=100.0, value=45.0, step=0.1)
st.write(f'**Der ausgewählte Hämatokritwert ist:** {haematokrit}% 🩸')

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

if hgb > 0 and erythrozyten > 0:
    result_dict =calculate_mch(hgb, erythrozyten)
    st.write(f'**Der MCH ist:** {result_dict["mch"]}')
    st.write(f'**Berechnet am:** {result_dict["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')
    st.write(f'**Kategorie:** {result_dict["category"]}')

    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result_dict)

        

