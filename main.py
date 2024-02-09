import cv2
import torch
import time
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

from ultralytics import YOLO

class YOLOVideoTransformer(VideoTransformerBase):
    def __init__(self, client, number):
        self.model = YOLO('best.pt').autoshape()  # Load YOLO model
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.client = client
        self.number = number
        self.message_sent = False
        self.fire_detected_time = None

    def transform(self, frame):
        detections = self.model(frame, conf=0.6)[0]  # Run fire detection
        detections_fire = []

        for detection in detections:
            x1, y1, x2, y2, score, class_id = detection
            if class_id == 0:  # Assuming fire class is 0
                detections_fire.append([x1, y1, x2, y2, score])

        # Draw bounding boxes for fire detections
        for fire_box in detections_fire:
            x1, y1, x2, y2, _ = fire_box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            cv2.putText(frame, 'Fire', (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            # Send message if fire detected
            if not self.message_sent:
                self.send_message(content="Alert, I think There is a fire!!!")
                self.message_sent = True

            # If fire detected, start timer
            if self.fire_detected_time is None:
                self.fire_detected_time = time.time()

            # Send message indicating fire detection if not sent already
            if time.time() - self.fire_detected_time >= 10:
                self.send_message(content="Alert, Fire still detected after 5 seconds!!!")
                self.fire_detected_time = None  # Reset timer

        return frame

    def send_message(self, content):
        # Send message via Twilio
        message = self.client.messages.create(
            from_='whatsapp:+14155238886',
            body=content,
            to=self.number
        )


def main():
    st.title('Fire Detection with YOLO and Streamlit')

    number = "YOUR_PHONE_NUMBER"
    client = "YOUR_TWILIO_CLIENT"  # Initialize your Twilio client here

    webrtc_ctx = webrtc_streamer(key="fire-detection", video_transformer_factory=YOLOVideoTransformer, client=client, number=number)

    if not webrtc_ctx.video_transformer:
        st.warning("Please allow access to your camera.")

    st.write('OpenCV window is not needed anymore. Just use the camera feed above!')

if __name__ == "__main__":
    main()
