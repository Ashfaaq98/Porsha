import PIL
import sys
from PIL import Image,  ExifTags


def metafun():
    # This function will take the user input of the image file and will extract the exif information
    
    imag = input("Enter the name of the image:")
    img=PIL.Image.open(imag)
    exifdata=img._getexif()
    print(type(exifdata))

    # If no exif data is found the function will print none and if any exif information is found 
    # the function will print it on the terminal

    if exifdata is None:
        print('Sorry, image has no exif data.')
    else:
        for key, val in exifdata.items():
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')
    
    sys.stdout.write('### Returning back to main page ####')