import os
import requests
from bs4 import BeautifulSoup
from functions import create_directory ,download_img, normalized_number
import personnal_data

# Type 2d or 3d
type = "3d"

# Path where to download pics
path = f"{personnal_data.path_data}/{type}/"

# Collect data
url = personnal_data.url_data
new_directory = url.split("/")[-2]
family_pic_name = "_".join(new_directory.split("-"))

# Create directory
create_directory(path + new_directory, family_pic_name)

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# find all figure tags on the page
figures = soup.find_all('figure')

# ts of each figure tag
n = 1
for fig in figures:
    #
    target_url = [i.split('"')[1] \
            #
            for i in \
            #
            str(list(fig.find_all('a'))[0]).split(" ") \
            #
            if "href" in i][0]
    print(target_url)
    # Create the file name of the picture
    filename = f"{path + new_directory}/{family_pic_name}_{normalized_number(n,3)}.jpg"
    download_img(target_url, filename)
    n += 1

