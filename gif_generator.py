import os
import shutil
from PIL import Image 
from functions import create_directory
from function_second import random_items_complex_list, purge_directory_content, copy_files_from_directories_list

path_lecture = ""
transitory_path = ""
transitory_name = transitory_path.split("/")[-1]
lecture_name = path_lecture.split("/")[-1]
path_to_scrap = ""
images_number_by_serie = 10
pic_broadness = 250

'''
What you need :
==> Directories containing pictures
    -> For the same serie you need this pattern NAME_SUBNAME
    -> One shot : NAME is enough  
'''
 
def complex_lecture(images_destination_path, images_targeted, galeries_number=20):
    # Generate a list of directories in the general directory
    temp_folders_list = [i for i in os.listdir(images_destination_path) if 'temp' in i]
    # Delete all temp file with the following pattern 'temp'
    for k in temp_folders_list:
        shutil.rmtree(f"{images_destination_path}/{k}")
    # List all folders containing images
    folder_list = [item for item in os.listdir(images_targeted)]
    # Determine the series number
    series_nb = len(set([folder.split('_')[0] for folder in folder_list]))
    # Increment for the temp directory (pattern -> temp_n)
    n = 1
    ### Start of the loop ######################################################
    while series_nb >= galeries_number:
        series_list = set([folder.split('_')[0] for folder in folder_list])
        series_nb = len(series_list)
        # Generate a list of a number of directories in the previous list
        old_list, lecture_list = random_items_complex_list(galeries_number, folder_list)
        # Update the folder list
        folder_list = old_list
        # Setup the temp directory path and directory name
        temp_path = f"{images_destination_path}/temp_{n}"
        temp_directory = f"temp_{n}"
        # Create the directory
        create_directory(temp_path, temp_directory)
        # If the directory already exists empty lecture directory
        purge_directory_content(temp_path)
        print()
        print('=== Copy files Process =======================================')
        # Proceed to copy images of the chosen directories
        copy_files_from_directories_list(lecture_list, images_targeted,temp_path)
        # Display the number of images in the lecture directory
        print("Pics number :" ,len([image for image in os.listdir(temp_path)]))
        # Increment of 1 for the next directory
        n += 1
        
def gif_generator(folder_pattern, folders_path, b_size, gif_destination):
    # List of temp directories
    temp_folders_list = [i for i in os.listdir(folders_path) if folder_pattern in i]
    print()
    print('=== Gif Generator Process ====================================')
    # Loop on each folder to generate gifs
    for _temp_folder in temp_folders_list:
        _temp_folder_path = f"{folders_path}/{_temp_folder}"
        _my_gal=[i for i in os.listdir(_temp_folder_path) \
                if "jpg" in i or "png" in i ]
        # Sort the list -> ascending
        _my_gal.sort()
        # Create an empty list for future pics
        _images = []
        print(f"Operating in {_temp_folder_path}...")
        # Open, resize and convert each pics
        for _pic in _my_gal:
            _foo = Image.open(f"{_temp_folder_path}/{_pic}")
            # Check the size of the picture
            _l,_h = _foo.size  # (1920, 1080)
            _l_goal = b_size
            # Calcul the new height
            _new_h = int(_l_goal*_h/_l)
            # Resize the picture
            _foo = _foo.resize((_l_goal,_new_h))
            # Convert the dolor for pdf conversion
            _foo = _foo.convert('RGB')
            _images.append(_foo)
        # Path of the gif file
        _gif_path = f"{gif_destination}/{_temp_folder}.gif"
        print(f"Generating the {_temp_folder}.gif...")
        # Create the gif
        _images[0].save(_gif_path, format="GIF", append_images=_images,
                save_all=True, duration=200, loop=0)
        print(f"{_temp_folder}.gif created...")
        # Delete the temp directory
        shutil.rmtree(_temp_folder_path)

if __name__ == "__main__":
    # Start the process
    # Build the architecture
    complex_lecture(transitory_path, path_to_scrap, images_number_by_serie)
    # Generate GIFs
    gif_generator("temp", transitory_path, pic_broadness, path_lecture)
    
    