import time
from progress.bar import IncrementalBar
import pyperclip
import os
import personnal_data
from functions import create_directory, request_process, check_category
from function_second import random_items_from_list
import re
from random import choice
import shutil

path_base = f"{personnal_data.path_data}"
path_lecture = f"{personnal_data.path_data}/lecture"
path = f"{personnal_data.path_data_spe}"

my_list = []

for i in os.listdir(path):
    my_list.append(i)

old_list, lecture_list = random_items_from_list(0, my_list)

create_directory(path_lecture, "lecture")

for file in os.listdir(path_lecture):
    os.remove(f"{path_lecture}/{file}")

for inc, folder in enumerate(lecture_list):
    folder_path = f"{path}/{folder}"
    for inc_2, file in enumerate(os.listdir(folder_path)):
        img_path = f"{folder_path}/{file}"
        new_img_name = f"{inc}_{folder}_{inc_2}"
        shutil.copyfile(img_path, f"{path_lecture}/{new_img_name}.jpg")

print(lecture_list)

# url, soup =  request_process()

# category = check_category(soup)

# print(category)

# if metas:
#     print("3D")
# else:
#     print("2D")

# path = f"{personnal_data.path_data}/hello"

# if create_directory(path, "hello"):
#     print("gj")
# else:
#     print('stop')

# s = pyperclip.paste()
# print(s)

# mylist = [1,2,3,4,5,6,7,8]
# a = time.time()
# bar = IncrementalBar('Countdown', max = len(mylist))
# for item in mylist:
#     bar.next()
#     time.sleep(1)
# bar.finish()
# b = time.time()

# print(b-a)
# path = "/Users/sofak/Documents"

# for i in os.listdir(path):
#     print(i)
#     print("Hello World")
    
