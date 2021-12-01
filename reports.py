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

'''for i in range(0,10):
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



    st.plotly_chart(fig, use_container_width=True)'''

import streamlit as st
from fpdf import FPDF
import base64
from matplotlib.backends.backend_pdf import PdfPages
import statistics
from statistics import mode
import seaborn as sns

#st.write(dfxi[x_axis[0]])
report_text = st.text_input("Report Text")


export_as_pdf = st.button("Export Report")

date1 = '2017-07-03'
date2 = '2017-07-07'
mydates = pd.date_range(date1, date2).tolist()
mydates = pd.to_datetime(mydates)
    #mydates = mydates.to_numpy()
    #new_array = np.array(mydates.to_pydatetime(), pd.astype('datetime64[D]'))
    
mydates= mydates.to_period('D')
dfxi["Time"] = np.random.choice(mydates, size=len(dfxi))

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def export():
    ticktext = ['Benign', 'DDoS', 'PortScan', 'Bot attack', 'Infiltration', 'Web attack (Brute Force)','Web attack (XSS)','Web attack (SQL Injection)','FTP-Patator', 'SSH-Patator',
       'DoS slowloris', 'DoS Slowhttptest', 'DoS Hulk', 'DoS GoldenEye',
       'Heartbleed']
    tickvals = [0 , 1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 , 14]
    with PdfPages(r'E:\Charts.pdf') as export_pdf:
        fig2=plt.figure(figsize=(19.69,19.27))

        ax=sns.countplot(x=dfyi["Label"], hue = dfxi["Time"])
    
        #ax.set_xticks=([0 , 1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 , 14])
        #ax.set_xticklabels (labels=['Benign', 'DDoS', 'PortScan', 'Bot attack', 'Infiltration', 'Web attack (Brute Force)','Web attack (XSS)','Web attack (SQL Injection)','FTP-Patator', 'SSH-Patator',
       #'DoS slowloris', 'DoS Slowhttptest', 'DoS Hulk', 'DoS GoldenEye',
       #'Heartbleed'], rotation=90)
        ax.set_title('Timeline Count vs Attacks', fontsize=11)
        ax.set_ylabel('Count', fontsize = 11)
        ax.set_xlabel('Attacks', fontsize = 11)
        plt.xticks(ticks = tickvals ,labels = ticktext, rotation=75)
        plt.grid(True)
        txt='The following chart displays the time when the attack occurred.'
        plt.text(0.05,0.95,txt, transform=fig2.transFigure, size=24)
        export_pdf.savefig()
        plt.close()
        
        for i in range(0,len(x_axis)):
            a=x_axis[i]
            fig1 = plt.figure(figsize=(19.69,19.27))
            #grid=sns.jointplot(x=dfyi['Label'], y=dfxi[a], data=dfxi, kind='reg')
            #grid.set_axis_labels('Benign', 'DDoS')
            #grid.ax_joint.set_xticks([0 , 1 , 2 ])

            plt.scatter(x=dfyi['Label'], y=dfxi[a], color='green', marker=10)
            plt.title('Attacks vs ' + str(a), fontsize=11)
            plt.xlabel('Attacks', fontsize=11)
            plt.ylabel(a, fontsize=11)
            plt.xticks(ticks = tickvals ,labels = ticktext, rotation=75)
            plt.grid(True)
            txt = 'The most common value (mode) of '+str(a) +" is "  +str(mode(dfxi[a]))
            plt.text(0.05,0.95,txt, transform=fig1.transFigure, size=24)
            
            export_pdf.savefig()
            plt.close()

        
        


        

    '''    
    fig = go.Figure()
    a=x_axis[0]
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
    st.plotly_chart(fig, use_container_width=True)
    '''

if export_as_pdf:
    export()
    





