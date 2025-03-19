from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st

st.title("Unterseite A")

st.write("Diese Seite ist eine Unterseite der Startseite.")

import streamlit as st

# Titel der App
st.title("🔘 Knopf-Klick-Zähler")

# Initialisiere den Zähler in der Session State, falls er noch nicht existiert
if "count" not in st.session_state:
    st.session_state.count = 0

# Erhöhe den Zähler, wenn der Knopf gedrückt wird
if st.button("Klick mich!"):
    st.session_state.count += 1

# Zeige die aktuelle Anzahl der Klicks an
st.subheader(f"📊 Der Knopf wurde *{st.session_state.count}* mal gedrückt.")