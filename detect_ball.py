import torch
from PIL import Image, ImageDraw

def detect_balls(model_path, img_path):
    # Load the YOLO model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, source='local')

    # Load the image
    img = Image.open(img_path)

    # Perform inference
    results = model(img_path)

    # Get bounding boxes and labels
    bbox_list = results.xyxy[0].cpu().numpy()  # xyxy format
    labels = results.names

    # Draw bounding boxes on the image
    draw = ImageDraw.Draw(img)
    for bbox in bbox_list:
        xmin, ymin, xmax, ymax, conf, cls = bbox
        label = labels[int(cls)]
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)
        draw.text((xmin, ymin), f"{label} {conf:.2f}", fill="red")

    # Show the image
    img.show()

# Example usage
model_path = 'runs/train/exp10/weights/best.pt'  # Path to your trained model
img_path = 'images/frame0000.jpg'  # Path to the image you want to test
detect_balls(model_path, img_path)
