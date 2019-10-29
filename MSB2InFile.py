import optparse
from PIL import Image, ImageFont, ImageDraw
from flask import Flask
from pip._vendor.distlib.compat import raw_input
import binascii
import optparse
import os
import textwrap

def write_text(text_to_write, image_size):
    """Writes text to an RGB image. Automatically line wraps
    text_to_write: the text to write to the image
    """
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)
    #Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def hideMSB2(filename, message):
	img = Image.open(filename)
	red_template = img.split()[0]
	green_template = img.split()[1]
	blue_template = img.split()[2]
	x_size = img.size[0]
	y_size = img.size[1]
    #text draw
	image_text = write_text(message, img.size)
	bw_encode = image_text.convert('1')
    #encode text into image
	encoded_image = Image.new("RGB", (x_size, y_size))
	pixels = encoded_image.load()
	for i in range(x_size):
		for j in range(y_size):
			red_template_pix = bin(red_template.getpixel((i,j)))
			tencode_pix = bin(bw_encode.getpixel((i,j)))
			if tencode_pix[-1] == '1':
				red_template_pix = red_template_pix[:-1] + '1'
			else:
				red_template_pix = red_template_pix[:-1] + '0'
			pixels[i, j] = (int(red_template_pix, 2), green_template.getpixel((i,j)), blue_template.getpixel((i,j)))
	encoded_image.save("HiddenFiles/Hide-" + filename, "PNG")
	return "Completed!"