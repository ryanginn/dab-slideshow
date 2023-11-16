# dab-slideshow
Make smarter DAB slideshows!

Examples of use include:

![Example of use in the Netherlands](https://i.ibb.co/26x83Ps/output.jpg) ![Example of use in Netherlands](https://i.ibb.co/72QG4xc/output.jpg) ![Example of use on trial DAB multiplex](https://i.ibb.co/NWM5jLW/output.jpg) ![use on pirate DAB multiplex in Northern Ireland](https://i.ibb.co/c2YdrnR/output.jpg)

## What does it do?
dab-slideshow is a project designed to recreate DAB slideshows such as Bayern 1's slideshow, which includes now playing information.

## How does it work? 
dab-slideshow uses the Azuracast API or the Icecast 2 API to fetch now playing data and includes it on an image compatible with DAB+ MOT slideshows.

## Potential use case?
dab-slideshow could be used in a DAB+ mux, alongside other slideshow images, such as station contact details, I have tried it in OpenDigitalRadio and it works well.

### Prerequisites
Any OS that supports Python (Windows, Mac, Linux, etc) <br>
Python 3.11 or newer
```
pip install pillow
```
```
pip install requests
```
```
pip install datetime
```
### Install
Download latest release from [here](https://github.com/ryanginn/dab-slideshow/releases/tag/main)<br>
Extract .zip file into any folder, doesn't matter<br>
Download a font you wish to use (does not come pre-installed)<br>
Edit run.py to suit your needs.<br>

If any issues arise, please leave an issue and I will look into it. Thanks!
