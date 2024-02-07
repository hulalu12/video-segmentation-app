import cv2
import numpy as np
from ultralytics import YOLO

# Import necessary libraries
import cv2
import numpy as np

# Load the YOLOv8 model
model = YOLO('./model/video-seg.pt')

# Open the video file
video_path = "./data/exercise.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run predict on the frame, persisting tracks between frames
        results = model.predict(frame, imgsz=(720,1280))
        masks = results[0].masks
        mask1 = masks[0]
        tensor_cpu = mask1.data[0].cpu()
        mask = tensor_cpu.numpy()
        new_mask = mask.astype(np.uint8)
        
        # Apply the mask to the frame
        image_frame = cv2.bitwise_and(frame, frame, mask=new_mask)
        
        # Display the frame with tracking
        cv2.imshow("Video Tracking", image_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
