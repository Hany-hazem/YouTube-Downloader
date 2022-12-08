# Import the necessary libraries
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from pytube import YouTube
import os

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
        self.low_resolution.setCheck

# Create a QApplication instance
app = QtWidgets.QApplication(sys.argv)

# Create an instance of the MainWindow class
window = MainWindow()

# Show the main window
window.show()

# Run the event loop
sys.exit(app.exec_())
