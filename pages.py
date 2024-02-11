import streamlit as st
from streamlit_webrtc import webrtc_streamer
import pandas as pd
from main import VideoTransformer
from twilio.rest import Client


account_sid = st.text_input("Enter your Twilio Account SID:")
auth_token = st.text_input("Enter your Twilio Auth Token:", type='password')
to_number = st.text_input("Recipient's Number with country code")
threshold = st.slider("Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

client = Client(account_sid, auth_token)
token = client.tokens.create()

def home_page():

    # Sidebar
    with st.sidebar:
        if st.sidebar.button("Contact me"):
            st.sidebar.markdown(
                """
                **Contact:-**\n
                *Hossam El-Dein Rizk*\n
                *Computer Vision Engineer*\n
                hossamrizk048@gmail.com\n
                [linkedin](https://www.linkedin.com/in/hossamrizk10/)
                [Github](https://github.com/hossamrizk)
                [Kaggle](https://www.kaggle.com/hossamrizk)
                """
            )
    st.title("Welcome to the Fire Detection and Alert System")
    st.write("**Empowering Safety, Protecting Lives**")
    st.write(
        "Welcome to my online platform dedicated to fire detection and alert system. I`m committed to leveraging technology to enhance safety and protect lives in our communities.")

    st.header("Who am I?")
    st.write(
        "I'm Hossam Eldein Rizk, a fresh graduate from the Faculty of Artificial Intelligence. Passionate about leveraging cutting-edge technologies to solve real-world problems, I am excited to embark on a journey of exploration and learning in the field of AI.")

    st.header("Problem Statement:")
    st.write(
        "The existing fire detection methods often lack accuracy, speed, and scalability, leaving communities vulnerable to fire hazards. Traditional systems rely heavily on manual intervention or outdated technology, resulting in delayed response times and increased damage.")

    st.header("Solution Approach:")
    st.write(
        "Inspired by advancements in machine learning and real-time data analysis, I envisioned a comprehensive Fire Detection and Alert System that could swiftly identify and alert authorities about potential fire incidents. By harnessing the power of computer vision algorithms and live video analysis, the system would provide early detection capabilities, enabling prompt action and minimizing the impact of fires.")

    st.header("Project Objectives:")
    st.write("""
    - Develop a robust machine learning model capable of accurately detecting fires in images or video streams.
    - Implement real-time monitoring and analysis to enable swift detection and alerting of fire incidents.
    - Design an intuitive user interface for easy access and interaction with the system.
    - Collaborate with stakeholders to gather feedback, iterate on the solution, and ensure alignment with community needs.
        """)

    st.header("Expected Impact:")
    st.write(
        "The Fire Detection and Alert System aims to revolutionize fire safety measures by providing proactive detection capabilities, reducing response times, and ultimately saving lives and property. By leveraging AI technologies, the project seeks to empower communities with the tools and resources needed to prevent and mitigate fire disasters effectively.")

def model_page():
    # Sidebar
    with st.sidebar:
        if st.sidebar.button("Contact me"):
            st.sidebar.markdown(
                """
                **Contact:-**\n
                *Hossam El-Dein Rizk*\n
                *Computer Vision Engineer*\n
                hossamrizk048@gmail.com\n
                [linkedin](https://www.linkedin.com/in/hossamrizk10/)
                [Github](https://github.com/hossamrizk)
                [Kaggle](https://www.kaggle.com/hossamrizk)
                """
            )
    st.write("# Model and Data")

    st.write("**Fire Detection Model:**")
    st.write("The fire detection model is built using state-of-the-art machine learning techniques to accurately identify and classify instances of fire in video streams. Here's an overview of the key components of our model:")
    st.write("- **Architecture:** The model utilizes a You Only Look Once(YOLO) architecture, which is well-suited for detection tasks.")
    st.write("""- **Training Data:** I trained the model on a free dataset of images containing both fire and non-fire scenes. You can use another data if you want.
                But in case you want to get the data which I used, [here](https://universe.roboflow.com/-jwzpw/continuous_fire/dataset/6) """)
    st.write("- **Training Process:** The model was trained on Kaggle website to take benefits of the free gpu. Feel free to use any platform you want, It dosen`t matter.")
    st.write("- **Accuracy and Performance:** The model was trained on 80 epochs only.The score of mAP50 is 0.90 and score of mAP50-95 is 0.663. I think if I trained it on more epochs it will give a better accuracy.")
    st.write("- **Whatsapp message Part:** In order to sending the message via whatsapp I used twilio library. It`s free, all you need is to create an account on the website and get your account information like account id and auth token." )

    st.write("- **Visualizations:** Here is a selectbox contains different plots from the model, So you can see how the model performing")

    # Select Box
    option = st.selectbox(
        "**Please chose which graph do you want to see**",

        ["Confusion matrix",
         "Normalized confusion matrix",
         "F1 curve",
         "Precision curve",
         "Recall curve",
         "Precision-Recall curve",
         "Results plots",
         "Results.csv"],

        index=None,
        placeholder= "Choose Plot"
    )

    if option == "Confusion matrix":
        st.image('images/confusion_matrix.png',caption='Confusion matrix')

    elif option == 'Normalized confusion matrix':
        st.image('images/confusion_matrix_normalized.png', caption='Normalized confusion matrix')

    elif option == 'F1 curve':
        st.image('images/F1_curve.png', caption='F1 curve')

    elif option == 'Precision curve':
        st.image('images/P_curve.png', caption='Precision curve')

    elif option == 'Recall curve':
        st.image('images/R_curve.png', caption='Recall curve')

    elif option == 'Precision-Recall curve':
        st.image('images/PR_curve.png', caption='Precision-Recall curve')

    elif option == 'F1 curve':
        st.image('images/F1_curve.png', caption='F1 curve')

    elif option == 'Results plots':
        st.image('images/results.png', caption='Results plots')


    elif option == 'Results.csv':
        df = pd.read_csv('images/results.csv')
        st.write("Take a detailed look at how our model was performing through the entire training process!")
        st.write(df)


import streamlit as st
from streamlit_webrtc import webrtc_streamer
from main import VideoTransformer

import streamlit as st
from streamlit_webrtc import webrtc_streamer
from main import VideoTransformer

def try_page():
    # Sidebar
    with st.sidebar:
        if st.sidebar.button("Contact me"):
            st.sidebar.markdown(
                """
                **Contact:-**\n
                *Hossam El-Dein Rizk*\n
                *Computer Vision Engineer*\n
                hossamrizk048@gmail.com\n
                [linkedin](https://www.linkedin.com/in/hossamrizk10/)
                [Github](https://github.com/hossamrizk)
                [Kaggle](https://www.kaggle.com/hossamrizk)
                """
            )

    # Main content
    st.title("Try a free demo here!")
    st.write("**Please note: This is a free demo, which does not contain all options or features and may not have optimal accuracy.**")
    st.write("""
    **Please note:** You must have an account on twilio before you can try this demo.
    If you don`t have one, you can create one using this [link](https://login.twilio.com/u/signup?state=hKFo2SBDSm45NjBsdzQxZElvLXZCeVBQWUdxdE1wOFAxb0FMeaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIDNOblY0OEE4dFFxV1kzb0EzazBWYzdQbzRRSEc4b1lfo2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks)\n
    After creating an account search for console dashboard, Then scroll down to get your Account SID and Auth Token\n
    Enter these informations, Finaly you will be able to try the demo!
    """)
    st.write("If you don`t enter the required information, you will face issues while running video. And the live video will stuck if it detect fire.\n"
             "So to avoid any problems please enter the required information first\n"
             )
    st.write("Thanks, I hope you like it. :)")

    # Input fields for Twilio credentials and threshold slider

    
    # Create instance of VideoTransformer
    video_transformer = VideoTransformer(threshold=threshold, account_sid=account_sid, auth_token=auth_token, to_number=to_number)
    

    # Display the video stream and fire detection
    webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=lambda: video_transformer, rtc_configuration={
      "iceServers": token.ice_servers
  })

    if not webrtc_ctx.video_transformer:
        st.warning("Please allow access to your camera.")



def feedback_page():
    # Sidebar
    with st.sidebar:
        if st.sidebar.button("Contact me"):
            st.sidebar.markdown(
                """
                **Contact:-**\n
                *Hossam El-Dein Rizk*\n
                *Computer Vision Engineer*\n
                hossamrizk048@gmail.com\n
                [linkedin](https://www.linkedin.com/in/hossamrizk10/)
                [Github](https://github.com/hossamrizk)
                [Kaggle](https://www.kaggle.com/hossamrizk)
                """
            )
    st.title("Feedback")
    st.write("I value your input!")
    st.write("Have questions or feedback? I'd love to hear from you! Reach me out for assistance, partnership opportunities, or to share your ideas and suggestions. Together, we can make a difference in fire safety.")
    st.write("Your feedback is crucial in helping me enhance the effectiveness and usability of my fire detection system.")
    st.write(
        "Thank you for visiting the Fire Detection and Alert System platform. Together, let's work towards a safer, fire-free future for all.")
