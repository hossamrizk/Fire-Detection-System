import ultralytics
from ultralytics import YOLO
import cv2
import torch
import time

def send_message(content, to_number, client):
    # Send message via Twilio
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=content,
        to=to_number
    )

def detect_fire(number, client):
    # Flag to track if message has been sent
    message_sent = False

    # CUDA if available, CPU otherwise
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load YOLO model
    model = YOLO('best.pt').to(device)

    cap = cv2.VideoCapture(0)
    fire_detected_time = None  # Initialize fire detection time
    while True:
        # Read frame from camera
        ret, frame = cap.read()

        if ret:
            # Convert frame from BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Run fire detection
            fire_detection = model(frame, conf=0.6)[0]

            detections_fire = []

            for detections in fire_detection.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = detections
                detections_fire.append([x1, y1, x2, y2, score])

            # Draw Bounding Box
            for fire_box in detections_fire:
                x1, y1, x2, y2, _ = fire_box
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                cv2.putText(frame, 'Fire', (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                # Send message if fire detected
                if not message_sent:
                    send_message(content="Alert, I think There is a fire!!!", to_number=number, client=client)
                    message_sent = True

                # If fire detected, start timer
                if fire_detected_time is None:
                    fire_detected_time = time.time()

                    # Send message indicating fire detection if not sent already
                if time.time() - fire_detected_time >= 10:
                    send_message(content="Alert, Fire still detected after 5 seconds!!!", to_number=number, client=client)
                    fire_detected_time = None  # Reset timer

            # Display the frame with bounding boxes and labels.
            cv2.imshow('Fire Detection Result', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

