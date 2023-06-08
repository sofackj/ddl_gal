import os
from random import random
from functions import normalized_number, data_setup, create_directory, check_url_request,generate_img_urls, ddl_process

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
