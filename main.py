from pytube import YouTube
import os
import sys
from tkinter import *
from tkinter import ttk
import tkinter as tk

class yt_downloader:
        def __init__(self,master):

                window.title("YouTube Downloader")
                self.label = ttk.Label(master,text = "Enter Youtube url")
                self.label.grid(row= 0, column= 0, columnspan= 2)

                ttk.button(master,text="Download audio_only",command= self.audio_only).grid(row = 1, column= 0)

                ttk.Button(master,text="Download Video",command=self.video_with_audio).grid(row= 1,column= 1)

                




# Create the main window
# window = tk.Tk()


# Create a text field for entering the URL of the YouTube video
url_field = tk.Entry(window)

# Create radio buttons for selecting the media type (video with audio or audio only)
video_with_audio = tk.Radiobutton(window, text="Video with audio", value="video with audio")
audio_only = tk.Radiobutton(window, text="Audio only", value="audio only")

# Create radio buttons for selecting the download resolution
low_resolution = tk.Radiobutton(window, text="Low resolution", value="low")
high_resolution = tk.Radiobutton(window, text="High resolution", value="high")

# Create a button for initiating the download
download_button = tk.Button(window, text="Download")

# Arrange the widgets in the window
url_field.grid(row=0, column=0)
video_with_audio.grid(row=1, column=0)
audio_only.grid(row=1, column=1)
low_resolution.grid(row=2, column=0)
high_resolution.grid(row=2, column=1)
download_button.grid(row=3, column=0, columnspan=2)

# Start the main loop
window.mainloop()


        # Define a function to be called when the "Download" button is clicked
def ytD():
        
            # Get the URL of the YouTube video from the text field
        url = url_field.text()

            # Check if a URL was entered
        if url == "":
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter a URL")
                return

            # Create a YouTube object using the URL
        yt = YouTube(url)

            # Determine the media type (video with audio or audio only)
        if video_with_audio.isChecked():
                media_type = "video with audio"
        else:
                media_type = "audio only"

            # Determine the download resolution
        if low_resolution.isChecked():
                resolution = "low"
        else:
                resolution = "high"

            # Download the YouTube video
        if media_type == "video with audio" and resolution == "low":
                stream = yt.streams.filter(file_extension = "mp4", res = "144p").first()
        elif media_type == "video with audio" and resolution == "high":
                stream = yt.streams.filter(file_extension = "mp4", res = "480p").first()
        elif media_type == "audio only" and resolution == "low":
                stream = yt.streams.filter(file_extension = "mp3", abr = "64kbps").first()
        else:
                stream = yt.streams.filter(file_extension = "mp3", abr = "128kbps").first()

                # Download the video
                stream.download()

                # Show a message box indicating that the download was successful
                QtWidgets.QMessageBox.information(self, "Success", f"{yt.title} has been successfully downloaded.")
          

                # Download the audio
                stream.download()

                # Show a message box indicating that the download was successful
                QtWidgets.QMessageBox.information(self, "Download Complete", "The video has been downloaded to the current working directory")
                QtCore.QObject.connect()

        # Connect the "clicked" signal of the "Download" button to the "download" function
        self.download_button.clicked.connect(self.ytD)
        



# # Create a QApplication instance
# app = QtWidgets.QApplication(sys.argv)

# Create an instance of the MainWindow class
ytD()


