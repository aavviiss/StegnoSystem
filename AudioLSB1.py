import wave, binascii, optparse, os
from PIL import Image
from flask import Flask

def AudioHideLSB1(filename, message):
    #read wave audio file
    song = wave.open(filename, mode='rb')
    #convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    string= message
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)
    # Write bytes to a new wave audio file
    with wave.open("HiddenFiles/Hide-" + filename, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()
    return "Completed!"
