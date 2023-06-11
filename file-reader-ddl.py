import os
import personnal_data
from largefunctions import ddl_app

# path_data value if no personnal_data module
path_data = None
# Path where to download pics
path = f"{personnal_data.path_data_3d}"
#
def check_txt_file(chosen_path):
    # Set to 0 for entering the loop
    n = 1
    # Set up the loop process
    while n != 0:
        n = 0
        for file in os.listdir(chosen_path):
            if ".txt" in file:
                txt_file = open(f"{chosen_path}/{file}", "r")
                for line in txt_file:
                    category = file.split(".")[0]
                    n += ddl_app(line.rstrip(), category, chosen_path)
                txt_file.close()

if __name__ == "__main__":
    # Start the process
    check_txt_file(path)
    