from functions import data_setup, create_directory, request_process, generate_img_urls, ddl_process
import personnal_data

# Type 2d or 3d
type = "3d"

# path_data value if no personnal_data module
path_data = None

# Path where to download pics
path = f"{personnal_data.path_data}/{type}/"

# Take the url and check the page status
url, soup = request_process()

# Collect data
new_directory, family_pic_name, pic_path = data_setup(url, path)

# Create directory
create_directory(pic_path, family_pic_name)

# Find all furls for all targeted pics
list_urls = generate_img_urls(soup)

# Full process
ddl_process(list_urls,pic_path,family_pic_name)

