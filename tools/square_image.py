import os
import cv2
import numpy as np

# Function to pad image if width > height
def pad_image(image):
    height, width, _ = image.shape
    if width > height:
        diff = width - height
        top = diff // 2
        bottom = diff - top
        padded_image = cv2.copyMakeBorder(image, top, bottom, 0, 0, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        return padded_image
    else:
        return image

# Input folder containing PNG files
input_folder = "./pub/"

# Output folder for processed images
output_folder = "./new_imgs/"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the list of PNG files in the input folder
png_files = [f for f in os.listdir(input_folder)]

# Process each PNG file
for file_name in png_files:
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)

    # Load the image
    image = cv2.imread(input_path)

    # Check if the image needs padding and pad it if necessary
    processed_image = pad_image(image)

    # Save the processed image to the output folder
    cv2.imwrite(output_path, processed_image)

print("Processing complete. Images saved in the output folder.")
