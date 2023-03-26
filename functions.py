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
                soup = BeautifulSoup(response.text, 'html.parser')
                return url, soup
            else:
                continue
        except:
            continue

def yes_or_no_input():
    ask_question = input("Use the default category ? ")
    if ask_question == "" or ask_question[0].lower() != "n":
        return False
    else:
        return True

# Check category
def check_category(soup, default_value, chosen_value):
    tags = soup.find_all("span",{"class":"post-category"})
    for element in tags:
        for content in element.contents:
            if "3D" in str(content):
                return chosen_value
            else:
                continue
    if yes_or_no_input():
        return chosen_value
    else:
        return default_value

# Get the URL
def get_the_url():
    if take_clipboard():
        return take_clipboard()
    else:
        return request_process()

# Prepare data
def data_setup(url, path):
    new_directory = url.split("/")[-2]
    family_pic_name = "_".join(new_directory.split("-"))
    pic_path = path + new_directory
    return family_pic_name, pic_path

# Create a directory
def create_directory(directory_path, folder_name):
    try:
        os.mkdir(directory_path)
        print(f"{folder_name} directory created successfully!")
        return True
    except OSError:
        print("The directory already exists !")
        return False

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
