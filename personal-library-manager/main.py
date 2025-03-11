#type:ignore
import streamlit as st
import pandas as pd
import datetime
import json
import os


DATA_FILE = "library_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
        
    else:
        with open(DATA_FILE, 'w') as f:
            json.dump({"books": []}, f)
        return {"books": []}


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    st.set_page_config("📚 Personal Library Manager", page_icon="💻")
    st.title("📚 Personal Library Manager")
    st.subheader("Organize your book collection with ease")

   
    library_data = load_data()

    
    menu = ["Add Book", "View Library", "Edit Book", "Delete Book"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        st.header("Add a New Book")
        with st.form(key='add_book_form'):
            title = st.text_input("Book Title")
            author = st.text_input("Author")
            isbn = st.text_input("ISBN (optional)")
            genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Romance", "Other"])
            status = st.selectbox("Status", ["To Read", "Reading", "Finished"])
            submit = st.form_submit_button(label="Add Book")

            if submit:
                if title and author:
                    new_book = {
                        "title": title,
                        "author": author,
                        "isbn": isbn,
                        "genre": genre,
                        "status": status,
                        "added_date": str(datetime.date.today())
                    }
                    library_data["books"].append(new_book)
                    save_data(library_data)
                    st.success(f"Added '{title}' to your library!")
                else:
                    st.error("Title and Author are required!")

    
    elif choice == "View Library":
        st.header("Your Library")
        
        if not library_data["books"]:
            st.info("Your library is empty. Add some books!")
        else:
            status_filter = st.multiselect(
                "Filter by Status",
                ["To Read", "Reading", "Finished"],
                default=["Reading"]
            )
            
            for book in library_data["books"]:
                if book["status"] in status_filter:
                    with st.container():
                        st.markdown(f"""
                        <div class="book-card" style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
                            <h3>{book['title']}</h3>
                            <p><b>Author:</b> {book['author']}</p>
                            <p><b>Genre:</b> {book['genre']}</p>
                            <p><b>Status:</b> {book['status']}</p>
                            <p><b>Added:</b> {book['added_date']}</p>
                            {"<p><b>ISBN:</b> " + book['isbn'] + "</p>" if book['isbn'] else ""}
                        </div>
                        """, unsafe_allow_html=True)

            
            st.subheader("Library Stats")
            total_books = len(library_data["books"])
            status_counts = pd.DataFrame(library_data["books"])["status"].value_counts()
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Books", total_books)
            col2.metric("Reading", status_counts.get("Reading", 0))
            col3.metric("Finished", status_counts.get("Finished", 0))

    elif choice == "Edit Book":
        st.header("Edit a Book")
        if library_data["books"]:
            titles = [book["title"] for book in library_data["books"]]
            selected_title = st.selectbox("Select Book to Edit", titles)
            
            book_to_edit = next(book for book in library_data["books"] if book["title"] == selected_title)
            
            with st.form(key='edit_book_form'):
                new_title = st.text_input("Book Title", value=book_to_edit["title"])
                new_author = st.text_input("Author", value=book_to_edit["author"])
                new_isbn = st.text_input("ISBN", value=book_to_edit["isbn"])
                new_genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Romance", "Other"], 
                                       index=["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Romance", "Other"].index(book_to_edit["genre"]))
                new_status = st.selectbox("Status", ["To Read", "Reading", "Finished"],
                                        index=["To Read", "Reading", "Finished"].index(book_to_edit["status"]))
                submit_edit = st.form_submit_button(label="Update Book")

                if submit_edit:
                    book_to_edit.update({
                        "title": new_title,
                        "author": new_author,
                        "isbn": new_isbn,
                        "genre": new_genre,
                        "status": new_status
                    })
                    save_data(library_data)
                    st.success(f"Updated '{new_title}' successfully!")
        else:
            st.info("No books to edit. Add some books first!")

    elif choice == "Delete Book":
        st.header("Delete a Book")
        if library_data["books"]:
            titles = [book["title"] for book in library_data["books"]]
            selected_title = st.selectbox("Select Book to Delete", titles)
            
            if st.button("Delete Book", key="delete"):
                library_data["books"] = [book for book in library_data["books"] if book["title"] != selected_title]
                save_data(library_data)
                st.success(f"Deleted '{selected_title}' from your library!")
        else:
            st.info("No books to delete. Add some books first!")

if __name__ == "__main__":
    main()
