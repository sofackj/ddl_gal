import os
import requests

# Create a directory
def create_directory(directory_path, folder_name):
    try:
        os.mkdir(directory_path)
        print(f"{folder_name} directory created successfully!")
    except OSError as error:
        print(f"Error creating directory: {error}")
        print("Process with the existing directory")

# Download pic one at a time
def download_img(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
            print("Image saved as", filename)
    else:
        print("Failed to download image")

# Number of zeros
def normalized_number(number, length):
    new_str = str(number)
    while len(new_str) < length:
        new_str = "0" + new_str
    return new_str
