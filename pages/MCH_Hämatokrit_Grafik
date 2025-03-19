# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BMI Grafik ===
import streamlit as st

st.title('🩺 MCH und Hämatokrit Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine MCH und Hämatokrit Daten vorhanden. Berechnen Sie Ihren MCH und Hämatokrit auf der Startseite.')
    st.stop()

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['weight'], 
                use_container_width=True)
st.caption('Hämoglobinwert über Zeit (g/dl)')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['height'],
                use_container_width=True)
st.caption('Erythrozytenanzahl über Zeit Millionen/μl')

# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['bmi'],
                use_container_width=True)
st.caption('MCH über Zeit')
