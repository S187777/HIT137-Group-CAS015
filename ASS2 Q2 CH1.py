import time

current_time = int(time.time())
generated_number = (current_time & 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)

import PIL
from PIL import Image

def change_pixels(img):

    width, height = img.size
    print(img.size)
    sum_red_pixels = 0
    pixel_map = img.load()

    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            pixel_map[x, y] = (r + n, g + n, b + n)
            sum_red_pixels += (r+n) 
    print(sum_red_pixels)
n = generated_number

img = Image.open("chapter1.jpg")
img = img.convert('RGB')

change_pixels(img)

img.save("chapter1out.png")
img.show()