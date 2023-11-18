# dab-slideshow.py

str = """
      _           _                     _   _       _                _                        
   __| |   __ _  | |__            ___  | | (_)   __| |   ___   ___  | |__     ___   __      __
  / _` |  / _` | | '_ \   _____  / __| | | | |  / _` |  / _ \ / __| | '_ \   / _ \  \ \ /\ / /
 | (_| | | (_| | | |_) | |_____| \__ \ | | | | | (_| | |  __/ \__ \ | | | | | (_) |  \ V  V / 
  \__,_|  \__,_| |_.__/          |___/ |_| |_|  \__,_|  \___| |___/ |_| |_|  \___/    \_/\_/  
                                                                                              
                                    VERSION 1.0.1 STABLE
"""

print(str)

from PIL import Image, ImageDraw, ImageFont
import requests
import datetime
import time
import textwrap
import re
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('dab-broadcast.conf')

# Read configuration values
icecast_url = config.get('dab-broadcast', 'icecast_url')
azuracast_url = config.get('dab-broadcast', 'azuracast_url')
station_shortcode = config.get('dab-broadcast', 'station_shortcode')
use_icecast = config.getboolean('dab-broadcast', 'use_icecast')
broadcast2_image_path = config.get('dab-broadcast', 'broadcast2_image')
output_image_path = config.get('dab-broadcast', 'output_image')
emergencybg_image_path = config.get('dab-broadcast', 'emergencybg_image')
alert_file_path = config.get('dab-broadcast', 'alert_file')
np_file_path = config.get('dab-broadcast', 'np_file')
artist_file_path = config.get('dab-broadcast', 'artist_file')
title_file_path = config.get('dab-broadcast', 'title_file')
np_font = config.get('dab-broadcast', 'np_font')
artist_font = config.get('dab-broadcast', 'artist_font')
title_font = config.get('dab-broadcast', 'title_font')
emergency_font = config.get('dab-broadcast', 'emergency_font')

# Initialize font variables with the updated font names
songfont = ImageFont.truetype(f"{title_font}", 17)
artistfont = ImageFont.truetype(f"{artist_font}", 13)
NPtext = ImageFont.truetype(f"{np_font}", 20)
EMtext = ImageFont.truetype(f"{emergency_font}", 15)

# Initialize a variable to store the emergency message
emergency_message = ""

# Initialize last_songname variable
last_songname = ""
eas_status_changed = False

while True:
    # checks for alerts
    with open(alert_file_path, "r") as f:
        new_emergency_message = f.read()

    # Check if the EAS status has changed
    if new_emergency_message != emergency_message:
        emergency_message = new_emergency_message
        eas_status_changed = True
        if emergency_message:
            print("Current EAS:", emergency_message)
            # Write emergency alert information to np.txt
            with open(np_file_path, 'w') as f:
                f.write(emergency_message)
            # Set title.txt to the alert
            with open(title_file_path, 'w') as f:
                f.write(emergency_message)
            # Set artist.txt to "Emergency Alert"
            with open(artist_file_path, 'w') as f:
                f.write("Emergency Alert")
        else:
            print("No alert being broadcast")
    else:
        eas_status_changed = False

    # Fetch now playing data from either Icecast or AzuraCast based on the configuration
    if use_icecast:
        now_playing_url = icecast_url
    else:
        now_playing_url = f"{azuracast_url}/nowplaying/{station_shortcode}"

    response = requests.get(now_playing_url)
    data = response.json()

    # Extract song information from the data
    if use_icecast:
        songname = data.get("icestats", {}).get("source", {}).get("title", "")
        artistname = ""
        # Split the song name by the dash (-) character
        songname_split = songname.split("-")
        if len(songname_split) == 2:
            artistname = songname_split[0].strip()
            songname = songname_split[1].strip()
            # Remove anything inside parentheses in the song name
            songname = re.sub(r"\(.*?\)", "", songname).strip()
        else:
            # If the split result does not have two elements, use the original song name and leave the artist name empty
            songname = re.sub(r"\(.*?\)", "", songname).strip()
    else:
        songname = data.get("now_playing", {}).get("song", {}).get("title", "").split("(")[0].strip()  # removes anything after '(' i.e. (Radio Edit)
        artistname = data.get("now_playing", {}).get("song", {}).get("artist", "")
        # Remove anything inside parentheses in the song name
        songname = re.sub(r"\(.*?\)", "", songname).strip()

    # Check if the song title or EAS status has changed
    if songname != last_songname or eas_status_changed:
        print("Song name:", songname)
        print("Artist name:", artistname)
        now = datetime.datetime.now()
        print("Last update:", now)

        if emergency_message:
            image = Image.open(emergencybg_image_path)
            draw = ImageDraw.Draw(image)
            wrapped_message = textwrap.fill(emergency_message, width=40)
            lines = wrapped_message.split("\n")
            y_text = 30
            for line in lines:
                draw.text((15, y_text), line, fill="white", font=EMtext)
                y_text += EMtext.getsize(line)[1]
        else:
            image = Image.open(broadcast2_image_path)
            draw = ImageDraw.Draw(image)
            draw.text((30, 30), "Now Playing", fill="white", font=NPtext)
            draw.text((30, 60), songname, fill="white", font=songfont)
            draw.text((30, 80), artistname, fill="white", font=artistfont)

            # Write now playing data to files
            with open(np_file_path, 'w') as f:
                f.write(f"{artistname} - {songname}")
            with open(artist_file_path, 'w') as f:
                f.write(artistname)
            with open(title_file_path, 'w') as f:
                f.write(songname)

        image.save(output_image_path)

        last_songname = songname

    print("Song name:", songname)
    print("Artist name:", artistname)

    # Sleep for 10 seconds before checking again
    time.sleep(10)

