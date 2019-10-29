from PIL import Image
from flask import Flask
import binascii, optparse, os

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
    """Return (red, green, blue) for the color given as #rrggbb."""
    hexcode = hexcode.lstrip('#')
    lv = len(hexcode)
    return tuple(int(hexcode[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def str2bin(message):
	binary = bin(int.from_bytes(message.encode(), 'big'))
	return(binary)

def encode(hexcode, digit):
    # if the last digit is 0/1/2/3/4/5 it will save data
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        hexcode = hexcode[:-1] + digit
        return hexcode
    else:
        return None

###### Hide ######
def hideLSB1(filename, message):
    img = Image.open(filename)
    # Adds Hex value to the end of the string
    binary = str2bin(message) + '1111111111111110'
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()
        newData = []
        digit = 0
        for item in datas:
            # Adding the new pixel
            if (digit < len(binary)):
                newpix = encode(rgb2hex(item[0], item[1], item[2]), binary[digit])
                if newpix == None:
                    newData.append(item)
                else:
                    r, g, b = hex2rgb(newpix)
                    newData.append((r, g, b, 255))
                    digit += 1
            else:
                newData.append(item)
        img.putdata(newData)
    img.save("HiddenFiles/Hide-" + filename, "PNG")
    return "Completed!"

