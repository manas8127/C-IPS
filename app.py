import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import time
from fpdf import FPDF
import base64
from matplotlib.backends.backend_pdf import PdfPages
import statistics
from statistics import mode
import seaborn as sns
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
mj=joblib.load('model_joblib_real_random_forest_fourteen')
df = pd.read_csv('x_test_fourteen.csv')

dfxi=df.iloc[0:100]
dfy = pd.read_csv(r'y_test_fourteen.csv')
dfyi=dfy.iloc[0:100]

date1 = '2017-07-03'
date2 = '2017-07-07'
mydates = pd.date_range(date1, date2).tolist()
mydates = pd.to_datetime(mydates)
    #mydates = mydates.to_numpy()
    #new_array = np.array(mydates.to_pydatetime(), pd.astype('datetime64[D]'))
    
mydates= mydates.to_period('D')
dfxi["Time"] = np.random.choice(mydates, size=len(dfxi))


k=0

x_axis=df.columns




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

            plt.scatter(x=dfyi['Label'], y=dfxi[a], s=500,c='blue')
            plt.title('Attacks vs ' + str(a), fontsize=11)
            plt.xlabel('Attacks', fontsize=11)
            plt.ylabel(a, fontsize=11)
            plt.xticks(ticks = tickvals ,labels = ticktext, rotation=75)
            plt.grid(True)
            txt = 'The most common value (mode) of '+str(a) +" is "  +str(mode(dfxi[a]))
            plt.text(0.05,0.95,txt, transform=fig1.transFigure, size=24)
            
            export_pdf.savefig()
            plt.close()


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
    export()
     


    




values=['205.174.165.73','205.174.165.69','205.174.165.70','205.174.165.71']





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

    

        



