from PIL import Image, ImageDraw, ImageFont
import requests
import datetime
import time

base_url = "https://<YOUR-INSTANCE-HERE>/api" # set this to http(s)://<YOUR INSTANCE HERE>/api

station = "<YOUR-SHORTCODE-HERE>" # put your shortcode here

last_songname = ""

while True:
    now_playing_url = base_url + "/nowplaying/" + station

    response = requests.get(now_playing_url)
    data = response.json()

    songname = data["now_playing"]["song"]["title"].split("(")[0].strip() # removes anything after '(' i.e. (Radio Edit)
    artistname = data["now_playing"]["song"]["artist"]

    if songname != last_songname:
        print("Song name:", songname)
        print("Artist name:", artistname)
        now = datetime.datetime.now()
        print("Last update:", now)

        image = Image.open("broadcast2.jpg")

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("liberation-sans-bold-italic.ttf", 17)
        NPtext = ImageFont.truetype("liberation-sans-bold-italic.ttf", 25)

        draw.text((25, 25), "NOW PLAYING:", fill="white", font=NPtext)
        draw.text((25, 55), songname, fill="white", font=font)
        draw.text((25, 75), artistname, fill="white", font=font)

        image.save("output.jpg")

        last_songname = songname

    # prints the song name and artist name logs every 10 seconds for monitoring (optional)
    print("Song name:", songname)
    print("Artist name:", artistname)
    
    time.sleep(10) # can be changed.

