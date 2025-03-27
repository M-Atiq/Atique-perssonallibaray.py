# Atique-perssonallibaray.py
this is a libaray management sys
import streamlit as st
import pandas as pd

# Initialize session state for storing books
if 'library' not in st.session_state:
    st.session_state.library = []

st.title("Personal Library Management")

# Form to add a book
with st.form("add_book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
    submit = st.form_submit_button("Add Book")
    
    if submit and title and author:
        st.session_state.library.append({"Title": title, "Author": author, "Genre": genre, "Year": int(year)})
        st.success(f'Book "{title}" added!')

# Display books
st.subheader("Library Collection")
if st.session_state.library:
    df = pd.DataFrame(st.session_state.library)
    st.dataframe(df)
else:
    st.info("No books added yet.")

# Search books
search_query = st.text_input("Search by Title or Author")
if search_query:
    results = [book for book in st.session_state.library if search_query.lower() in book["Title"].lower() or search_query.lower() in book["Author"].lower()]
    if results:
        st.subheader("Search Results")
        st.dataframe(pd.DataFrame(results))
    else:
        st.warning("No matching books found.")

# Delete books
if st.session_state.library:
    delete_title = st.selectbox("Select a book to delete", [book["Title"] for book in st.session_state.library])
    if st.button("Delete Book"):
        st.session_state.library = [book for book in st.session_state.library if book["Title"] != delete_title]
        st.success(f'Book "{delete_title}" deleted!')
        st.experimental_rerun()

