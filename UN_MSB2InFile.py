import optparse
from PIL import Image, ImageFont, ImageDraw
from flask import Flask
from pip._vendor.distlib.compat import raw_input
import binascii
import optparse
import os
import textwrap
#Decode MSB2
def retrMSB2(filename):
    encoded_image = Image.open(filename)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    #Check the red channel
    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0,0,0)
    decoded_image.save("DiscoverdFilesHistory/decoded-"+filename,"PNG")