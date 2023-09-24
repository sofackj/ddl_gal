import os
import shutil
from random import random,shuffle
from functions import normalized_number, \
    data_setup, create_directory, check_url_request, \
        generate_img_urls, ddl_process, lines_list_in_txt
from function_second import purge_directory_content, \
    copy_files_from_directories_list, random_items_complex_list

def ddl_app(url, section_directory, root_path): 
    print()
    # Take the url and check the page status
    soup = check_url_request(url)
    # Check the value of soup is legit
    if soup:
        # gallery_section_directory
        final_path = f"{root_path}/{section_directory}"
        print(final_path)
        create_directory(final_path, section_directory)
        # Collect data
        family_pic_name, pic_path = data_setup(url, final_path)
        # Create directory
        if create_directory(pic_path, family_pic_name):
            # Find all furls for all targeted pics
            list_urls = generate_img_urls(soup, 'figure')
            print(f"Downloading images into {pic_path}")
            print()
            # Full process
            ddl_process(list_urls,pic_path,family_pic_name)
            print()
            # Check the numbers of downloaded pics
            print(f"Pics downloaded : {len(os.listdir(pic_path))}")
            print()
            return 1
        else:
            # If the directory already exists return 0 value for thr parent loop
            print("Process terminated !")
            print()
            return 0
    else:
        # If the directory already exists return 0 value for thr parent loop
        print(f"The URL doesn't fulfill the requirement for the process !\nURL : {url}")
        print()
        return 0

def sort_files_series(directory_to_sort, ext, prefix):
    # Pass from a pattern nnnnnn-number -> nnnnnn_number
    for new_file in [video for video in os.listdir(directory_to_sort) if ext in video and '-' in video]:
        os.rename(f"{directory_to_sort}/{new_file}", f"{directory_to_sort}/{'_'.join(new_file.split('-'))}")
    # Files to target
    _main_list = [video for video in os.listdir(directory_to_sort) if ext in video]
    # New files to sort
    _clips_list = [filename for filename in _main_list if filename.split('_')[0] != prefix]
    # Loop into files to convert
    while len(_clips_list) != 0:
        #
        _first_sample = _clips_list[0]
        #
        _pattern_sample = ''.join(_first_sample.split('_')[:-1])
        #
        _same_pattern_list = [file for file in _clips_list if ''.join(file.split('_')[:-1]) == _pattern_sample]
        #
        _clips_list = [file for file in _clips_list if ''.join(file.split('_')[:-1]) != _pattern_sample]
        #
        random_nb = int(random()*100000)
        _serial = normalized_number(random_nb,5)
        while _serial in list(set([file.split('_')[1] for file in _main_list if file.split('_')[0] == prefix])):
            random_nb = int(random()*100000)
            _serial = normalized_number(int(random()*100000),5)
        #
        for vid in _same_pattern_list:
            #
            os.rename(f"{directory_to_sort}/{vid}", f"{directory_to_sort}/{prefix}_{_serial}_{vid.split('_')[-1]}")

def complex_lecture(images_destination_path, images_targeted, pics_number=20, files_number=9, txt_file=False):
    # Generate a list of directories in the general directory
    temp_folders_list = [i for i in os.listdir(images_destination_path) if 'temp' in i]
    # Delete all temp file with the following pattern 'temp'
    for k in temp_folders_list:
        shutil.rmtree(f"{images_destination_path}/{k}")
    # List all folders containing images
    # if the list is in a txt file
    if txt_file:
        folder_list = lines_list_in_txt(images_targeted)
    # if the list is in the repertory
    else:
        folder_list = [item for item in os.listdir(images_targeted) if "." not in item]
    # print(folder_list)
    # Determine the series number
    # series_nb = len(set([("_").join(folder.split('_')[:-1]) if "_" in folder else folder for folder in folder_list]))
    series_nb = len(folder_list)
    # Increment for the temp directory (pattern -> temp_n)
    n = 1
    ### Start of the loop ######################################################
    while series_nb >= pics_number and n <= files_number:
        # Generate a list of a number of directories in the previous list
        old_list, lecture_list = random_items_complex_list(pics_number, folder_list)
        # Update the folder list
        folder_list = old_list
        # Setup the temp directory path and directory name
        temp_path = f"{images_destination_path}/temp_{n}"
        temp_directory = f"temp_{n}"
        print()
        print(f'=== Copy files Process <{n}> =======================================')
        # Create the directory
        create_directory(temp_path, temp_directory)
        # If the directory already exists empty lecture directory
        purge_directory_content(temp_path)
        # Proceed to copy images of the chosen directories
        copy_files_from_directories_list(lecture_list, images_targeted,temp_path)
        # Display the number of images in the lecture directory
        print("Pics number :" ,len([image for image in os.listdir(temp_path)]))
        # Increment of 1 for the next directory
        n += 1
        # Check the condition for the loop
        series_nb = len(set([folder.split('_')[0] for folder in folder_list]))
 
def clips_list_random_complex(clips_directory):
    _clips_list = [i for i in os.listdir(clips_directory)]
    shuffle(_clips_list)
    _copy_clip = _clips_list.copy()
    _my_clips = []
    _set_number = list(set(('').join(i.split('_')[:-1]) for i in _copy_clip))
    # Fill the clips list for the first condition in the loop
    #
    _first_clip = _copy_clip.pop(0)
    # Add the clip in the list
    _my_clips.append(_first_clip)
    # Remove the serie from the series list
    _set_number.remove(('').join(_first_clip.split('_')[:-1]))
    # Start of the loop
    while len(_copy_clip) > 0:
        # Remove the first clip of the list
        _chosen_clip = _copy_clip.pop(0)
        # Check the serie of the clip
        _chosen_serie = ('').join(_chosen_clip.split('_')[:-1])
        # if the serie's name is in the series list
        if _chosen_serie in _set_number and ('').join(_my_clips[-1].split('_')[:-1]) != _chosen_serie:
            # Add the clip in the list
            _my_clips.append(_chosen_clip)
            # Remove the serie from the series list
            _set_number.remove(_chosen_serie)
        else:
            # If the series list is empty
            if len(_set_number) == 0:
                # Fill it again with the clips left
                _set_number = list(set(('').join(i.split('_')[:-1]) for i in _copy_clip))
            elif len(_set_number) == 1 and _chosen_serie == _set_number[-1]:
                 # Add the clip in the list
                _my_clips.append(_chosen_clip)
                # Remove the serie from the series list
                _set_number.remove(_chosen_serie)
            else:
                # If the serie not in the series list add the clip at the end of the clips list
                _copy_clip.append(_chosen_clip)
        # print(len(_my_clips), len(_clips_list))
    return _my_clips