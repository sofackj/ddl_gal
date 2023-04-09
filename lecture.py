import os
import personnal_data
from functions import create_directory
from function_second import random_items_from_list
import shutil

path_base = f"{personnal_data.path_data}"
path_lecture = f"{personnal_data.path_data}/lecture"
path = f"{personnal_data.path_data_spe}"

folder_list = [item for item in os.listdir(path)]

old_list, lecture_list = random_items_from_list(20, folder_list)

create_directory(path_lecture, "lecture")

for file in os.listdir(path_lecture):
    os.remove(f"{path_lecture}/{file}")

for inc, folder in enumerate(lecture_list):
    folder_path = f"{path}/{folder}"
    for inc_2, file in enumerate(os.listdir(folder_path)):
        img_path = f"{folder_path}/{file}"
        new_img_name = f"{inc}_{folder}_{inc_2}"
        shutil.copyfile(img_path, f"{path_lecture}/{new_img_name}.jpg")

print(len([image for image in os.listdir(path_lecture)]))
