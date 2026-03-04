import streamlit as st

# Wir definieren nur die Seiten, die ihr WIRKLICH im Ordner 'views' habt
pg = st.navigation([
    st.Page("views/home.py", title="Home", icon="🏠"),
    st.Page("views/bakterien_rechner.py", title="Bakterien-Rechner", icon="🧫"),
    st.Page("views/unterseite_a.py", title="Zusatz-Rechner", icon="📊")
])

# Das hier startet die App
pg.run()
