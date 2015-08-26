from PIL import Image
import os

# 512 here

try:
    sizes = []
    sizesFilename = input("Enter text file containing sizes: ")
    with open(sizesFilename, "r") as sizesContent:
        for line in sizesContent:
            # TODO: split the train wreck
            sizes = sizesContent.read().splitlines()

    iconFilename = input('Enter icon name: ')
    ouputFolderName = input("Enter folder name that will contain new icons: ")


    rawIcon = Image.open(iconFilename)
    for size in sizes:
        size = int(size)

        if size > 512: #find out the input image's dimensions. And use that in place of '512'
            print("Warning: " + size + " will decrease in quality!")

        resizedIcon = rawIcon.resize((size, size), Image.ANTIALIAS)
        resizedIcon.save(os.path.join(ouputFolderName, size + ".png"))

except Exception as e:
    print(e)