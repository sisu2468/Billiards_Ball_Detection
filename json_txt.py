import json
import os
from PIL import Image

# Define the width and height of your images
IMG_WIDTH = 640  # Set this to the actual width of your images
IMG_HEIGHT = 480  # Set this to the actual height of your images

def convert_json_to_yolo(json_file, img_folder, output_folder):
    with open(json_file) as f:
        data = json.load(f)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for item in data:
        frame = item['image']
        labels = item['annotations']

        # img_path = os.path.join(img_folder, frame)
        img_path = os.path.join(img_folder, frame)
        with Image.open(img_path) as img:
            img_width, img_height = img.size

        label_path = os.path.join(output_folder, frame.replace('.jpg', '.txt'))

        with open(label_path, 'w') as f:
            for label in labels:
                cls = label['label']
                bbox = label['coordinates']
                x_center = bbox['x'] / img_width
                y_center = bbox['y'] / img_height
                width = bbox['width'] / img_width
                height = bbox['height'] / img_height
                f.write(f"{cls} {x_center} {y_center} {width} {height}\n")

# Example usage
json_file = 'annotations.json'
img_folder = 'images'
output_folder = 'labels'
convert_json_to_yolo(json_file, img_folder, output_folder)
