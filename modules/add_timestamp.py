#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import time
import logging
from config import Display, Paths

def add_timestamp(image, color):
    draw = ImageDraw.Draw(image)
    timestamp = time.strftime("Last updated %Y-%m-%d %H:%M:%S")
    font = ImageFont.truetype(Display.FONT_PATH, Display.FONT_SIZE)
    draw.text((10, Display.IMAGE_SIZE[1] - Display.FONT_SIZE - 5), timestamp, font=font, fill = color)
    logging.info("Timestamp added")
    print("Timestamp added")
    return image
