import streamlit as st
import pandas as pd
import joblib
import time
import subprocess
import os

from streamlit.elements.arrow import Data

st.set_page_config(page_title='C-IPS')


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>C-IPS</h1>", unsafe_allow_html=True)
#st.write()

# st.write("\n")


col1, col2, col3 , col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    pass
with col2:
    pass
with col3 :
    pass
with col4:
    pass
with col5:
    pass
with col6:
    pass
with col7:
    button_start= st.button('Terminal')
with col8:
    st.button("Report")
    

if button_start:
    subprocess.call('start', shell = True) 


    


mj=joblib.load('model_joblib_real_random_forest_fourteen')
df = pd.read_csv('x_test_fourteen.csv')
k=0

# .format(port.to_string(index=False))
for i in range(1, 102):
    d=df.iloc[i-1:i]
    st.write("\n")
    st.write("\n")
    st.write(d)
    # port = d['Destination Port']
    val = mj.predict(d)
    if val == 0:
            #st.success("Benign network, NORMAL TRAFFIC detected!")
        if(k>0):
            time.sleep(2)
        k=k+1
        continue
    elif val == 1:
        st.error("DDoS attack detected! Decoy Server Activated for IP address 205.174.165.73")
    elif val == 2: 
        st.error("PortScan attack detected! Decoy Server Activated for IP address 205.174.165.73")
    elif val == 3:
        st.error("Bot attack detected! Decoy Server Activated for IP address 205.174.165.73")
    elif val == 4: 
        st.error("Infiltration attack detected! Decoy Server Activated for IP address 205.174.165.73")
    elif val == 5: 
        st.error("Web attack (Brute Force) detected! IP address 205.174.165.73 blocked for next 15 seconds")
    elif val == 6:
        st.error("Web attack (XSS) detected! IP address 205.174.165.73 blocked for next 15 seconds ")
    elif val == 7:
        st.error("Web attack (SQL Injection) detected! IP address 205.174.165.73 blocked for next 15 seconds")
    else:
        st.error("FTP-Patator attack detected! IP address 205.174.165.69 blocked for next 15 seconds")

    

        



