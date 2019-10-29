# We will use wave package available in native Python installation to read and write .wav audio file
import wave
from PIL import Image
from flask import Flask
import binascii
import optparse
import os

def AudiortrLSB1(filename):
    # Use wave package (native to Python) for reading the received audio file
    import wave
    song = wave.open(filename, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]

    # Print the extracted text
    print ("Success")
    song.close()
    return(decoded)


    
