# Fire Detection System with YOLOv8 and Twilio Integration

Welcome to the Fire Detection System project! This repository contains code for a fire detection system using the YOLOv8 model and Twilio integration to alert users via WhatsApp in case of fire detection.

## Overview

This project aims to provide a simple yet effective solution for fire detection using computer vision techniques. It utilizes the YOLOv8 model, a state-of-the-art object detection algorithm, to detect the presence of fire in video streams. Once a fire is detected, the system sends a WhatsApp message to alert the user using the Twilio API.

## Features

- Fire detection using YOLOv8
- Integration with Twilio for real-time WhatsApp alerts
- Streamlit web application for easy user interaction
- Simple setup process requiring only Twilio account details

## Getting Started

To try out the fire detection system, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/hossamrizk/Fire-Detection-System.git

2. Install the necessary dependencies:
   
   ```bash
   pip install -r requirements.txt
   
3. Change directory to this repo
4. Run the Streamlit app

   ```bash
   streamlit run app.py

5. Create an account on [Twilio](https://www.twilio.com/en-us) and obtain your Account SID, Auth Token, and Twilio phone number.
6. In Try it page, write your accountid, auth token and your number.
7. Finaly you are able to try it!


## Disclaimer
This project is intended as a demonstration and study aid. It may not be suitable for production use without further development and testing. Please use caution when relying on automated systems for critical tasks such as fire detection. 
Feel free to explore the code and contribute to its improvement!
