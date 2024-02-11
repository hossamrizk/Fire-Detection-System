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
        account_sid = st.text_input("Enter your Twilio Account SID:")
        auth_token = st.text_input("Enter your Twilio Auth Token:", type='password')
        to_number = st.text_input("Recipient's Number with country code")
        threshold = st.slider("Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
        try_page(account_sid, auth_token, to_number, threshold)
    elif selected_page == "Feedback":
        feedback_page()

if __name__ == "__main__":
    main()
