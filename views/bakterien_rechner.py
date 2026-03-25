import streamlit as st
import pandas as pd
import plotly.express as px 
from datetime import datetime
from functions.calculations import calculate_bacterial_growth, get_growth_steps
from utils.data_manager import DataManager

st.set_page_config(page_title="Bakterien-Simulator", layout="wide")
st.title("🧫 Bakterien-Wachstums-Simulator")

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["timestamp", "n0", "t", "g", "count"])


st.sidebar.header("Parameter anpassen")
n0 = st.sidebar.slider("Startanzahl ($N_0$)", 1, 1000, 100)
t = st.sidebar.slider("Beobachtungszeit (min)", 0, 500, 120)
g = st.sidebar.slider("Generationszeit (min)", 10, 100, 20)

nt, n_gen = calculate_bacterial_growth(n0, t, g)
result_steps = get_growth_steps(n0, t, g)

if st.sidebar.button("Simulation in Historie speichern"):
    new_entry = pd.DataFrame([{
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "n0": n0,
        "t": t,
        "g": g,
        "count": int(nt)
    }])

    st.session_state.history = pd.concat([new_entry, st.session_state.history], ignore_index=True)
    

    data_manager = DataManager()
    data_manager.save_user_data(st.session_state.history, 'data.csv')
    st.sidebar.success("Gespeichert!")


col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Endanzahl Bakterien", value=f"{int(nt):,}")
with col2:
    st.metric(label="Anzahl Generationen", value=f"{round(n_gen, 1)}")
with col3:
    growth_rate = ((nt - n0) / n0) * 100 if n0 > 0 else 0
    st.metric(label="Wachstum", value=f"+{int(growth_rate)}%", delta="Exponential")

st.divider()


df_plot = pd.DataFrame({
    "Zeit (Minuten)": result_steps["data"]["times"],
    "Bakterienanzahl": result_steps["data"]["counts"]
})

fig = px.area(df_plot, x="Zeit (Minuten)", y="Bakterienanzahl", 
              title="Exponentielles Wachstum über Zeit",
              template="plotly_white",
              color_discrete_sequence=['#00CC96']) 

fig.update_layout(xaxis_title="Zeit in Minuten", yaxis_title="Anzahl der Zellen", hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)


st.subheader("📊 Verlauf der Simulationen")
if not st.session_state.history.empty:
    st.dataframe(st.session_state.history, use_container_width=True)
    
    if st.button("Verlauf leeren"):
        st.session_state.history = pd.DataFrame(columns=["timestamp", "n0", "t", "g", "count"])
        st.rerun()
else:
    st.info("Noch keine Einträge in der Historie. Nutze den Button in der Sidebar zum Speichern.")

with st.expander("🔬 Biologische Erklärung & Formel"):
    st.write(f"""
    Das Modell berechnet die Zellzahl nach der Formel: $N_t = {n0} \cdot 2^{{({t}/{g})}}$.
    Aktuell haben wir ca. **{round(n_gen, 1)} Verdopplungszyklen** durchlaufen.
    """)
