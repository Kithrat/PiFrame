#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import time
import sys
import logging
from waveshare_epd import epd7in3f
from modules import wttr, cal
from config import Display, Paths

# Logging setup
logging.basicConfig(filename=Paths.LOG_FILE, level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s')

# Display
epd = epd7in3f.EPD()
epd.init()
logging.info("Initializing screen")
print("Initializing screen.")

def display_image(image):
    if image is None:
        logging.warning("Attempted to display a None image.")
        print("Attempted to display a None image")
        return
    epd.Clear()
    epd.display(epd.getbuffer(image))
    logging.info("Screen updated.")
    print("Screen updated")

try:
    while True:
        display_image(wttr.update_weather())
        time.sleep(1800)
        display_image(cal.update_calendar())
        time.sleep(1800)

except KeyboardInterrupt:
    logging.info("Interrupted by user. Putting display to sleep.")
    print("Interrupted by user. Putting display to sleep.")
    epd.sleep()
    sys.exit()

except Exception as e:
    logging.error(f"Fatal error: {e}")
    print("Fatal error: {e}")
    epd.sleep()
    sys.exit()
