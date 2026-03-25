import pandas as pd
import streamlit as st
from utils.data_manager import DataManager  
from utils.login_manager import LoginManager

data_manager =DataManager(
    fs_protocol= 'webdav',
    fs_root_folder="BMLD_APP_DB"
)
login_manager = LoginManager(data_manager)
login_manager.login_register()


if 'history' not in st.session_state:
    st.session_state['history'] = data_manager.load_user_data(
        'data.csv', 
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )

pg = st.navigation([
    st.Page("views/home.py", title="Home", icon="🏠"),
    st.Page("views/bakterien_rechner.py", title="Bakterien-Rechner", icon="🧫"),
    st.Page("views/unterseite_a.py", title="Mikrobieller-Rechner", icon="🦠")
])
pg.run()
