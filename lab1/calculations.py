import math
import os
import sys
from WFile import WFile

def get_folders_content(path: str) -> list:
    files_path_list = []

    for path, _, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.txt'):
                files_path_list.append(os.path.join(path, file))
                
    return files_path_list


def get_files_list(files_path_list: list) -> list:
    files_list = [WFile(file_path) for file_path in files_path_list]
    
    return files_list


def calculate_files_words_weight_coef(files_list: list):
    for file in files_list:
        for word in file.words_count.keys():
            file.calculate_words_weight_coef({word: len(get_files_with_word(word, files_list))}, len(files_list))


def get_files_with_word(word: str, files_list: list) -> list:
    files_with_word = []
    for file in files_list:
        if word.lower().strip() in file.words_count.keys():
            files_with_word.append(file)
            
    return files_with_word


def eq_rating(files: list, search: str):
    calculate_files_words_weight_coef(files)
    
    search_list = set(search.lower().split())
    
    for file in files:
        file.words_from_search = [word for word in file.words_weight_coef.keys() if word in search_list]
        
        eq_rate = 0
        for word in file.words_from_search:
            eq_rate += file.words_weight_coef[word]
            #print(word, file.words_weight_coef[word])
            
        file.set_eq_rate(eq_rate)

def sort_key(file):
    return file.eq_rate
