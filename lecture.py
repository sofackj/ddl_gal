import os
import personnal_data
from functions import create_directory
from function_second import random_items_from_list, purge_directory_content, copy_files_from_directories_list

path_base = personnal_data.path_nxts
path_lecture = personnal_data.lecture_path
lecture_name = personnal_data.lecture_path.split("/")[-1]
path_to_scrap = personnal_data.tfnxt_path

# Function to provision the lecture directory
def apply_lecture(images_destination_path, images_destination_name, images_targeted, galeries_number=20):
    # Create the directory
    create_directory(images_destination_path, images_destination_name)
    # If the directory already exists empty lecture directory
    purge_directory_content(images_destination_path)
    # Generate a list of directories in the general directory
    folder_list = [item for item in os.listdir(images_targeted)]
    # Generate a list of a number of directories in the previous list
    old_list, lecture_list = random_items_from_list(galeries_number, folder_list)
    # Proceed to copy images of the chosen directories
    copy_files_from_directories_list(lecture_list, images_targeted,images_destination_path)
    # Display the number of images in the lecture directory
    print(len([image for image in os.listdir(images_destination_path)]))

if __name__ == "__main__":
    # Start the process
    apply_lecture(path_lecture, lecture_name, path_to_scrap, 20)
