# Anthony Rizzo

from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = "new-file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file_" +str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)

            src = new_file_track + "/" + filename
            new_destination = folder_destinaton +"/" + filename
            os.rename(src, new_destination)

folder_to_track = "C:\\Users\rizzo\Downloads\code"
folder_destination = "C:\\Users\rizzo\Downloads\code"
event_handler = MyHandler()
observer = observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
try:    
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()