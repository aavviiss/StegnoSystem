from PIL import Image
from flask import Flask
import binascii, optparse, os, argparse, os.path, sys

def retrLSB2(filename):
    out = ""
    byte = ""
    try:
        with Image.open(filename) as img:
            pixels = img.load()
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    rgb_list = list(pixels[i, j])
                    blue = rgb_list[-1]
                    if blue % 2:
                        byte += "1"
                    else:
                        byte += "0"
                    if len(byte) == 8:
                        if byte == "11111111":
                            break
                        out += byte
                        byte = ""
                if byte == "11111111":
                    break
            output_text = ""
            for i in range(0, len(out), 8):
                byte = out[i:i+8]
                output_text += binary_to_char(byte)           
            print("created")
            return(output_text)

    except OSError:
            msg = "File '{}' is not a valid image"
            raise TypeError(msg.format(filename))

def binary_to_char(binary):
    asc = int(binary, base=2)
    if asc >= 128:
        print(binary)
        raise ValueError("Unknown Input Characters.")
    return chr(asc)
