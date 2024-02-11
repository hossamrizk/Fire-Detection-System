import streamlit as st
from pages import home_page, model_page, try_page, feedback_page


def main():
    # Page configuration
    st.set_page_config(
        page_title="Fire Detection System",
        page_icon="🔥",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar navigation
    st.sidebar.title("Navigate")
    page_option = ["Home", "Model and Data", "Try it!", "Feedback"]
    selected_page = st.sidebar.radio("Go to", page_option)

    # Display selected page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Model and Data":
        model_page()
    elif selected_page == "Try it!":
        try_page()
    elif selected_page == "Feedback":
        feedback_page()



if __name__ == "__main__":
    main()
