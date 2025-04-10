#type:ignore
import streamlit as st
import hashlib
import os
import json
from cryptography.fernet import Fernet


def load_key():
    if os.path.exists("key.json"):
        with open("key.json", "r") as f:
            key_data = json.load(f)
            return key_data["key"].encode() 
    else:
        key = Fernet.generate_key()
        with open("key.json", "w") as f:
            json.dump({"key": key.decode()}, f)  
        return key

key = load_key()
cipher = Fernet(key)

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "users" not in st.session_state:
    st.session_state.users = load_users()
if "stored_data" not in st.session_state:
    st.session_state.stored_data = load_data()
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "page" not in st.session_state:
    st.session_state.page = "Login" 

st.set_page_config(layout="wide", page_title="Secure Data App", page_icon=":lock:")
st.title("Secure Data Encryption App")
st.sidebar.title("Navigation")


if st.session_state.current_user is None:
    st.session_state.page = st.sidebar.selectbox("Choose an action", ["Login", "Sign Up"], key="not_logged_in")
    if st.session_state.page == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            hashed_pw = hash_password(password)
            if username in st.session_state.users and st.session_state.users[username] == hashed_pw:
                st.session_state.current_user = username
                st.session_state.attempts = 0
                st.session_state.page = "Home"
                st.success(f"Welcome, {username}!")
            else:
                st.error("Wrong username or password!")
    elif st.session_state.page == "Sign Up":
        st.subheader("Sign Up")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm password", type="password")
        if st.button("Sign Up"):
            if new_username and new_password and confirm_password:
                if new_username in st.session_state.users:
                    st.error("Username already exists!")
                elif new_password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    hashed_pw = hash_password(new_password)
                    st.session_state.users[new_username] = hashed_pw
                    save_users(st.session_state.users)
                    st.success("Account created successfully!")
            else:
                st.error("Please fill in all fields.")

else:
    st.write(f"Logged in as {st.session_state.current_user}")
    st.session_state.page = st.sidebar.selectbox("Choose an action", ["Home", "Insert Data", "Retrieve Data", "Logout"], key="logged_in")
    if st.session_state.page == "Home":
        st.subheader("Home")
        st.write("Welcome! Pick an option from the sidebar!")
    elif st.session_state.page == "Insert Data":
        st.subheader("Store New Data")
        data = st.text_area("Enter your data here:")
        passkey = st.text_input("Enter your passkey:", type="password")
        if st.button("Store Data"):
            if data and passkey:
                encrypted_data = cipher.encrypt(data.encode()).decode()
                hashed_passkey = hash_password(passkey)
                user_data = st.session_state.stored_data.get(st.session_state.current_user, {})
                data_id = f"data{len(user_data) + 1}"
                user_data[data_id] = {"data": encrypted_data, "passkey": hashed_passkey}
                st.session_state.stored_data[st.session_state.current_user] = user_data
                save_data(st.session_state.stored_data)
                st.success(f"Stored as {data_id}")
            else:
                st.error("Enter both data and passkey!")
    elif st.session_state.page == "Retrieve Data":
        st.subheader("Retrieve Data")
        data_id = st.text_input("Enter the ID of the data you want to retrieve (e.g., data1):")
        passkey = st.text_input("Enter your passkey:", type="password")
        st.write(f"Failed attempts: {st.session_state.attempts}/3")
        if st.button("Retrieve Data"):
            if data_id and passkey:
                user_data = st.session_state.stored_data.get(st.session_state.current_user, {})
                if data_id in user_data:
                    stored = user_data[data_id]
                    if hash_password(passkey) == stored["passkey"]:
                        decrypted_data = cipher.decrypt(stored["data"].encode()).decode()
                        st.success("Here’s your data:")
                        st.write(decrypted_data)
                        st.session_state.attempts = 0
                    else:
                        st.session_state.attempts += 1
                        st.error("Wrong passkey!")
                        if st.session_state.attempts >= 3:
                            st.session_state.current_user = None
                            st.session_state.page = "Login"
                            st.error("Too many tries! Logging you out.")
                else:
                    st.error("Data ID not found!")
            else:
                st.error("Please enter both data ID and passkey!")
    elif st.session_state.page == "Logout":
        st.session_state.current_user = None
        st.session_state.page = "Login"
        st.success("Logged out successfully!")

