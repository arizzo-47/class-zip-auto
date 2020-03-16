import time
import zipfile
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Monitor directory
class Watcher:
    monitor_directory = r"C:\Users\rizzo\Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.monitor_directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

# Unzip, move, and rename starter folder
class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        file_name = "code.zip"

        # If monitored event is created or modified
        if event.event_type == 'created' or event.event_type == 'modified':
            print("Change in directory detected - %s.\n" % event.src_path)\

            # Compare folder to file name we care about
            new_file = (event.src_path).split('\\')
            if new_file[len(new_file) - 1] == file_name:
                directory_to_place = r"C:\Users\rizzo\OneDrive\School Year\Fourth Year 2019\Spring 2020\OOD\Download-Folder"

                tempPath = directory_to_place + "\\tempDir"
        
                if not os.path.exists(tempPath):
                    os.mkdir(tempPath)
               
                # Unzip folder to temp location
                unzip(file_name, tempPath)

                # Remove zip folder after unzipping
                try:
                    os.remove(directory_to_place+"\\"+file_name)
                except:
                    print("Zip removed")
                
# Extracts zipfile to destination directory
def unzip(source_filename, dest_dir):
    zf = zipfile.ZipFile(source_filename)
    zf.extractall(dest_dir)

if __name__ == '__main__':
    w = Watcher()
    w.run()
