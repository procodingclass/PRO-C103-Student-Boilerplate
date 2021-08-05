import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE "/ ") in VSC"
to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE "/ ") in VSC"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       
        name, extension = os.path.splitext(event.src_path)       
        time.sleep(1)
        print("name :" + name)
        print("extension :" + extension)



# Initialize event handler
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()

observer.join()