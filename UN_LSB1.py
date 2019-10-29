from PIL import Image
from flask import Flask
import binascii, optparse, os

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def bin2str(binary):
    message = binascii.unhexlify('%x' % (int(binary, 2)))
    return message

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

#Retrieve
def retrLSB1(filename):
	img = Image.open(filename)
	binary = ''
	if img.mode in ('RGBA'): 
		img = img.convert('RGBA')
		datas = img.getdata()
		for item in datas:
			digit = decode(rgb2hex(item[0],item[1],item[2]))
			if digit == None:
				pass
			else:
				binary = binary + digit
				if (binary[-16:] == '1111111111111110'):
					print ("Success")
					mystring = bin2str(binary[:-16])
					print(mystring)
					return mystring

		return bin2str(binary)
	return "Incorrect Image Mode, Couldn't Retrieve"
