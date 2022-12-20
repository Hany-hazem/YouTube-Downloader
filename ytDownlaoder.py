import subprocess

# Run the pip install command
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
# # Clear the terminal

import sys
import os
# Get the directory containing the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Append the path to the site-packages/subfolder directory
sys.path.append(os.path.join(script_dir, 'site-packages'))

# Now you can import the modules from the subfolder as usual
from pytube import YouTube
import urllib.request
from moviepy.editor import *
from mutagen.id3 import APIC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC
import mutagen
import ffmpeg
from PIL import Image
import io


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("Welcome to My YouTube Video and Audio Downloader ")
print("To Select Want You Want Type The Number For The Option ")
ans = "1"
while ans == "1":
    yt = str(input("Enter the URL of the video you want to download: \n>> "))
    while yt == "" :
        print("No URL Found.")
        yt = str(input("Enter the URL of the video you want to download: \n>> "))

    yt = YouTube(yt,use_oauth=False,allow_oauth_cache=True)
    # yt.caption_tracks()
    print("Select download format:")
    print("1: Video file with audio (.mp4)")
    print("2: Audio only (.mp3)")

    media_type = (input(">> "))
    while media_type == "" :
        print("Invalid selection.")
        print("Select download format:")
        print("1: Video file with audio (.mp4)")
        print("2: Audio only (.mp3)")
        media_type = int(input(">> "))

    while media_type != "1" and media_type != "2":
        print("Invalid selection.")
        print("Select download format:")
        print("1: Video file with audio (.mp4)")
        print("2: Audio only (.mp3 or .wav)")
        media_type = (input(">> "))
    if media_type == "2":

        print("select the audio file format")
        print("1: mp3 ")
        print("2: wav ")
        file_format = (input(">> "))
        while file_format != "1" and file_format != "2":
            print("Invalid selection.")
            print("select the audio file format")
            print("1: mp3 ")
            print("2: wav ")
            file_format = (input(">> "))

        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
        
        audio_streams = yt.streams.filter(only_audio=True)

        sorted_streams = sorted(audio_streams, key=lambda s: s.bitrate, reverse=True)

        highest_bitrate_stream = sorted_streams[0]


        print("Downloading...")
        # Download audio file to specified location
        out_file = highest_bitrate_stream.download(output_path=destination)
        print(yt.title + " has been successfully downloaded.")
        # Print value of out_file
        print(out_file)

        # Extract metadata
        metadata = {"Title": yt.title, "Description": yt.description, "Author": yt.author}

        if not os.path.exists(out_file):
            print("Error: File not found at", out_file)
        else:

            if file_format == "1":    #mp3 format

                # Load the audio file
                audio = AudioFileClip(out_file)

                # Save the audio as an MP3 file
                audio.write_audiofile(out_file + ".mp3",bitrate="320k")

                os.remove(out_file)

                 # Extract thumbnail URL
                thumbnail_url = yt.thumbnail_url

                # Download thumbnail image and save it to a file
                urllib.request.urlretrieve(thumbnail_url, "thumbnail.jpg")

                # Load the image data from the file into memory
                image_data = Image.open("thumbnail.jpg")

                # Open the MP3 file in mutagen
                audio = MP3(out_file+".mp3" )
                # Remove the existing ID3 tag
                audio.delete()

               # Set the metadata for the MP3 file using the ID3 tag
                audio["TIT2"] = TIT2(encoding=3, text=yt.title)
                audio["TPE1"] = TPE1(encoding=3, text=yt.author)
                audio["TALB"] = TALB(encoding=3, text=yt.title)
                audio["TPE2"] = TPE2(encoding=3, text=yt.author)
                audio["COMM"] = COMM(encoding=3, lang=u'eng', desc=u'desc', text=yt.description)
                audio["TCOM"] = TCOM(encoding=3, text=yt.author)

                # Add the ID3 tag to the MP3 file

                audio.save()

                # Add thumbnail to audio file
                with open("thumbnail.jpg", "rb") as f:
                    audio.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover', data=f.read()))

                audio.save()
                image_data.close()
                os.remove("thumbnail.jpg") 
        
            if file_format == "2" :
                # Load the audio from the Webm file
                audio = AudioFileClip(out_file)


                # Save the audio as an MP3 file
                audio.write_audiofile(out_file + ".wav",bitrate="25600k")

                os.remove(out_file)


                # Open the WAV file using mutagen
                audio = mutagen.File(out_file+".wav")

                # Remove the existing ID3 tag
                audio.delete()

                # Set the metadata for the MP3 file using the ID3 tag
                audio["TIT2"] = TIT2(encoding=3, text=yt.title)
                audio["TPE1"] = TPE1(encoding=3, text=yt.author)
                audio["TALB"] = TALB(encoding=3, text=yt.title)
                audio["TPE2"] = TPE2(encoding=3, text=yt.author)
                audio["COMM"] = COMM(encoding=3, lang=u'eng', desc=u'desc', text=yt.description)
                audio["TCOM"] = TCOM(encoding=3, text=yt.author)

                # Add the ID3 tag to the WAV file

                audio.save()
            


            audio.save()
              

        
        print(yt.title + " has been successfully downloaded. Thumbnail and metadata can be found in the same directory as the audio file.")




    if media_type == "1":    

        print("Select download Resolution:")
        print("1: Low-Resolution ")
        print("2: High-Resolution ")
        Or = (input(">> "))

        while Or != "1" and Or != "2":
            print("Invalid selection.")
            print("Select download Resolution:")
            print("1: Low-Resolution ")
            print("2: High-Resolution ")
            Or = int(input(">> "))

        if Or == "1":
            print("Enter the destination (leave blank for current directory)")
            destination = str(input(">> ")) or '.'
            low = yt.streams.get_lowest_resolution()
            print("Downloading...")
            low.download(output_path = destination)
            print(yt.title + " has been successfully downloaded in Low Resolution.")

        if Or == "2":
            print("Enter the destination (leave blank for current directory)")
            destination = str(input(">> ")) or '.'
            high = yt.streams.get_highest_resolution()
            print("Downloading...")
            high.download(output_path = destination)
            print(yt.title + " has been successfully downloaded in High Resolution.")

    print("Enter 1 to download another (video or audio ), press any key to exit")
    ans = input(">> ")

