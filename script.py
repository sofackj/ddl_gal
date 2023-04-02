import time
from progress.bar import IncrementalBar
import pyperclip
import os
import personnal_data
from functions import create_directory, request_process, check_category
import re

path = f"{personnal_data.path_data}"

my_list = []

for i in os.listdir(path):
    if "txt" in i:
        file = open(f"{path}/{i}", "r")
        for line in file:
            my_list.append(line.rstrip())
        file.close()

print(my_list)

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
    
