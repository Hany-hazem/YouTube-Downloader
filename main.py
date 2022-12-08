from pytube import YouTube
import os
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

# def yt_downloader():




#         print("Welcome to My YouTube Video and Audio Downloader ")
#         print("To Select Want You Want Type The Number For The Option ")
#         ans = "1"
#         while ans == "1":
#             yt = str(input("Enter the URL of the video you want to download: \n>> "))
#             while yt == "" :
#                 print("No URL Found.")
#                 yt = str(input("Enter the URL of the video you want to download: \n>> "))

                
#             yt = YouTube(yt)
#             # yt.caption_tracks()
#             print("Select download format:")
#             print("1: Video file with audio (.mp4)")
#             print("2: Audio only (.mp3)")

#             media_type = int(input(">> "))
#             while media_type == "" :
#                 print("Invalid selection.")
#                 print("Select download format:")
#                 print("1: Video file with audio (.mp4)")
#                 print("2: Audio only (.mp3)")
#                 media_type = int(input(">> "))

#             while media_type != 1 and media_type != 2:
#                             print("Invalid selection.")
#                             print("Select download format:")
#                             print("1: Video file with audio (.mp4)")
#                             print("2: Audio only (.mp3)")
#                             media_type = int(input(">> "))
#             if media_type == 2:

#                 print("Enter the destination (leave blank for current directory)")
#                 destination = str(input(">> ")) or '.'

#                 audio = yt.streams.filter(only_audio = True).first()
#                 print()
#                 out_file = audio.download(output_path = destination)
#                 print(yt.title + " has been successfully downloaded.")
                
#                 if media_type == 2:
#                     base, ext = os.path.splitext(out_file)
#                     new_file = base + '.mp3'
#                     os.rename(out_file, new_file)

#             if media_type == 1:    

#                             print("Select download Resolution:")
#                             print("1: Low-Resolution ")
#                             print("2: High-Resolution ")
#                             Or = int(input(">> "))

#                             while Or != 1 and Or != 2:
#                                 print("Invalid selection.")
#                                 print("Select download Resolution:")
#                                 print("1: Low-Resolution ")
#                                 print("2: High-Resolution ")
#                                 Or = int(input(">> "))

#                             if Or == 1:
#                                 print("Enter the destination (leave blank for current directory)")
#                                 destination = str(input(">> ")) or '.'
#                                 low = yt.streams.get_lowest_resolution()
#                                 print("Downloading...")
#                                 low.download(output_path = destination)
#                                 print(yt.title + " has been successfully downloaded in Low Resolution.")
#                             if Or == 2:
#                                 print("Enter the destination (leave blank for current directory)")
#                                 destination = str(input(">> ")) or '.'
#                                 high = yt.streams.get_highest_resolution()
#                                 print("Downloading...")
#                                 high.download(output_path = destination)
#                                 print(yt.title + " has been successfully downloaded in High Resolution.")

#             ans = (input("do you want to Download another Youtube video ? ( press 1 for yes ,and anything else for no ) : "))
#             if ans != "1" :
#                 print("Thank you for using my program, have a Nice Day :) ")
    # Create a QApplication instance
app = QtWidgets.QApplication(sys.argv) 

# Create a class for the main window of the GUI
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        

        # Set the window title and dimensions
        self.setWindowTitle('YouTube Downloader')
        self.setGeometry(200, 200, 800, 600)

        # Create a central widget for the window
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a layout for the central widget
        self.layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a label and a text field for the URL of the YouTube video
        self.label = QtWidgets.QLabel("Enter the URL of the YouTube video:")
        self.layout.addWidget(self.label)
        self.url_field = QtWidgets.QLineEdit()
        self.layout.addWidget(self.url_field)

        # Create a group box for the media type options
        self.media_type_group_box = QtWidgets.QGroupBox("Select download format:")
        self.layout.addWidget(self.media_type_group_box)

        # Create a layout for the media type group box
        self.media_type_layout = QtWidgets.QVBoxLayout()
        self.media_type_group_box.setLayout(self.media_type_layout)

        # Create radio buttons for the media type options
        self.video_with_audio = QtWidgets.QRadioButton("Video file with audio (.mp4)")
        self.media_type_layout.addWidget(self.video_with_audio)
        self.audio_only = QtWidgets.QRadioButton("Audio only (.mp3)")
        self.media_type_layout.addWidget(self.audio_only)

        # Set the default radio button to "Video file with audio"
        self.video_with_audio.setChecked(True)

        # Create a group box for the resolution options
        self.resolution_group_box = QtWidgets.QGroupBox("Select download resolution:")
        self.layout.addWidget(self.resolution_group_box)

        # Create a layout for the resolution group box
        self.resolution_layout = QtWidgets.QVBoxLayout()
        self.resolution_group_box.setLayout(self.resolution_layout)

        # Create radio buttons for the resolution options
        self.low_resolution = QtWidgets.QRadioButton("Low-Resolution")
        self.resolution_layout.addWidget(self.low_resolution)
        self.high_resolution = QtWidgets.QRadioButton("High-Resolution")
        self.resolution_layout.addWidget(self.high_resolution)

        # Set the default radio button to "Low-Resolution"
        self.low_resolution.setChecked(True)

                # Create a "Download" button
        self.download_button = QtWidgets.QPushButton("Download")
        self.layout.addWidget(self.download_button)

        # Define a function to be called when the "Download" button is clicked
    def download():
            # Get the URL of the YouTube video from the text field
            url = self.url_field.text()

            # Check if a URL was entered
            if url == "":
                QtWidgets.QMessageBox.warning(self, "Error", "Please enter a URL")
                return

            # Create a YouTube object using the URL
            yt = YouTube(url)

            # Determine the media type (video with audio or audio only)
            if self.video_with_audio.isChecked():
                media_type = "video with audio"
            else:
                media_type = "audio only"

            # Determine the download resolution
            if self.low_resolution.isChecked():
                resolution = "low"
            else:
                resolution = "high"

            # Download the YouTube video
            if media_type == "video with audio":
                # Get the highest resolution video stream that matches the selected resolution
                if resolution == "low":
                    stream = yt.streams.filter(file_extension = "mp4").get_lowest_resolution()
                else:
                    stream = yt.streams.filter(file_extension = "mp4").get_highest_resolution()

                # Download the video
                stream.download()

                # Show a message box indicating that the download was successful
                QtWidgets.QMessageBox.information(self, "Success", f"{yt.title} has been successfully downloaded.")
            else:
                # Get the highest bitrate audio stream
                stream = yt.streams.filter(only_audio = True).get_highest_bitrate()

                # Download the audio
                stream.download()

                # Show a message box indicating that the download was successful
                QtWidgets.QMessageBox.information(self, "Success", f"{yt.title} has been successfully downloaded.")

        # Connect the "clicked" signal of the "Download" button to the "download" function
            self.download_button.clicked.connect(download())



# # Create a QApplication instance
# app = QtWidgets.QApplication(sys.argv)

# Create an instance of the MainWindow class
window = MainWindow()

# Show the main window
window.show()

# Run the event loop
sys.exit(app.exec_())



