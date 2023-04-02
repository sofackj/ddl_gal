from functions import data_setup, create_directory, get_the_url, text_file_request,generate_img_urls, ddl_process
import personnal_data
import os

# path_data value if no personnal_data module
path_data = None

# Path where to download pics
path = f"{personnal_data.path_data}"

def ddl_app(url, type, chosen_directory): 
    print()
    # Take the url and check the page status
    soup = text_file_request(url)
    # Check the value of soup is legit
    if soup:
        # gallery_type
        final_path = f"{chosen_directory}/{type}/"
        print((final_path))
        # Collect data
        family_pic_name, pic_path = data_setup(url, final_path)
        # Create directory
        if create_directory(pic_path, family_pic_name):
            # Find all furls for all targeted pics
            list_urls = generate_img_urls(soup)
            print()
            # Full process
            ddl_process(list_urls,pic_path,family_pic_name)
            print()
            # Check the numbers of downloaded pics
            print(f"Pics downloaded : {len(os.listdir(pic_path))}")
        else:
            print("Process terminated !")
    else:
        print(f"The URL doesn't fulfill the requirement for the process !\nURL : {url}")
    print()

my_list = []

for i in os.listdir(path):
    if "txt" in i:
        file = open(f"{path}/{i}", "r")
        for line in file:
            my_list.append(line.rstrip())
        file.close()

for url in my_list:
    ddl_app(url, "3d", path)

if __name__ == "__main__":
    pass
    # ddl_app(path)