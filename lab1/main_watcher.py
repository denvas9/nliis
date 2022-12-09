import time
#import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from db_connection import get_database
from watcher_file_ops import reviewFolders

class FileSysDBHandler(FileSystemEventHandler):
    def __init__(self, db_collection, paths) -> None:
        super().__init__()
        self.db_collection = db_collection;
        self.paths = paths;
        reviewFolders(paths, db_collection)
        
    def on_any_event(self, event):
        if (event.is_directory):
            return
        reviewFolders(self.paths, self.db_collection)
        print(event.event_type, event.src_path)
    


if __name__ == '__main__':
    dbname = get_database()
    collection_name = dbname['files']
    
    paths = ['d:/EYAZIS/ILang1/text_a','d:/EYAZIS/ILang1/text_b']
    
    event_handler = FileSysDBHandler(collection_name, paths)
    
    
    observer = Observer()
    for watch_path in paths:
        observer.schedule(event_handler, path=watch_path, recursive=False)
        
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()