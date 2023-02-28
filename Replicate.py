import replicate
import os
import urllib.request
from PIL import Image,ImageColor,ImageFilter,ImageOps,ImageSequence



os.environ["REPLICATE_API_TOKEN"] = "1b644179e3e437dd59053c7a9fdhjskjac92c93139837fs"
model = replicate.models.get("yuval-alaluf/sam")
version = model.versions.get("9222a21c181b707209ef12b5e0d7e94c994b58f01c7b2fec075d2e892362f13c")
def convertGif_png(gifPath,savepath):
    with Image.open(gifPath) as im:
     for i in range(im.n_frames):
        im.seek(i)
        im.save(os.path.join(savepath, 'Age{}.png'.format(i)))
   

def AgeConversion(imagepath, savepathgif, gifpath, savepathImg):
    input = {
        'image': open(imagepath, 'rb'),
        'target_age': 'default' 
    }
    output = version.predict(**input)
    print(output)
    outputImg = urllib.request.urlretrieve(output, savepathgif)
    convertGif_png(gifpath,savepathImg)

root_dir = "data"
# AgeConversion('data/AaronFinch/original.jpg','data/AaronFinch')
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'original.jpg':
            print('inside resized')
            imagepath = os.path.join(subdir, file)
            savepathgif = os.path.join(subdir, "outputAge.gif")
            gifpath = os.path.join(subdir, "outputAge.gif")
            savepathImg = os.path.join(subdir)
            AgeConversion(imagepath, savepathgif,gifpath,savepathImg)