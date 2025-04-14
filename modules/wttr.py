#!/usr/bin/python

import time
import logging
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from waveshare_epd import epd7in3f
from config import Display, Paths
from utils.image_tools import add_timestamp, invert_blackwhite

def update_weather():
    try:
        response = requests.get(Paths.WEATHER_URL, timeout=30)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert('RGB')
        image = image.resize(Display.IMAGE_SIZE)
        image = invert_blackwhite(image)
        logging.info("Weather data retrieved.")
        print("Weather data retrieved.")
        add_timestamp(image, (0, 0, 0))
        return image

    except Exception as e:
        logging.error(f"Error updating weather: {e}")
        print(f"Error: {e}")
        return None
