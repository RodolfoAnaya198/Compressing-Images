import os
import sys
import PIL
from PIL import Image
from tkinter.filedialog import *

def printConsoleHeader():
  # Menu console
  os.system("cls")
  print("ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©")
  print("ğ§           IMAGE COMPRESSOR         ğ§")
  print("ğ§                                    ğ§")
  print("ğ§                 By: Rodolfo Anaya  ğ§")
  print("ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©ğ©")
  print("\nğ°ğ°ğ°\n")

def createImgCmpDirectory() -> str:
  # Getting the path of working directory
  path = os.getcwd()
  img_compress_directory = path+"\img-compressed"

  # Create a directory for compressed images
  if not os.path.exists(img_compress_directory):
    os.makedirs(img_compress_directory)

  return img_compress_directory


def compressImages(files, quality_compression):
  try:
    if (len(files) > 1): 
      print("\nğ Compressing images:\n") 
    else: 
      print("\nğ Compressing image:\n")
    
    # Iterating the files
    for i in range(len(files)):
      image = Image.open(files[i])

      # Show the filename
      print(f"\tâ¡  { image.filename} â")

      # Compressing every image in the touple
      image.save(f"ImagenCmprimida_{i}.jpg", "JPEG", optimize=True, quality=quality_compression)
    
    print("\nğ¢ All images were compressed appropriately ğ¢\n")
  except:
    print("\nğ´ Some part of the compression process failed ğ´")


printConsoleHeader()

# Getting a touple of file images
image_files = askopenfilenames()

# Creating directory for compressed images
img_compress_directory = createImgCmpDirectory()

# Moving tho directory for compressed images
os.chdir(img_compress_directory)

# Compressing images
compressImages(image_files, 30)

# Open the img-compressed directory in file explorer
os.system(f"start {img_compress_directory}")



