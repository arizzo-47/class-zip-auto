import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import zipfile
import os

class Watcher:
    DIRECTORY_TO_WATCH = "C:\\Users\\rizzo\\OneDrive\\School Year\\Fourth Year 2019\\Spring 2020\\Python-automation-script\\class-zip-auto\\testStart"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        file_name = "code.zip"

        if event.event_type == 'created' or event.event_type == 'modified':
            print("Change in directory detected - %s.\n" % event.src_path)\

            new_file = (event.src_path).split('\\')
            if new_file[len(new_file) - 1] == file_name:
                directory_to_place = "C:\\Users\\rizzo\\OneDrive\\School Year\\Fourth Year 2019\\Spring 2020\\Python-automation-script\\class-zip-auto\\testStart"

                tempPath = directory_to_place + "\\tempDir"
        
                if not os.path.exists(tempPath):
                    os.mkdir(tempPath)
               
                unzip(file_name, tempPath)

                try:
                    os.remove(directory_to_place+"\\"+file_name)
                except:
                    print("Zip removed")
                

def unzip(source_filename, dest_dir):
    zf = zipfile.ZipFile(source_filename)
    zf.extractall(dest_dir)

if __name__ == '__main__':
    w = Watcher()
    w.run()