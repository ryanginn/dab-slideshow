# dab-slideshow
Make smarter DAB slideshows!

Examples of use include:

![Example of use in the Netherlands](https://i.ibb.co/26x83Ps/output.jpg) ![Example of use in Netherlands](https://i.ibb.co/72QG4xc/output.jpg)

## What does it do?
dab-slideshow is a project designed to recreate DAB slideshows such as Bayern 1's slideshow, which includes now playing information.

![Example](https://github.com/ryangontv/dab-slideshow/assets/98589683/223798f2-ddb5-4d7d-a12d-063ceb36ffdf)


## How does it work? 
dab-slideshow uses the Azuracast API or the Icecast 2 API to fetch now playing data and includes it on an image compatible with DAB+ MOT slideshows.

## Potential use case?
dab-slideshow could be used in a DAB+ mux, alongside other slideshow images, such as station contact details, I have tried it in OpenDigitalRadio and it works well.

### Prerequisites
Any OS that supports Python (Windows, Mac, Linux, etc) <br>
Background image that is 320x240px resolution, under 10KB in JPG form <br>
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
Download latest release from [here](https://github.com/ryanginn/dab-slideshow/releases/tag/stable)<br>
Extract .zip file into any folder, doesn't matter<br>
Download a font you wish to use (does not come pre-installed)<br>
Configure dab-broadcast.conf <br>
Edit run.py to suit your needs.<br>

### Use with other standards?

In theory, dab-slideshow can be modified to be used with HD Radio (DRM uses the same size slideshow so you do not need to modify anything), all you need to modify is the following 
<br>
- Resolution of image
- Position of text
- Size of image
HD Radio supports 200x200px with a maximum size of 24 KB.

If any issues arise, please leave an issue and I will look into it. Thanks!
