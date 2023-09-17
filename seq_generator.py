import os
import shutil
from PIL import Image 
from largefunctions import complex_lecture

path_lecture = ""
transitory_path = ""
transitory_name = transitory_path.split("/")[-1]
lecture_name = path_lecture.split("/")[-1]
path_to_scrap = ""
images_number_by_serie = 5
pic_broadness = 500

'''
What you need :
==> Directories containing pictures
    -> For the same serie you need this pattern NAME_SUBNAME
    -> One shot : NAME is enough  
'''

def seq_generator(folder_pattern, folders_path, b_size, gif_destination, pdf=True):
    if pdf:
        file_type = "pdf"
    else:
        file_type = "gif"
    # List of temp directories
    temp_folders_list = [i for i in os.listdir(folders_path) if "temp" in i]
    print()
    print(f'=== {file_type.upper()} Generator Process ====================================')
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
        _file_path = f"{gif_destination}/{folder_pattern}_{_temp_folder}.{file_type}"
        print(f"Generating the {folder_pattern}_{_temp_folder}.{file_type}...")
        if pdf:
            # Create the pdf
            _images[0].save(_file_path, f"{file_type.upper()}" ,resolution=200.0, \
                save_all=True, append_images=_images[1:])
        else:
            # Create the gif
            _images[0].save(_file_path, format=f"{file_type.upper()}", append_images=_images, \
                            save_all=True, duration=200, loop=0)
        print(f"{folder_pattern}_{_temp_folder}.{file_type} created...")
        # Delete the temp directory
        shutil.rmtree(_temp_folder_path)
        print('---------------------------------------------')


if __name__ == "__main__":
    # Start the process
    # Build the architecture
    complex_lecture(transitory_path, path_to_scrap, images_number_by_serie)
    # Generate GIFs
    seq_generator("temp", transitory_path, pic_broadness, path_lecture, True)
    pass