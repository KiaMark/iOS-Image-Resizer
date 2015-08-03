from PIL import Image
import os

try:
    list = []
    with open("Sizes.txt", "r") as content:
        for line in content:
            list = content.read().splitlines()

    for value in list:
        size = int(value)
        img = Image.open('bookmarq.png')

        if size > 512:
            print("Warning: " + value + " will decrease in quality!")

        im = img.resize((size, size), Image.ANTIALIAS)
        im.save(os.path.join("Resized", value + ".png"))

except Exception as e:
    print(e)