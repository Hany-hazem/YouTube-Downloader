#test tk
from pytube import YouTube
import tkinter as tk

# Import the YouTube class from the pytube module
from pytube import YouTube

# Create the main window
window = tk.Tk()
window.title("YouTube Downloader")

# Create a text field for entering the URL of the YouTube video
url_label = tk.Label(window, text="URL:")
url_field = tk.Entry(window)

# Create radio buttons for selecting the media type (video with audio or audio only)
video_with_audio = tk.Radiobutton(window, text="Video with audio", value="video with audio")
audio_only = tk.Radiobutton(window, text="Audio only", value="audio only")

# Create radio buttons for selecting the download resolution
low_resolution = tk.Radiobutton(window, text="Low resolution", value="low",state=tk.NORMAL)
high_resolution = tk.Radiobutton(window, text="High resolution", value="high",state=tk.NORMAL)

# Create a button for initiating the download
download_button = tk.Button(window, text="Download")

# Arrange the widgets in the window
url_field.grid(row=0, column=0)
video_with_audio.grid(row=1, column=0)
audio_only.grid(row=1, column=1)
low_resolution.grid(row=2, column=0)
high_resolution.grid(row=2, column=1)
download_button.grid(row=3, column=0, columnspan=2)

# Define the callback function for the download button
def ytD():
    # Get the URL of the YouTube video from the text field
    url = url_field.get()

    # Check if a URL was entered
    if url == "":
        tk.messagebox.showwarning("Error", "Please enter a URL")
        return

    # Create a YouTube object using the URL
    yt = YouTube(url)

    # Determine the media type (video with audio or audio only)
    if video_with_audio.state() == tk.NORMAL:
        media_type = "video with audio"
    else:
        media_type = "audio only"

    # Determine the download resolution
    if low_resolution.state() == tk.NORMAL:
        resolution = "low"
    else:
        resolution = "high"

    # Download the YouTube video
    if media_type == "video with audio" and resolution == "low":
        stream = yt.streams.filter(file_extension="mp4", res="144p").first()
    elif media_type == "video with audio" and resolution == "high":
        stream = yt.streams.filter(file_extension="mp4", res="480p").first()
    elif media_type == "audio only" and resolution == "low":
        stream = yt.streams.filter(file_extension="mp3", abr="64kbps").first()
    else:
        stream = yt.streams.filter(file_extension="mp3", abr="128kbps").first()

    # Download the video
    stream.download()

    # Show a message box indicating that the download was successful
    tk.messagebox.showinfo("Success", f"{yt.title} has been successfully downloaded.")

# Connect the "clicked" signal of the "Download" button to the "download" function
download_button.config(command=ytD)

# Define a callback function for the "Audio only" radio button
def on_audio_only_selected():
    # Disable the "Low resolution" and "High resolution" radio buttons
    low_resolution.config(state=tk.DISABLED)
    high_resolution.config(state=tk.DISABLED)

# Define a callback function for the "Video with audio" radio button
def on_video_with_audio_selected():
    # Enable the "Low resolution" and "High resolution" radio buttons
    low_resolution.config(state=tk.NORMAL)
    high_resolution.config(state=tk.NORMAL)

# Connect the "selected" signal of the "Audio only" radio button to the "on_audio_only_selected" function
audio_only.config(command=on_audio_only_selected)

# Connect the "selected" signal of the "Video with audio" radio button to the "on_video_with_audio_selected" function
video_with_audio.config(command=on_video_with_audio_selected)

# Make the "Download" button the default button
window.bind("<Return>", lambda event: download_button.invoke())

# Start the main loop
window.mainloop()



