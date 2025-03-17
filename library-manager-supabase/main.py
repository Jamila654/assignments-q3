#type:ignore
import streamlit as st
import sqlite3
import hashlib

def init_db():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        read_status TEXT DEFAULT 'Unread',  -- New column: Reading or Unread or Finished
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)''')
    conn.commit()
    return conn

if "db" not in st.session_state:
    st.session_state.db = init_db()
if "user_id" not in st.session_state:
    st.session_state.user_id = None

def register_user(username, password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    try:
        st.session_state.db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        st.session_state.db.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(username, password):
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    result = st.session_state.db.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, hashed_pw)).fetchone()
    return result[0] if result else None

def add_book(title, author, user_id, read_status="Unread"):
    st.session_state.db.execute("INSERT INTO books (title, author, user_id, read_status) VALUES (?, ?, ?, ?)", 
                                (title, author, user_id, read_status))
    st.session_state.db.commit()

def get_books(user_id):
    return st.session_state.db.execute("SELECT id, title, author, read_status FROM books WHERE user_id = ?", (user_id,)).fetchall()

def update_book(book_id, title, author, read_status, user_id):
    if st.session_state.db.execute("SELECT 1 FROM books WHERE id = ? AND user_id = ?", (book_id, user_id)).fetchone():
        st.session_state.db.execute("UPDATE books SET title = ?, author = ?, read_status = ? WHERE id = ?", 
                                    (title, author, read_status, book_id))
        st.session_state.db.commit()
        return True
    return False

def delete_book(book_id, user_id):
    if st.session_state.db.execute("SELECT 1 FROM books WHERE id = ? AND user_id = ?", (book_id, user_id)).fetchone():
        st.session_state.db.execute("DELETE FROM books WHERE id = ?", (book_id,))
        st.session_state.db.commit()
        return True
    return False

def search_books(query, user_id):
    return st.session_state.db.execute("SELECT id, title, author, read_status FROM books WHERE user_id = ? AND (title LIKE ? OR author LIKE ?)", 
                                      (user_id, f"%{query}%", f"%{query}%")).fetchall()

def get_read_status(user_id):
    total = len(get_books(user_id))
    reading = len([b for b in get_books(user_id) if b[3] == "Reading"])
    unread = len([b for b in get_books(user_id) if b[3] == "Unread"])
    finished = len([b for b in get_books(user_id) if b[3] == "Finished"])
    return total, reading, unread, finished


def library_manager():
    
    total, reading, unread, finished = get_read_status(st.session_state.user_id)
    st.sidebar.write(f"**User ID:** {st.session_state.user_id}")
    st.sidebar.write(f"**Total Books:** {total}")
    if st.sidebar.button("Logout", key="logout"):
        st.session_state.user_id = None
        st.session_state.view = "Login"
        st.rerun()

    
    if "view" not in st.session_state or st.session_state.view not in ["Add", "View", "Update", "Delete", "Search"]:
        st.session_state.view = "View"
    menu = ["Add", "View", "Update", "Delete", "Search"]
    st.session_state.view = st.sidebar.radio("**Menu**", menu, index=menu.index(st.session_state.view))

    
    with st.container():
        st.markdown("<h1 style='text-align: center; color: #2c3e50;'>📚 Personal Library</h1>", unsafe_allow_html=True)
        if st.session_state.view == "Add":
            st.subheader("Add Book")
            with st.form("add_form", clear_on_submit=True):
                title = st.text_input("Title")
                author = st.text_input("Author")
                read_status = st.selectbox("Read Status", ["Unread", "Reading", "Finished"])
                if st.form_submit_button("Add"):
                    if title and author:
                        add_book(title, author, st.session_state.user_id, read_status)
                        st.success("Book added!")
                    else:
                        st.error("Fill all fields!")

        elif st.session_state.view == "View":
            st.subheader("Your Books")
            books = get_books(st.session_state.user_id)
            if books:
                for id, title, author, status in books:
                    st.markdown(f"**ID:** {id} | **Title:** {title} | **Author:** {author} | **Status:** {status}")
            else:
                st.info("No books yet. Add some!")

        elif st.session_state.view == "Update":
            st.subheader("Update Book")
            with st.form("update_form"):
                book_id = st.number_input("Book ID", min_value=1, step=1)
                title = st.text_input("New Title")
                author = st.text_input("New Author")
                read_status = st.selectbox("Read Status", ["Unread", "Reading", "Finished"])
                if st.form_submit_button("Update"):
                    if title and author:
                        if update_book(book_id, title, author, read_status, st.session_state.user_id):
                            st.success("Book updated!")
                        else:
                            st.error("Book not found or not yours!")
                    else:
                        st.error("Fill all fields!")

        elif st.session_state.view == "Delete":
            st.subheader("Delete Book")
            with st.form("delete_form"):
                book_id = st.number_input("Book ID", min_value=1, step=1)
                if st.form_submit_button("Delete"):
                    if delete_book(book_id, st.session_state.user_id):
                        st.success("Book deleted!")
                    else:
                        st.error("Book not found or not yours!")

        elif st.session_state.view == "Search":
            st.subheader("Search Books")
            query = st.text_input("Search by title or author")
            if query:
                results = search_books(query, st.session_state.user_id)
                if results:
                    for id, title, author, status in results:
                        st.markdown(f"**ID:** {id} | **Title:** {title} | **Author:** {author} | **Status:** {status}")
                else:
                    st.info("No matches found.")

def main():
    st.set_page_config(page_title="Library Manager", page_icon="📖", layout="centered")
    if st.session_state.user_id is None:
        with st.container():
            st.markdown("<h1 style='text-align: center; color: #2c3e50;'>📚 Welcome to BookHaven</h1>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["Login", "Register"])
            with tab1:
                with st.form("login_form"):
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    if st.form_submit_button("Login"):
                        user_id = login_user(username, password)
                        if user_id:
                            st.session_state.user_id = user_id
                            st.session_state.view = "View"
                            st.rerun()
                        else:
                            st.error("Invalid credentials or user not found.")
            with tab2:
                with st.form("register_form", clear_on_submit=True):
                    new_user = st.text_input("New Username")
                    new_pass = st.text_input("New Password", type="password")
                    if st.form_submit_button("Register"):
                        if register_user(new_user, new_pass):
                            st.success("Registered! Please login.")
                        else:
                            st.error("Username taken!")
    else:
        library_manager()

if __name__ == "__main__":
    main()