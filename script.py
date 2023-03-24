import time
from progress.bar import IncrementalBar
import pyperclip
import os
import personnal_data
from functions import create_directory

path = f"{personnal_data.path_data}/hello"

if create_directory(path, "hello"):
    print("gj")
else:
    print('stop')

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
    
