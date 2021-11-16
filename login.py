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
from time import *
from streamlit.script_runner import StopException, RerunException



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

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created an account, now refresh the page to LogIn")
			#st.info("Go to Login Menu to login")

	hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
	st.markdown(hide_st_style, unsafe_allow_html=True)


if __name__ == '__main__':
	main()