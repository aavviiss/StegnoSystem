import optparse, binascii, optparse, os
from PIL import Image
from flask import Flask
from pip._vendor.distlib.compat import raw_input

def read_bit(data):
	newd = []
	for i in data:
		newd.append(format(ord(i), '08b'))
	return newd

def encode_img(img, data):
	datalist = read_bit(data)
	datalen = len(datalist)
	imdata = iter(img.getdata())
	pix = []
	for i in range(8 * datalen):
		pix.append(imdata.__next__())

	pix2 = []
	for i in range(datalen):
		for j in range(0, 8):
			if (datalist[i][j] == '0'):
				pix2.append(pix[j] & img.maskZero)
			else:
				pix2.append(pix[j] | img.maskOne)
	return pix2

def encode_enc(img, data):
	(x, y) = (0, 0)
	for Pix_val in encode_img(img, data):
		img.putpixel((x, y), Pix_val)
		if (x == img.width - 1):
			x = 0
			y += 1
		else:
			x += 1

def hideMSB1(filename, message):
	img = Image.open(filename).convert('L')
	img.maskOne = 128
	img.maskZero = 127
	message = message+'@@'
	encode_enc(img, message)
	img.save("HiddenFiles/Hide-" + filename, "PNG")
	print("Completed!")
