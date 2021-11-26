import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time
import pandas as pd
import plotly.graph_objects as go
import joblib


st.set_page_config(page_title='Reports')



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown("<h1 style='text-align: center; color: white;'>C-IPS</h1>", unsafe_allow_html=True)


mj=joblib.load('model_joblib_real_random_forest_fourteen')
#df = pd.read_csv('x_test_fourteen.csv')
dfx = pd.read_csv('x_test_fourteen.csv')
dfxi=dfx.iloc[0:100]
dfy = pd.read_csv(r'y_test_fourteen.csv')
dfyi=dfy.iloc[0:100]

st.title("Reports")
#x_axis = st.selectbox(
#        "Choose a column for its relationship with the Label", dfx.columns)



x_axis=dfx.columns




#st.write(type(x_axis[0]))

#st.write(len(x_axis))

for i in range(0,len(x_axis)):
    fig = go.Figure()
    a=x_axis[i]
    #st.write(dfxi[a])
    
    fig.add_trace(go.Scatter(x=dfyi['Label'], y=dfxi[a], 
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='Bubble Chart'))
    

    fig.update_layout(
        
            xaxis_title="Attacks",
    yaxis_title=a,
        xaxis = dict(
        tickmode = 'array',
        tickvals = [0 , 1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 , 14],
        ticktext = ['Benign', 'DDoS', 'PortScan', 'Bot attack', 'Infiltration', 'Web attack (Brute Force)','Web attack (XSS)','Web attack (SQL Injection)','FTP-Patator', 'SSH-Patator',
       'DoS slowloris', 'DoS Slowhttptest', 'DoS Hulk', 'DoS GoldenEye',
       'Heartbleed']
        )
        )
    

    time.sleep(2)



    st.plotly_chart(fig, use_container_width=True)
    





