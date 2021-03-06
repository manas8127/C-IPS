# import streamlit as st
# import subprocess

# def id_authenticated(username):
#     return username == "******"

# def pw_authenticated(password):
#     return password == "*****"

# def generate_login_block():
#     block1 = st.empty()
#     block2 = st.empty()
#     block3 = st.empty()
#     block4 = st.empty()
#     return block1, block2, block3, block4

# def clean_blocks(blocks):
#     for block in blocks:
#         block.empty()

# def login(blocks):
#     blocks[0].markdown("""
#         <style>
#             input {
#                 -webkit-text-security: none;
#             }
#         </style>
#         """, unsafe_allow_html=True)

#     blocks[0].markdown("""
#         <style>
#             input {
#                 -webkit-text-security: none;
#             }
#         </style>
#         """, unsafe_allow_html=True)

#     return blocks[1].text_input("Username:"), blocks[3].text_input('Password:', value = "", type = "password")

# login_blocks = generate_login_block()
# username, password = login(login_blocks)
# login_button = st.button("Log In")


# if login_button & id_authenticated(username) & pw_authenticated(password):
#     st.success("You are logged in")
#     subprocess.Popen(["streamlit", "run", "app.py"])
# elif login_button:
#     st.error("Please input valid username and/or password")


import streamlit as st
import pandas as pd
from datetime import *
import time
from streamlit.script_runner import StopException, RerunException
import subprocess
import pyautogui
from PIL import Image
img=Image.open('cips2.png')

st.set_page_config(page_title='C-IPS Login', page_icon=img)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	st.markdown("<h1 style='text-align: center; color: white;'>C-IPS</h1>", unsafe_allow_html=True)

	menu = ["LogIn","SignUp"]
	choice = st.selectbox("Menu",menu)

	if choice == "LogIn":
		

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		if st.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In successfully as {}".format(username))
				subprocess.Popen(["streamlit", "run", "app.py"])

				# task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				# if task == "Add Post":
				# 	st.subheader("Add Your Post")

				# elif task == "Analytics":
				# 	st.subheader("Analytics")
				# elif task == "Profiles":
				# 	st.subheader("User Profiles")
				# 	user_result = view_all_users()
				# 	clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
				# 	st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		st.info("Make changes to server whose ownership does not belong to you constitutes to un-ethical hacking and can lead to imprisonment under IT Act.")
		st.checkbox("I accept the terms and conditions")
		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created an account, this page will automatically refresh")
			time.sleep(1)
			#st.info("Go to Login Menu to login")
			pyautogui.hotkey('f5')
			



	


if __name__ == '__main__':
	main()