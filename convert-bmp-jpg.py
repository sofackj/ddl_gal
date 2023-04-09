import os
import aspose.words as aw
import personnal_data

path_base = f"{personnal_data.path_downloads}/test"
path_lecture = f"{personnal_data.path_data}/lecture"
path = f"{personnal_data.path_data}"

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

n = 1
for i in os.listdir(path_base):
    shape = builder.insert_image(f"{path_base}/{i}")
    shape.image_data.save(f"{path}/{n}.jpg")
    n += 1 
