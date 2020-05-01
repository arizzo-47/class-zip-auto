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
    
        # If monitored event is created or modified
        if event.event_type == 'created':
            print("Change in directory detected - %s\n" % event.src_path)

            # Store path and name of file created
            new_file_path = (event.src_path)
            new_file_path_list = new_file_path.split('\\')

            monitor_directory = ""
            for item in new_file_path_list[:-1]:
                monitor_directory += item + '\\'

            new_file = new_file_path_list[len(new_file_path_list) -1]
           
            fileSplit = os.path.splitext(new_file)
            file_no_extension = ""
            
            # Loop through all but last element
            for item in fileSplit[:-1]:
                file_no_extension += item

            extension = fileSplit[len(fileSplit) - 1]

            # If file is zip
            if extension == ".zip":
                unzip_location = monitor_directory + file_no_extension

                index = 1
                while os.path.exists(unzip_location):
                    unzip_location = monitor_directory + file_no_extension + "(" + str(index) + ")"
                    index += 1

                unzip(new_file, unzip_location)

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
