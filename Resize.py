from PIL import Image
import os

try:
    list = []
    text = input("Enter text file containing sizes: ")
    with open(text, "r") as content:
        for line in content:
            list = content.read().splitlines()

    picture = input('Enter picture name: ')
    folder = input("Enter folder name that will contain new images: ")
    for value in list:
        size = int(value)
        img = Image.open(picture)

        if size > 512:
            print("Warning: " + value + " will decrease in quality!")

        im = img.resize((size, size), Image.ANTIALIAS)
        im.save(os.path.join(folder, value + ".png"))

except Exception as e:
    print(e)