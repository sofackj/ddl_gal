import personnal_data
from functions import generate_img_urls, check_url_request
from function_second import pages_list
from largefunctions import ddl_app

path_base = f"{personnal_data.path_downloads}/test"
path_lecture = f"{personnal_data.path_data}/lecture"
path = f"{personnal_data.path_data}"

def download_multi_galery(page_url_before_number,
                          page_url_after_number,
                          galeries_folder_directory,
                          root_directory):
    # List of galeries pages urls
    galeries_pages = pages_list(page_url_before_number, page_url_after_number)
    # For each url pages
    for page in galeries_pages:
        # Generate a list of all galery urls in the page
        galeries_list = generate_img_urls(check_url_request(page), 'h2')
        # For each galery url
        for galery in galeries_list:
            # Download the galery pics
            ddl_app(galery, galeries_folder_directory, root_directory)

if __name__ == "__main__":
    # Start the process
    download_multi_galery(personnal_data.url_dbz, '/', "dbz", personnal_data.stories_path)
