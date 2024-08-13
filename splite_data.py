import shutil
import random
import os

def split_data(img_folder, label_folder, train_ratio=0.8):
    img_files = [f for f in os.listdir(img_folder) if f.endswith('.jpg')]
    random.shuffle(img_files)
    
    train_count = int(len(img_files) * train_ratio)
    train_files = img_files[:train_count]
    val_files = img_files[train_count:]

    for split, files in zip(['train', 'val'], [train_files, val_files]):
        split_img_folder = os.path.join('data', split, 'images')
        split_label_folder = os.path.join('data', split, 'labels')
        os.makedirs(split_img_folder, exist_ok=True)
        os.makedirs(split_label_folder, exist_ok=True)
        
        for file in files:
            shutil.copy(os.path.join(img_folder, file), split_img_folder)
            label_file = file.replace('.jpg', '.txt')
            label_path = os.path.join(label_folder, label_file)
            if os.path.exists(label_path):
                shutil.copy(label_path, split_label_folder)
            else:
                print(f"Label file {label_path} not found, skipping.")

# Example usage
img_folder = 'images'
label_folder = 'labels'
split_data(img_folder, label_folder)
