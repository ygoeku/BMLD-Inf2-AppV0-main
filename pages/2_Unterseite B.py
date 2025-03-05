import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Titel
st.title("MCH und Hämatokrit Berechnung mit Punktdiagramm")

# Abfrage des Geschlechts
geschlecht = st.selectbox("Wählen Sie Ihr Geschlecht:", ["Wählen Sie aus", "Männlich", "Weiblich"])

# Nur wenn das Geschlecht ausgewählt ist, sollen die Eingabefelder angezeigt werden
if geschlecht != "Wählen Sie aus":
    # Eingabefelder für Hämoglobin (g/dl) und Erythrozytenanzahl (Millionen/µl)
    hgb = st.number_input("Hämoglobin (g/dl):", min_value=0.0, step=0.1)
    erythrozyten = st.number_input("Erythrozytenanzahl (Millionen/µl):", min_value=0.0, step=0.1)

    # Berechnung des MCH, wenn alle Eingaben gültig sind
    if hgb > 0 and erythrozyten > 0:
        mch = (hgb / erythrozyten) * 10  # Berechnung des MCH-Werts
        st.write(f"Der MCH-Wert beträgt: {mch:.2f} pg")
        
        # Geschlechtsspezifische Hinweise für den MCH-Wert
        if geschlecht == "Männlich":
            st.write("Für Männer liegt der normale MCH-Wert typischerweise zwischen 27.5 und 33 pg.")
        else:
            st.write("Für Frauen liegt der normale MCH-Wert typischerweise zwischen 26 und 32.5 pg.")
    
    else:
        st.write("Bitte geben Sie gültige Werte für Hämoglobin und Erythrozytenanzahl ein.")

    # Eingabefeld für den Hämatokritwert
    haematokrit = st.slider('Wählen Sie den Hämatokritwert (in %):', 
                            min_value=0.0, 
                            max_value=100.0, 
                            value=45.0, 
                            step=0.1)
    st.write('Der ausgewählte Hämatokritwert ist:', haematokrit, '%')

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Erstellen der x-Achsenwerte für MCH und Hämatokrit
    parameter = ['MCH (pg)', 'Hämatokrit (%)']
    values = [mch, haematokrit]

    # Erstellen der Vergleichslinien für die Referenzwerte
    if geschlecht == "Männlich":
        # Männer Referenzbereich: MCH 27.5-33 pg, Hämatokrit 40-53 %
        ax.plot([0, 1], [27.5, 27.5], label="Männlicher MCH-Referenzbereich", color="blue", linestyle="--")
        ax.plot([0, 1], [33, 33], label="Männlicher MCH-Referenzbereich", color="blue", linestyle="--")
        ax.plot([0, 1], [40, 40], label="Männlicher Hämatokrit-Referenzbereich", color="green", linestyle="--")
        ax.plot([0, 1], [53, 53], label="Männlicher Hämatokrit-Referenzbereich", color="green", linestyle="--")
    else:
        # Frauen Referenzbereich: MCH 26-32.5 pg, Hämatokrit 35-47 %
        ax.plot([0, 1], [26, 26], label="Weiblicher MCH-Referenzbereich", color="blue", linestyle="--")
        ax.plot([0, 1], [32.5, 32.5], label="Weiblicher MCH-Referenzbereich", color="blue", linestyle="--")
        ax.plot([0, 1], [35, 35], label="Weiblicher Hämatokrit-Referenzbereich", color="green", linestyle="--")
        ax.plot([0, 1], [47, 47], label="Weiblicher Hämatokrit-Referenzbereich", color="green", linestyle="--")

    # Punkte für den MCH- und Hämatokritwert des Benutzers
    ax.scatter(0, mch, color='red', label=f'Ihr MCH-Wert ({mch:.2f} pg)', zorder=5)
    ax.scatter(1, haematokrit, color='orange', label=f'Ihr Hämatokritwert ({haematokrit:.1f}%)', zorder=5)

    # Anpassen der Achsen und Labels
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['MCH (pg)', 'Hämatokrit (%)'])
    ax.set_ylabel('Wert')
    ax.set_title('Vergleich von MCH und Hämatokrit mit Referenzbereichen')
    ax.legend()

    # Anzeige des Diagramms in Streamlit
    st.pyplot(fig)

else:
    st.write("Bitte wählen Sie ein Geschlecht aus.")
