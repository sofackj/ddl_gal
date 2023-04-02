import os
import personnal_data
from largefunctions import ddl_app

# path_data value if no personnal_data module
path_data = None

# Path where to download pics
path = f"{personnal_data.path_data}"

# Set to 0 for entering the loop
n = 1
# Set up the loop process
while n != 0:
    n = 0
    for type in os.listdir(path):
        if "txt" in type:
            file = open(f"{path}/{type}", "r")
            for line in file:
                n += ddl_app(line.rstrip(), type, path)
            file.close()

if __name__ == "__main__":
    pass
    # ddl_app(path)