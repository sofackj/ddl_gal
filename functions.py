import requests

def download_img(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
            print("Image saved as", filename)
    else:
        print("Failed to download image")

# Number of zeros
def normalized_number(number, length):
    new_str = str(number)
    while len(new_str) < length:
        new_str = "0" + new_str
    return new_str
