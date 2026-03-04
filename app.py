import streamlit as st


pg = st.navigation([
    st.Page("views/home.py", title="Home", icon="🏠"),
    st.Page("views/bakterien_rechner.py", title="Bakterien-Rechner", icon="🧫"),
    st.Page("views/unterseite_a.py", title="Mikrobieller-Rechner", icon="🦠")
])


pg.run()
