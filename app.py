import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

# Wenn die Datei im Hauptverzeichnis liegt:
pg_second = st.Page("addition_calculator.py", title="Unterseite A", icon=":material/info:")

# Wenn die Datei in einem UNTERORDNER namens "addition_calculator" liegt:
pg_second = st.Page("addition_calculator/addition_calculator.py", title="Unterseite A", icon=":material/info:")


pg = st.navigation([pg_home, pg_second])
pg.run()
