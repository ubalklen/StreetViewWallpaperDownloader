# Street View Wallpaper Downloader
All I wanted was that my wallpapers are random Street View images. Google provides an [API](https://developers.google.com/maps/documentation/streetview/intro) to download Street View photos, but the maximum size is 640x640. This script hacks around that limitation by taking a screenshot of images as they are rendered in a browser.

## Requirements
* Python 3.7
* Python modules in [requirements.txt](requirements.txt)
* Chrome browser
* A compatible Chrome [webdriver](https://chromedriver.chromium.org/downloads) (current [chromedriver.exe](chromedriver.exe) in this repo is compatible with Chrome 83)
* [Google API key](https://developers.google.com/maps/documentation/streetview/get-api-key) set to use [Street View Static API](https://developers.google.com/maps/documentation/streetview/intro) and [Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/tutorial)

## Usage
1. Clone or download this repo.
2. Edit [save_random_view.py](save_random_view.py) to add your key into `API_KEY` variable.
3. Edit [clean_street_view.html](clean_street_view.html) to add your key into <code>https://<!---->maps.googleapis<!---->.com/maps/api/js?key=**ADD_YOUR_KEY-HERE**&callback=initPano</code>
4. Run `python save_random_view.py`
5. Random street view clean image will be in [images](images) folder

## Details
Script uses [polygons](polygons) (formatted as a set of coordinates) to limit the area of images. Current repo has 2 polygons roughly covering all land on Earth. You can use custom polygons to limit the images to more specific regions.

Because there isn't a smart way to get a valid Street View coordinate, the script may take several seconds to finish. Smaller polygons may help.