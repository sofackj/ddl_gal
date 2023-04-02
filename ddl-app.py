import personnal_data
from functions import get_the_url, check_category
from largefunctions import ddl_app

# path_data value if no personnal_data module
path_data = None

# Path where to download pics
path = f"{personnal_data.path_data}"

# Take the url and check the page status
url, soup = get_the_url()
# Data finisher
type = check_category(soup, "2D", "3D")


if __name__ == "__main__":
    # Start the process
    ddl_app(url, type, path)