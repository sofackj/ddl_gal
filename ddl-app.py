from functions import data_setup, create_directory, get_the_url, generate_img_urls, ddl_process
import personnal_data
import os

# Type 2d or 3d
type = "2d"

# path_data value if no personnal_data module
path_data = None

# Path where to download pics
path = f"{personnal_data.path_data}/{type}/"

def ddl_app(chosen_directory): 
    print()
    # Take the url and check the page status
    url, soup = get_the_url()
    # Collect data
    family_pic_name, pic_path = data_setup(url, chosen_directory)
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
    print()

if __name__ == "__main__":
    ddl_app(path)