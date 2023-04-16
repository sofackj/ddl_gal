import personnal_data
from functions import generate_img_urls, check_url_request, create_directory
from function_second import pages_list
from largefunctions import ddl_app

url_to_scrap = personnal_data.url_galeries_tfs
path_base = personnal_data.stories_path
directory_name= personnal_data.url_galeries_tfs.split("/")[-1]
directory_path = personnal_data.tfs_path

def download_multi_galery(page_url_before_number,
                          page_url_after_number,
                          galeries_directory_name,
                          root_directory):
    create_directory(root_directory, directory_name)
    # List of galeries pages urls
    galeries_pages = pages_list(page_url_before_number, page_url_after_number)
    # For each url pages
    for page in galeries_pages:
        # Generate a list of all galery urls in the page
        galeries_list = generate_img_urls(check_url_request(page), 'h2')
        # For each galery url
        for galery in galeries_list:
            # Download the galery pics
            ddl_app(galery, galeries_directory_name, root_directory)

if __name__ == "__main__":
    # Start the process
    download_multi_galery(url_to_scrap, '/', directory_name, directory_path)
