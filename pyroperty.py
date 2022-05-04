#!/usr/bin/python3

import sys
from exif import Image
from rich import print

file = sys.argv[1]

image = Image(file)

image_exif = dir(image)

print()
print("[bold magenta]pyroperty[/bold magenta]", ":camera:")
print()
print(f"The EXIF data for '{file}' is as follows:")

for j in range (0, (len(file) + 35)):
    print("[magenta]-[/magenta]", end="")

print()

for i in range (0, len(image_exif)):
    if image.get(image_exif[i]):
        if image_exif[i] == "flash":
            continue    
        print(f"{image_exif[i]:35}: {image.get(image_exif[i], 'Unknown')}")

# ~iosj 2022