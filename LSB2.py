from PIL import Image
from flask import Flask
import binascii, optparse, os, argparse, os.path, sys

def hideLSB2(filename, message):
    binary_message = ""
    for char in message:
        binary_message += char_to_binary(char)
    #Add Flag to the end of the message
    binary_message += "11111111"
    img_name = os.path.basename(filename).split('.')[0]
    message_index = 0
    try:
        with Image.open(filename) as img:
            pixels = img.load()
            MAX_BINARY_LENGTH = img.size[0] * img.size[1]
            MAX_BINARY_LENGTH -= MAX_BINARY_LENGTH % 8
            if len(binary_message) > MAX_BINARY_LENGTH:
                print("WARNING: message too large, truncating...")
                print("TIP: Use larger resolution image to encode the entire message.")
            #Store the relevant part of the message
            binary_message = binary_message[:MAX_BINARY_LENGTH]
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    #Encode the message in the wanted pixel 
                    rgb_list = list(pixels[i, j])
                    blue = rgb_list[-1]
                    if blue % 2:
                        if binary_message[message_index] == '0':
                            blue -= 1
                            rgb_list[-1] = blue
                            pixels[i, j] = tuple(rgb_list)
                    else:
                        if binary_message[message_index] == '1':
                            blue += 1
                            rgb_list[-1] = blue
                            pixels[i, j] = tuple(rgb_list)

                    message_index += 1
                    if message_index == len(binary_message): break
                if message_index == len(binary_message): break
            #Save the encoded message
            img.save(f"encoded-{img_name}.png")
            img.save("HiddenFiles/Hide-" + filename, "PNG")
            print("Done!")
    except OSError:
            msg = "File '{}' is not a valid image"
            raise TypeError(msg.format(filename))
    return "Completed!"

def char_to_binary(char):
    #Convert Char to Binary
    if ord(char) >= 128:
        raise ValueError("Unknown Input Characters.")
    return "{:0>8s}".format(bin(ord(char))[2:])

