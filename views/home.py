
import streamlit as st


st.title(" CellCompute :  Digitaler Bakterien-Rechner 🧫")


st.markdown("""
### Projekt-Übersicht
Willkommen zu unserer App für das Modul **Informatik 2 (BMLD/ZHAW)**. 
Dieses Tool wurde speziell entwickelt, um das **exponentielle Wachstum von Bakterienkulturen** 
interaktiv zu simulieren und zu visualisieren.
""")

st.divider()


st.header(" Autoren 👩‍🔬")
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




# ...existing code...
import streamlit as st
import base64

def set_bg_from_url(url: str):
    st.markdown(f"""
    <style>
    .stApp {{
      background-image: url("{url}");
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      background-attachment: fixed;
      filter: saturate(0.9) brightness(1.05);
      opacity: 0.95;
    }}
    </style>
    """, unsafe_allow_html=True)

def set_bg_from_local(image_path: str):
    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
      background-image: url("data:image/png;base64,{b64}");
      background-size: cover;
      background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# Beispiel: URL oder lokale Datei nutzen
# set_bg_from_url("https://example.com/path/to/your-mint-bacteria-pattern.jpg")
# oder nach Download:
# set_bg_from_local("assets/background-mint.png")

pg = st.navigation([
    st.Page("views/home.py", title="Home", icon="🏠"),
    st.Page("views/bakterien_rechner.py", title="Bakterien-Rechner", icon="🧫"),
    st.Page("views/unterseite_a.py", title="Mikrobieller-Rechner", icon="🦠")
])

# ...existing code...
pg.run()