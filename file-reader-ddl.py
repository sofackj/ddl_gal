import os
import personnal_data
from largefunctions import ddl_app

# path_data value if no personnal_data module
path_data = None
# Path where to download pics
path = f"{personnal_data.path_data}"
#
def check_txt_file(chosen_path):
    # Set to 0 for entering the loop
    n = 1
    # Set up the loop process
    while n != 0:
        n = 0
        for type in os.listdir(chosen_path):
            if "txt" in type:
                file = open(f"{chosen_path}/{type}", "r")
                for line in file:
                    n += ddl_app(line.rstrip(), type, chosen_path)
                file.close()

if __name__ == "__main__":
    # Start the process
    check_txt_file(path)