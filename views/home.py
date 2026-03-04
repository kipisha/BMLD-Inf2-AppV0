
import streamlit as st


st.title("🧬 Biomedizinischer Bakterien-Rechner")


st.markdown("""
### Projekt-Übersicht
Willkommen zu unserer App für das Modul **Informatik 2 (BMLD/ZHAW)**. 
Dieses Tool wurde speziell entwickelt, um das **exponentielle Wachstum von Bakterienkulturen** 
interaktiv zu simulieren und zu visualisieren.
""")

st.divider()


st.header("👤 Autoren & Mitwirkende")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Autorin 1")
    st.write("**Name:** Darlene Armenio")
    st.write("**E-Mail:** armdar01@students.zhaw.ch")

with col2:
    st.subheader("Autorin 2")
    st.write("**Name:** Kipisha Selvan")
    st.write("**E-Mail:** selvakip@students.zhaw.ch")

st.divider()


st.info("💡 **Anleitung:** Nutze das Menü auf der linken Seite, um zum **Bakterien-Rechner** zu navigieren.")


st.caption("Entwickelt im Frühjahr 2026 | BMLD | ZHAW")
