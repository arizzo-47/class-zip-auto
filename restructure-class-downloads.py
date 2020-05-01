import time
import zipfile
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Monitor directory
class Watcher:
    monitor_directory = r"C:\Users\rizzo\OneDrive\Personal Projects\Python-automation-script\class-zip-auto\testFolder"

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
    
        # If monitored event is created or modified
        if event.event_type == 'created' or event.event_type == 'modified':
            print("Change in directory detected - %s.\n" % event.src_path)\

            # Store path and name of file created
            new_file_path = (event.src_path)
            new_file_path_list = new_file_path.split('\\')
            
            new_file = new_file_path_list[len(new_file_path_list) -1]
           
            fileSplit = os.path.splitext(new_file)
            extension = fileSplit[len(fileSplit) - 1]

            # If file is zip
            if extension == ".zip":
                # Unzip folder to temp location
                print(new_file_path)
                unzip(new_file, r"C:\Users\rizzo\OneDrive\Personal Projects\Python-automation-script\class-zip-auto\testFolder")

                # Remove zip folder after unzipping
                try:
                    os.remove(new_file_path)
                except:
                    print("Zip removed")
                
# Extracts zipfile to destination directory
def unzip(source_filename, file_path):

    zf = zipfile.ZipFile(source_filename)
    zf.extractall(file_path)

if __name__ == '__main__':
    w = Watcher()
    w.run()
