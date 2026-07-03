import os
import shutil

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

os.makedirs(destination_folder, exist_ok=True)
for file in os.listdir(source_folder):

    if file.endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(file, "moved successfully")

print("All JPG files moved!")
