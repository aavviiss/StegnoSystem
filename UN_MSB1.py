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

def retrMSB1(filename):
	image = Image.open(filename,'r')
	data = ''
	imgdata = iter(image.getdata())
	pixels = []
	while True:
		try:
			pixels.append(imgdata.__next__())
		except StopIteration:
			break
	binstr = ''
	for i in pixels:
		if (i & 128 == 0):
			binstr += '0'
		else:
			binstr += '1'
	data2 = []
	i=9
	for i in range(1000):
		data2.append(binstr[i * 8:(8 + i * 8)])
		temp = chr(int(data2[i], 2))
		if (temp == '@'):
			data2.append(binstr[(i+1) * 8:(8 + (i+1) * 8)])
			temp = chr(int(data2[i+1], 2))
			if (temp == '@'):
				return(data)
		data += chr(int(data2[i], 2))
	return(data)