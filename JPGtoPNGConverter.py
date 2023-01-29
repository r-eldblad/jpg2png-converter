import sys
import os
from PIL import Image


# grab first and second argument
input_folder = sys.argv[1]
output_folder = sys.argv[2]
target_extension = '.png'

# check if path/ (second argument) exists, and if not create it
if os.path.exists(output_folder):
    print(f"{output_folder} mappen existerar redan. Försök igen.")
elif not os.path.exists(input_folder):
    print(f"{input_folder} är inte giltig. Försök igen.")
else:
    os.mkdir(output_folder)
    if os.path.exists(output_folder):
        print(f'{output_folder} mappen skapades.')

    for image in os.listdir(input_folder):
        if (image.endswith(".jpg")):
            filename, extension = os.path.splitext(image)
            print(filename, extension)
            original_image = Image.open(f'{input_folder}{filename}{extension}')
            original_image.save(f"{output_folder}{filename}{target_extension}")
            print(f"{filename} konverterades")

print("Klart.")