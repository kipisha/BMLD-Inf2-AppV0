import streamlit as st
import pandas as pd
from functions.calculations import calculate_bacterial_growth, get_growth_steps

data = {
    "Organismus": [
        "Escherichia coli", "Bacillus subtilis", "Staphylococcus aureus", 
        "Salmonella enterica", "Vibrio cholerae", "Pseudomonas aeruginosa",
        "Listeria monocytogenes", "Mycobacterium tuberculosis", "Treponema pallidum",
        "Clostridium perfringens", "Streptococcus pyogenes", "Campylobacter jejuni"
    ],
    "Generationszeit_min": [20, 26, 28, 25, 13, 45, 40, 720, 1980, 10, 40, 90],
    "Kategorie": ["Darm", "Labor", "Krankenhaus", "Lebensmittel", "Wasser", "Wunde", "Kühlkette", "Lunge", "STD", "Wundinfekt", "Hals", "Darm"]
}
df_bakterien = pd.DataFrame(data)


st.title("Mikrobieller-Rechner🦠")
    
st.markdown("""
    Wähle einen Organismus aus der Datenbank aus. Die Generationszeit ($g$) wird 
    automatisch für die Berechnung übernommen.
    """)



st.subheader("Bakterien-Katalog")
selected_organism = st.selectbox("Suche in der Datenbank:", df_bakterien["Organismus"])
    

g_aus_liste = df_bakterien[df_bakterien["Organismus"] == selected_organism]["Generationszeit_min"].values[0]


with st.form("pro_calc"):
        col1, col2 = st.columns(2)
        with col1:
            n0 = st.number_input("Startanzahl (N0)", value=100)
            t = st.number_input("Zeit (min)", value=180)
        with col2:

            g = st.number_input(f"Generationszeit für {selected_organism}", value=int(g_aus_liste))
        
        submit = st.form_submit_button("Wachstum berechnen")

if submit:

        nt, n_gen = calculate_bacterial_growth(n0, t, g)
        st.success(f"Ergebnis für {selected_organism}: {int(nt):,} Bakterien")
        

        times, counts = get_growth_steps(n0, t, g)
        chart_df = pd.DataFrame({"Zeit": times, "Anzahl": counts})
        st.line_chart(chart_df.set_index("Zeit"))
