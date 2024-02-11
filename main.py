import cv2
from ultralytics import YOLO
import time
import streamlit as st
from twilio.rest import Client
from twilio.base.exceptions import TwilioException
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

class VideoTransformer(VideoTransformerBase):
    def __init__(self, threshold, account_sid, auth_token, to_number):
        self.model = YOLO('best.pt')
        self.threshold = threshold
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.to_number = to_number
        self.last_message_time = 0  # To keep track of the time when the last message was sent

    def transform(self, frame):
        frame = frame.to_ndarray(format="bgr24")

        fire_detection = self.model(frame, conf=self.threshold)[0]

        detections_fire = []

        for detections in fire_detection.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detections
            detections_fire.append([x1, y1, x2, y2, score])

        # Check if any fire detections are present
        if detections_fire:
            for fire_box in detections_fire:
                x1, y1, x2, y2, _ = fire_box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                cv2.putText(frame, 'Fire', (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            # Send message with delay
            current_time = time.time()
            if current_time - self.last_message_time > 10:  # Check if 10 seconds have passed since the last message
                try:
                    self.send_message()
                    self.last_message_time = current_time  # Update the last message time
                except TwilioException as e:
                    st.error(f"Twilio Exception: {e}")

        return frame

    def send_message(self):
        if not self.account_sid or not self.auth_token or not self.to_number:
            raise ValueError("Twilio credentials and phone numbers are required.")

        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Fire detected! Your attention is required.',
            to='whatsapp:' + self.to_number
        )
        print("Message sent successfully.")

def main():
    st.title('Fire Detection with YOLO and Streamlit')

    # Initialize your Twilio client here
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    to_number = st.text_input("Recipient's Number with country code")

    # Create instance of VideoTransformer
    video_transformer = VideoTransformer(threshold=0.5, account_sid=account_sid, auth_token=auth_token, to_number=to_number)
    
    token = client.tokens.create()

    # Display the video stream and fire detection
    webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=lambda: video_transformer, rtc_configuration={
      "iceServers": token.ice_servers
  })

    if not webrtc_ctx.video_transformer:
        st.warning("Please allow access to your camera.")

    st.write('OpenCV window is not needed anymore. Just use the camera feed above!')

if __name__ == "__main__":
    main()
