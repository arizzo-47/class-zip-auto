# Anthony Rizzo

from watchdog.observers import Observer
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

folder_to_track = "C:\\Users\\rizzo\\OneDrive\\School Year\\Fourth Year 2019\\Spring 2020\\Python-automation-script\\class-zip-auto\\testStart"
folder_destination = "C:\\Users\\rizzo\\OneDrive\\School Year\\Fourth Year 2019\\Spring 2020\\Python-automation-script\\class-zip-auto\\testEnd"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
try:    
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()