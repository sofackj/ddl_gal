from functions import data_setup, create_directory, get_the_url, check_category,generate_img_urls, ddl_process
import personnal_data
import os

# path_data value if no personnal_data module
path_data = None


# Path where to download pics
path = f"{personnal_data.path_data}"

def ddl_app(chosen_directory): 
    print()
    # Take the url and check the page status
    url, soup = get_the_url()
    # Data finisher
    type = check_category(soup, "2D", "3D")
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
    print()

if __name__ == "__main__":
    ddl_app(path)