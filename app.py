import streamlit as st
import pandas as pd
import joblib
import time
import subprocess
import os
from PIL import Image
img=Image.open('cips2.png')

from streamlit.elements.arrow import Data

#favicon="C:\Users\ASUS\Documents\Juspay-CIPS\cips2.png"
st.set_page_config(page_title='C-IPS', page_icon=img)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
#st.markdown(hide_st_style, unsafe_allow_html=True)

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
    button_report= st.button("Report")
    

if button_start:
    subprocess.call('start', shell = True)

if button_report:
    subprocess.Popen(["streamlit", "run", "reports.py"])
     


    


mj=joblib.load('model_joblib_real_random_forest_fourteen')
df = pd.read_csv('x_test_fourteen.csv')
k=0

values=['205.174.165.73','205.174.165.69','205.174.165.70','205.174.165.71', 
'85.237.172.55',
'157.79.212.141',
'197.23.92.143',
'81.87.44.36',
'228.131.54.49',
'174.147.164.42',
'6.16.43.120',
'111.168.193.137',
'144.3.229.250',
'62.174.83.16']

iplist= []
iplist= np.random.choice(values, size= 101)

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
        st.error("DDoS attack detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val == 2: 
        st.error("PortScan attack detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val == 3:
        st.error("Bot attack detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val == 4: 
        st.error("Infiltration attack detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val == 5: 
        st.error("Web attack (Brute Force) detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val == 6:
        st.error("Web attack (XSS) detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val == 7:
        st.error("Web attack (SQL Injection) detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val ==8:
        st.error("FTP-Patator attack detected! Decoy Server activated for IP Address "+ iplist[i])
    elif val==9:
        st.error('SSH-Patator attack detected! Decoy Server activated for IP Address' + iplist[i])
    elif val==10:
        st.error('DoS slowloris attack detected! Decoy Server activated for IP Address' + iplist[i])
    elif val ==11:
        st.error('DoS Slowhttptest attack detected! Decoy Server activated for IP Address' + iplist[i])
    elif val==12:
        st.error('DoS Hulk attack detected! Decoy Server activated for IP Address' + iplist[i])
    elif val==13:
        st.error('DoS GoldenEye attack detected! Decoy Server activated for IP Address' + iplist[i])
    else:
        st.error('Heartbleed attack detected! Decoy Server activated for IP Address' + iplist[i])

    

        



