import re
import os

def get_words(filePath) -> list[str]:
    res = set()
    
    with open(filePath, 'r') as file:
        for row in file:
            row = re.sub(r'[^\w\s]', '', row).lower()
            for word in row.split():
                res.add(word)
                    
    return list(res)
        
def get_folders_content(path: str) -> list:
    files_path_list = []

    for path, _, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.txt'):
                files_path_list.append(os.path.join(path, file).replace('\\','/'))
                
    return files_path_list

def reviewFolders(paths, db_collection): 
    db_collection.drop()
    for folderPath in paths:
        filePaths = get_folders_content(folderPath)
        for filePath in filePaths:
            db_collection.insert_one({
                'path':filePath,
                'words':get_words(filePath),
            })    
