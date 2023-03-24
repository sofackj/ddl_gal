import os
import requests
import time
from progress.bar import IncrementalBar
from bs4 import BeautifulSoup
import pyperclip

#
def take_clipboard():
    url = pyperclip.paste()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return url, soup
        else:
            return False
    except:
        return False

#
def request_process():
    while True:
        url = input("URL target : ")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Clean URL added !")
                soup = BeautifulSoup(response.text, 'html.parser')
                return url, soup
            else:
                continue
        except:
            continue

# Get the URL
def get_the_url():
    if take_clipboard():
        print("Clean URL in the clipboard !")
        return take_clipboard()
    else:
        return request_process()

# Prepare data
def data_setup(url, path):
    new_directory = url.split("/")[-2]
    family_pic_name = "_".join(new_directory.split("-"))
    pic_path = path + new_directory
    return new_directory, family_pic_name, pic_path

# Create a directory
def create_directory(directory_path, folder_name):
    try:
        os.mkdir(directory_path)
        print(f"{folder_name} directory created successfully!")
    except OSError as error:
        print(f"Error creating directory: {error}")
        print("Process with the existing directory")  

#
def generate_img_urls(soup_object):
    # 
    url_list = []
    #
    figures = soup_object.find_all('figure')
    # 
    for element in figures:
        #
        target_url = [
            i.split('"')[1] for i in str(list(element.find_all('a'))[0]).split(" ") if "href" in i
        ][0]
        #
        url_list.append(target_url)
    return url_list

# Download pic one at a time
def download_img(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
            # print("Image saved as", filename.split("/")[-1])
    else:
        # print("Failed to download image")
        pass

# Number of zeros
def normalized_number(number, length):
    new_str = str(number)
    while len(new_str) < length:
        new_str = "0" + new_str
    return new_str

#
def ddl_process(list_urls, path, pic_serie):
    n = 1
    bar = IncrementalBar('Countdown', max = len(list_urls))
    for url in list_urls:
        start = time.time()
        # Create the file name of the picture
        filename = f"{path}/{pic_serie}_{normalized_number(n,3)}.jpg"
        download_img(url, filename)
        stop = time.time()
        bar.next()
        time.sleep(stop-start)
        n += 1
