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
        # This is chrome, you can set whatever browser you like
        # Avoid 403 Forbidden
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        response = requests.get(url, headers=headers)
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
            # This is chrome, you can set whatever browser you like
            # Avoid 403 Forbidden
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return url, soup
            else:
                continue
        except:
            continue

# Check if the url is correct, if yes return the soup into a variable if asked
def check_url_request(url):
    try:
        # This is chrome, you can set whatever browser you like
        # Avoid 403 Forbidden
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(f"Error during the GET response : {response.status_code} ")
            return False
    except:
        print(f"Couldn't perform the request correctly for the fllowing url: \n{url}")
        return False

# Get the URL
def get_the_url():
    if take_clipboard():
        return take_clipboard()
    else:
        return request_process()

#
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
            if chosen_value in str(content):
                return chosen_value
            else:
                continue
    if yes_or_no_input():
        return chosen_value
    else:
        return default_value

# Prepare data
def data_setup(url, path):
    new_directory = url.split("/")[-2]
    family_pic_name = "_".join(new_directory.split("-"))
    pic_path = path + "/" + new_directory
    return family_pic_name, pic_path

# Create a directory
def create_directory(directory_path, folder_name):
    try:
        os.mkdir(directory_path)
        print(f"{folder_name} directory created successfully!")
        return True
    except OSError:
        print(f"The directory {folder_name} already exists !")
        return False

# 
def generate_img_urls(soup_object, tag, tag_class=None):
    if soup_object:
        # 
        url_list = []
        #
        pack = soup_object.find_all(tag, tag_class)
        # 
        for element in pack:
            #
            target_url = [
                i.split('"')[1] for i in str(list(element.find_all('a'))[0]).split(" ") if "href" in i
            ][0]
            #
            url_list.append(target_url)
        return url_list
    else:
        print("Error -> URL not conform or resuest status different from 200.\nCheck error described above.")

# Download pic one at a time
def download_img(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
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

def lines_list_in_txt(chosen_path, file_id=""):
    # List of lines
    lines_list = []
    # Set up the loop process
    for file in os.listdir(chosen_path):
        if ".txt" in file and file_id in file:
            txt_file = open(f"{chosen_path}/{file}", "r")
            for line in txt_file:
                lines_list.append(line.strip())
            txt_file.close()
    return lines_list
