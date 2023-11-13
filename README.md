# dab-slideshow
Make smarter DAB slideshows!

## What does it do?
dab-slideshow is a project designed to recreate DAB slideshows such as Bayern 1's slideshow, which includes now playing information.

## How does it work? 
dab-slideshow uses the Azuracast API (currently) to grab song information, I may create a seperate branch which pulls from Icecast2 instead in the future.

## Potential use case?
dab-slideshow could be used in a DAB+ mux, alongside other slideshow images, such as station contact details, I have tried it in OpenDigitalRadio and it works well.

### Prerequisites
```
Any Operating System that supports Python
Python 3.11 or newer
Pillow (``pip install pillow``)
Requests (``pip install requests``)
Datetime (``pip install datetime``)
```
