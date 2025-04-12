#!/usr/bin/python

import time
import logging
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from waveshare_epd import epd7in3f
from config import Display, Paths
from modules import add_timestamp

def update_weather():
    try:
        response = requests.get(Paths.WEATHER_URL, timeout=30)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert('RGB')
        image = image.resize(Display.IMAGE_SIZE)
        logging.info("Weather data retrieved.")
        print("Weather data retrieved.")
        add_timestamp.add_timestamp(image, (255, 255, 255))
        return image

    except Exception as e:
        logging.error(f"Error updating weather: {e}")
        print(f"Error: {e}")
        return None
