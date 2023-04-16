import os
import shutil
from check_functions import test_requests
from random import choice

# Purge all the files of a directory
def purge_directory_content(directory_path):
    for image in os.listdir(directory_path):
        try:
            os.remove(f"{directory_path}/{image}")
        except:
            print(f"The file or folder '{image}' can't be deleted...")

# Take random items of list
def random_items_from_list(nb, target_list):
    new_list = []
    for i in range(nb):
        # Choose a random item
        random_item = choice(target_list)
        # Add the random item to the list
        new_list.append(random_item)
        # Remove the item from the first list
        target_list.remove(random_item)
    # Return the first list modified with the new list
    return target_list, new_list

#
def copy_files_from_directories_list(directories_list, root_directory_path,images_destination_path):
    for inc, folder in enumerate(directories_list):
        folder_path = f"{root_directory_path}/{folder}"
        for inc_2, file in enumerate(os.listdir(folder_path)):
            img_path = f"{folder_path}/{file}"
            new_img_name = f"{inc}_{folder}_{inc_2}"
            shutil.copyfile(img_path, f"{images_destination_path}/{new_img_name}.jpg")

#
def pages_list(url, back_url=''):
    list_url_pages = []
    #
    n = 1
    #
    while True:
        url_page = f"{url}{n}{back_url}"
        if test_requests(url_page):
            list_url_pages.append(url_page)
            # print(url_page)
            n += 1
        else:
            break
    return list_url_pages
