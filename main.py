from PIL import Image, ImageDraw, ImageFont
import requests
import datetime
import time
import textwrap
import re

# Location of Azuracast API - example http(s)://<DOMAIN>/api
base_url = "<ENTER-URL-HERE>"

station = "<ENTER-SHORTCODE-HERE>" # station shortcode, example "program1"

last_songname = ""

# Initialize a variable to store the emergency message
emergency_message = ""

useIcecast = False # Change this to True if you want to use Icecast 2 or False to use Azuracast API.

while True:
    # checks for alerts
    f = open("alert.txt", "r")
    emergency_message = f.read()
    # Close the file
    f.close()
    
    if useIcecast:
        # Provide the icecast mount here, format is http(s)://<URL>/status-json.xsl?mount=</mount.codec> e.g http://10.0.10.2/status-json.xsl?mount=/radio.mp3
        now_playing_url = "<ENTER-URL-HERE>"
        response = requests.get(now_playing_url)
        data = response.json()
        songname = data.get("icestats", {}).get("source", {}).get("title", "")
        # Split the song name by the dash (-) character
        songname_split = songname.split("-")
        if len(songname_split) == 2:
            artistname = songname_split[0].strip()
            songname = songname_split[1].strip()
        else:
            # If the split result does not have two elements, use the original song name and leave the artist name empty
            artistname = ""
        songname = re.sub(r"\(.*?\)", "", songname).strip()
    else:
        # Azuracast API
        now_playing_url = base_url + "/nowplaying/" + station
        response = requests.get(now_playing_url)
        data = response.json()
        songname = data.get("now_playing", {}).get("song", {}).get("title", "").split("(")[0].strip() # removes anything after '(' i.e. (Radio Edit)
        artistname = data.get("now_playing", {}).get("song", {}).get("artist", "")

    # Check if the song title has changed
    if songname != last_songname:
        # prints the current song and when it was last updated, only for troubleshooting
        print("Song name:", songname)
        print("Artist name:", artistname)
        now = datetime.datetime.now()
        print("Last update:", now)
        
        if emergency_message:
            # this can be any image as long as it's 320x240 and in jpg form
            image = Image.open("emergencybg.jpg")
        else:
            # this can be any image as long as it's 320x240 and in jpg form
            image = Image.open("source.jpg")

        draw = ImageDraw.Draw(image)

        # Modify this to the font you provided
        songfont = ImageFont.truetype("FONT.ttf", 17)
        artistfont = ImageFont.truetype("FONT.ttf", 13)
        NPtext = ImageFont.truetype("FONT.ttf", 20)
        EMtext = ImageFont.truetype("FONT.ttf", 15)

        # this is an optional function, you can keep alert.txt empty and it will not be used.
        if emergency_message:
            wrapped_message = textwrap.fill(emergency_message, width=40)
            lines = wrapped_message.split("\n")
            y_text = 30
            for line in lines:
                draw.text((15, y_text), line, fill="white", font=EMtext)
                y_text += EMtext.getsize(line)[1]
        else:
            draw.text((30, 30), "Now Playing", fill="white", font=NPtext)
            draw.text((30, 60), songname, fill="white", font=songfont)
            draw.text((30, 80), artistname, fill="white", font=artistfont)

        image.save("output.jpg")

        last_songname = songname

    print("Song name:", songname)
    print("Artist name:", artistname)
    
    # Sleep for 10 seconds before checking again
    time.sleep(10)

