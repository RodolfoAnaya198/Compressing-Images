from this import d
from tkinter import image_names
import PIL
from PIL import Image
from tkinter.filedialog import *
import os

# Getting a touple of file images
files = askopenfilenames()

try:
  # Getting the path of working directory
  path = os.getcwd()

  # Create a directory for compressed images
  img_compress_directory = path+"\img-compressed"
  if not os.path.exists(img_compress_directory):
    os.makedirs(img_compress_directory)

  # Moving tho directory for compressed images
  os.chdir(img_compress_directory)

  # Iterating the files
  for i in range(len(files)):
    image = Image.open(files[i])

    # Show the filename of a image in touple
    print("Compressing image:", image.filename)

    # Compressing every image in the touple
    image.save(f"ImagenComprimida_{i}.jpg", "JPEG", optimize=True, quality=30)

  print("All images are compressed rigth")
  os.system("start .")
except:
  print("Some part in the compression procces brack")