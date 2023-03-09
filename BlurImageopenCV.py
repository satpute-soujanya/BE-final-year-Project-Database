import cv2 
import os

def blurImage(imagepath, ksize, savepath):
    image = cv2.imread(imagepath)
    image = cv2.blur(image, ksize) 
    cv2.imwrite(savepath, image)    
root_dir = "data"

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'black_whiteresized.jpg':
            print('inside blureed',subdir)
            image_path = os.path.join(subdir, file)
            save_path = os.path.join(subdir, "blur" + file)
            try:
                blurImage(image_path, (10,10),save_path)
            except:
                print('error')
