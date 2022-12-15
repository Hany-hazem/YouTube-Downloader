from pytube import YouTube
import os
import sys

print("Welcome to My YouTube Video and Audio Downloader ")
print("To Select Want You Want Type The Number For The Option ")
ans = "1"
while ans == "1":
                        yt = str(input("Enter the URL of the video you want to download: \n>> "))
                        while yt == "" :
                            print("No URL Found.")
                            yt = str(input("Enter the URL of the video you want to download: \n>> "))

                            
                        yt = YouTube(yt)
                        # yt.caption_tracks()
                        print("Select download format:")
                        print("1: Video file with audio (.mp4)")
                        print("2: Audio only (.mp3)")

                        media_type = int(input(">> "))
                        while media_type == "" :
                            print("Invalid selection.")
                            print("Select download format:")
                            print("1: Video file with audio (.mp4)")
                            print("2: Audio only (.mp3)")
                            media_type = int(input(">> "))

                        while media_type != 1 and media_type != 2:
                                        print("Invalid selection.")
                                        print("Select download format:")
                                        print("1: Video file with audio (.mp4)")
                                        print("2: Audio only (.mp3)")
                                        media_type = int(input(">> "))
                        if media_type == 2:

                            print("Enter the destination (leave blank for current directory)")
                            destination = str(input(">> ")) or '.'

                            audio = yt.streams.filter(only_audio = True).first()
                            print("Downloading...")
                            out_file = audio.download(output_path = destination)
                            print(yt.title + " has been successfully downloaded.")
                            
                            if media_type == 2:
                                base, ext = os.path.splitext(out_file)
                                new_file = base + '.mp3'
                                os.rename(out_file, new_file)

                        if media_type == 1:    

                                        print("Select download Resolution:")
                                        print("1: Low-Resolution ")
                                        print("2: High-Resolution ")
                                        Or = int(input(">> "))

                                        while Or != 1 and Or != 2:
                                            print("Invalid selection.")
                                            print("Select download Resolution:")
                                            print("1: Low-Resolution ")
                                            print("2: High-Resolution ")
                                            Or = int(input(">> "))

                                        if Or == 1:
                                            print("Enter the destination (leave blank for current directory)")
                                            destination = str(input(">> ")) or '.'
                                            low = yt.streams.get_lowest_resolution()
                                            print("Downloading...")
                                            low.download(output_path = destination)
                                            print(yt.title + " has been successfully downloaded in Low Resolution.")
                                        if Or == 2:
                                            print("Enter the destination (leave blank for current directory)")
                                            destination = str(input(">> ")) or '.'
                                            high = yt.streams.get_highest_resolution()
                                            print("Downloading...") 
                                            high.download(output_path = destination)
                                            print(yt.title + " has been successfully downloaded in High Resolution.")
                        print(r"------------------------------------------------")
                        ans = (input("do you want to Download another Youtube video ? ( press 1 for yes ,and anything else for no ) : "))
                        print(r"------------------------------------------------")
                        if ans != "1" :
                            print("Thank you for using my program, have a Nice Day :) ")