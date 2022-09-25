import PIL.Image
from pathlib import Path
import time
from pygame import mixer  
import os
mixer.init()
mixer.music.load('bad-apple.mp3')

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", " ", "."]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height - 20))

    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):

    directory = 'frames'
    mixer.music.play()
    files = Path(directory).glob('*')
    for file in range(0, 6579):
        fram = "frames/frame" + str(file) + ".jpg"
        image = PIL.Image.open(fram)

        new_image_data = pixels_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)  
        ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

        print(ascii_image)

        time.sleep(0.0239)

    
# run program
main()

