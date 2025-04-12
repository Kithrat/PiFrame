#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import subprocess
import logging
import time
from config import Display, Paths
from modules import add_timestamp

def update_calendar():
    try:
        # Generate calendar from remind
        text_cal = subprocess.check_output(['remind', '-c+7', Paths.REMIND_PATH]).decode()
        logging.info("Generating calendar")
        print("Generating calendar")
        # Create white background
        cal = Image.new('1', Display.IMAGE_SIZE, 255)
        draw = ImageDraw.Draw(cal)
        # Draw the text
        font = ImageFont.truetype(Display.FONT_PATH, Display.FONT_SIZE)
        margin = 10
        offset =10
        for line in text_cal.splitlines():
            draw.text((margin, offset), line, font=font, fill=0)
            offset += 20
        # Save for debugging
        cal.save("calendar_output.bmp")
        add_timestamp.add_timestamp(cal, 0)
        return cal 

    except Exception as e:
        logging.error(f"Error updating calendar: {e}")
        print(f"Error updating calendar: {e}")
        return None
