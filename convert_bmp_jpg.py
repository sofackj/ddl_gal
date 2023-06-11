import os
import aspose.words as aw
import personnal_data

path_base = ""
path_lecture = ""
path = ""

# Prepare the builder
doc = aw.Document()
builder = aw.DocumentBuilder(doc)

# Process for the conversion
n = 1
for i in os.listdir(path_base):
    shape = builder.insert_image(f"{path_base}/{i}")
    shape.image_data.save(f"{path}/newpic_{n}.jpg")
    n += 1 

if __name__ == "__main__":
    # Start the process
    print("Application to validate")
    