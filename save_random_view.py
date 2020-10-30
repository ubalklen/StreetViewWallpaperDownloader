import sys
import glob
import time
import csv
import requests
import matplotlib.path as mplt_path
from selenium import webdriver
from os import path
from random import uniform

# fmt: off
API_URL = "https://maps.googleapis.com/maps/api/streetview/metadata"  # Not billed
API_KEY = "ADD_YOUR_KEY_HERE"  # get a key at https://developers.google.com/maps/documentation/streetview/get-api-key
WIDTH = 1920
HEIGHT = 1080
# fmt: on

if getattr(sys, "frozen", False):
    script_path = path.dirname(sys.executable)
else:
    script_path = path.dirname(path.abspath(__file__))

# Setup on land polygons
paths = []
for poly_file in glob.glob("polygons\*.csv"):
    with open(poly_file, newline="") as f:
        data = list(csv.reader(f))
        paths.append(mplt_path.Path(data, closed=True))

# Get a valid Street View coordinate
status = False

while status != "OK":
    onland = False

    # Pick a random point that is on land
    while not onland:
        lat, lng = uniform(-180, 180), uniform(-90, 90)

        for p in paths:
            if p.contains_point((lat, lng)):
                onland = True
                break

    # Check if random point has a Street View panorama
    locstring = str(lat) + "," + str(lng)
    r = requests.get(API_URL + "?key=" + API_KEY + "&location=" + locstring)
    status = r.json()["status"]

# Webdriver setup
options = webdriver.chrome.options.Options()
options.add_argument("--log-level=3")  # minimal logging
options.add_argument("--window-size=" + str(WIDTH) + "," + str(HEIGHT))
options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", options=options)
page_path = path.join(
    script_path, "clean_street_view.html?lat=" + str(lat) + "&lng=" + str(lng)
)
driver.get(page_path)
time.sleep(1)  # wait for image to load
driver.save_screenshot("images\\" + str(lat) + "_" + str(lng) + ".png")
driver.close()
