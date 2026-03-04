import streamlit as st

# Navigation definieren
pg = st.navigation([
    st.Page("views/home.py", title="Home", icon="🏠"),
    st.Page("views/bmi-calculator.py", title="Bakterien-Rechner", icon="🧫")
])

# App ausführen
pg.run()
