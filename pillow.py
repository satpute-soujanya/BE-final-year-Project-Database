import os
import urllib.request
from PIL import Image,ImageColor,ImageFilter,ImageOps
# 1 Done
def resize_with_aspect_ratio(image, size,save_path):
    imgoriginal = Image.open(image)
    resizedImage= imgoriginal.convert('RGB').copy()
    resizedImage.thumbnail(size)
    resizedImage.save(save_path)
    return resizedImage
# 2
def convert_to_pencil_sketch(image_path, save_path):
    image = Image.open(image_path).convert("L")
    image = image.filter(ImageFilter.CONTOUR)
    image = ImageOps.invert(image)
    image.save(save_path)
# 3
def convert_to_black_white(image_path ,save_path):
    image = Image.open(image_path).convert("1")
    image = image.filter(ImageFilter.CONTOUR)
    image = ImageOps.invert(image)
    image.save(save_path) 
# 4
def convert_to_pencil_sketchLA(image_path, save_path):
    image = Image.open(image_path).convert("RGBA").convert("LA")
    image = image.filter(ImageFilter.CONTOUR)
    image.save(save_path)
root_dir = "data"
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'original.jpg':
            print('inside original')
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "resized.jpg")
            resize_with_aspect_ratio(image_path,(128,128) ,save_path)

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'resized.jpg':
            print('inside resized')
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "pencil_sketch_" + file)
            convert_to_pencil_sketch(image_path, save_path)


for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'resized.jpg':
            print('inside resized')
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "sketchLA" + file)
            convert_to_pencil_sketchLA(image_path, save_path)

