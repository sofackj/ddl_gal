import os
import requests
from bs4 import BeautifulSoup
from functions import download_img, normalized_number

# Type 2d or 3d
type = "2d"

# Path where to download pics
path = f""

# replace the URL with the web page you want to scrape
url = \
''
new_directory = url.split("/")[-2]
family_pic_name = "_".join(new_directory.split("-"))

# Create directory
# new_directory = f"{directory}/test"
try:
    os.mkdir(path + new_directory)
    print(f"{family_pic_name} directory created successfully!")
except OSError as error:
    print(f"Error creating directory: {error}")
    print("Process with the existing directory")

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# find all figure tags on the page
figures = soup.find_all('figure')

# print the conten
# ts of each figure tag
n = 1
for fig in figures:
    #
    test = [i.split('"')[1] \
            #
            for i in \
            #
            str(list(fig.find_all('a'))[0]).split(" ") \
            #
            if "href" in i][0]
    print(test)
    filename = f"{path + new_directory}/{family_pic_name}_{normalized_number(n,3)}.jpg"
    download_img(test, filename)
    n += 1

