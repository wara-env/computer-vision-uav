from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Read image
image = cv2.imread("bus.jpg")

# Run detection
results = model(image)

# Draw detection results
annotated_image = results[0].plot()

# Save result
cv2.imwrite("result.jpg", annotated_image)

print("Detection selesai!")
print("Hasil disimpan sebagai result.jpg")
