import streamlit as st
import pandas as pd
import plotly.express as px 
from functions.calculations import calculate_bacterial_growth, get_growth_steps
from utils.data_manager import DataManager

st.title("🧫 Bakterien-Wachstums-Simulator")


st.sidebar.header("Parameter anpassen")
n0 = st.sidebar.slider("Startanzahl ($N_0$)", 1, 1000, 100)
t = st.sidebar.slider("Beobachtungszeit (min)", 0, 500, 120)
g = st.sidebar.slider("Generationszeit (min)", 10, 100, 20)


nt, n_gen = calculate_bacterial_growth(n0, t, g)
result_test = calculate_bacterial_growth(n0, t, g)
st.write(result_test)

result = get_growth_steps(n0, t, g)  
times = result["data"]["times"]
counts = result["data"]["counts"]


df = pd.DataFrame({
    "Zeit (Minuten)": times,
    "Bakterienanzahl": counts
})



col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Endanzahl Bakterien", value=f"{int(nt):,}")
with col2:
    st.metric(label="Anzahl Generationen", value=f"{round(n_gen, 1)}")
with col3:

    growth_rate = ((nt - n0) / n0) * 100 if n0 > 0 else 0
    st.metric(label="Wachstum", value=f"+{int(growth_rate)}%", delta="Exponential")

st.divider()


st.subheader("Wachstumskurve")

fig = px.area(df, x="Zeit (Minuten)", y="Bakterienanzahl", 
              title="Exponentielles Wachstum über Zeit",
              template="plotly_white",
              color_discrete_sequence=['#00CC96']) 

fig.update_layout(
    xaxis_title="Zeit in Minuten",
    yaxis_title="Anzahl der Zellen",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)


with st.expander("🔬 Biologische Erklärung & Formel"):
    st.write(f"""
    Das Modell berechnet die Zellzahl nach der Formel: $N_t = {n0} \cdot 2^{{({t}/{g})}}$.
    Aktuell haben wir ca. **{round(n_gen, 1)} Verdopplungszyklen** durchlaufen.
    """)
st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])])
st.dataframe(st.session_state['data_df'])
 
data_manager = DataManager()
data_manager.save_user_data(st.session_state['data_df'], 'data.csv')