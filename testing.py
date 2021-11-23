import time
import streamlit as st
import pyautogui


st.set_page_config(page_title='C-IPS Testing Panel')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>C-IPS Testing Panel</h1>", unsafe_allow_html=True)


def check(ip):
    iptype=ip.index('-')
    c=ip[iptype+2:]
    return c

values=['205.174.165.73 - Decoy','205.174.165.69 - Decoy','205.174.165.70 - Decoy','205.174.165.71 - Decoy', 
'85.237.172.55 - Normal Traffic',
'157.79.212.141 - Normal Traffic',
'197.23.92.143 - Normal Traffic',
'81.87.44.36 - Normal Traffic',
'228.131.54.49 - Normal Traffic',
'174.147.164.42 - Normal Traffic',
'6.16.43.120 - Normal Traffic',
'111.168.193.137 - Normal Traffic',
'144.3.229.250 - Normal Traffic',
'62.174.83.16 - Normal Traffic']

# i=values[0].index('-')
# c=values[0][i+2:]
# st.write(c)


options = list(range(len(values)))

value = st.selectbox("Select IP", options, format_func=lambda x: values[x])

col1, col2, col3 , col4 = st.columns(4)

with col1:
    pass
with col2:
    pass
with col3 :
    pass
with col4:
    button= st.button('Check Response')



if button:
    ch=check(values[value])
    if(ch == 'Decoy'):
        st.warning('Suspicious activity detected from this IP')
        time.sleep(10)
        pyautogui.hotkey('f5')
    elif(ch == 'Normal Traffic'):
        st.success('Normal traffic from this IP')

        
        
        
    

    



