#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import time
import logging
from config import Display, Paths

def invert_blackwhite(image):
    inverted = image.copy()
    pixels = inverted.load()
    for y in range(inverted.height):
        for x in range(inverted.width):
            r, g, b = pixels[x, y]
            if (r, g, b) == (0, 0, 0):  # pure black
                pixels[x, y] = (255, 255, 255)
            elif (r, g, b) == (255, 255, 255):  # pure white
                pixels[x, y] = (0, 0, 0)
            # leave all other colors alone
    return inverted

def invert_near_blackwhite(image, threshold):
    """
    Inverts pixels that are close to black or white.
    
    Args:
        image: PIL Image in RGB mode.
        threshold: Integer between 0-255. 
                   Lower = stricter match to pure black/white, higher = more forgiving.
    
    Returns:
        A new PIL Image with inverted black/white-like pixels.
    """
    inverted = image.copy()
    pixels = inverted.load()

    for y in range(inverted.height):
        for x in range(inverted.width):
            r, g, b = pixels[x, y]

            # Calculate brightness: simple average or use luminance
            brightness = (r + g + b) / 3

            if brightness <= threshold:  # near black
                pixels[x, y] = (255, 255, 255)
            elif brightness >= 255 - threshold:  # near white
                pixels[x, y] = (0, 0, 0)
            # Leave midtones or colors alone

    return inverted


def add_timestamp(image, color):
    draw = ImageDraw.Draw(image)
    timestamp = time.strftime("Last updated %Y-%m-%d %H:%M:%S")
    font = ImageFont.truetype(Display.FONT_PATH, Display.FONT_SIZE)
    draw.text((10, Display.IMAGE_SIZE[1] - Display.FONT_SIZE - 5), timestamp, font=font, fill = color)
    logging.info("Timestamp added")
    print("Timestamp added")
    return image
