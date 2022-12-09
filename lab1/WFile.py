import math
import re


class WFile:
    def __init__(self, path):
        self.path = path
        self.words_count = {}
        self.calculate_words_count()
        self.words_weight_coef = {}
        self.words_weight = {}
        self.eq_rate = 0
        self.words_from_search = []

    def calculate_words_count(self) -> None:
        with open(self.path, 'r') as file:
            for row in file:
                row = re.sub(r'[^\w\s]', '', row).lower()
                for word in row.split():
                    if word in self.words_count.keys():
                        self.words_count[word] += 1
                    else:
                        self.words_count[word] = 1

    # ф-ла 1.6
    def calculate_words_weight_coef(self, files_word_count: dict, files_count: int) -> None:
        for word in files_word_count.keys():
            if files_word_count[word] == 1 and files_count == 1:
                self.words_weight_coef[word] = 1
            else:
                self.words_weight_coef[word] = self.words_count[word] * math.log(files_count/files_word_count[word])


    def set_eq_rate(self, value: float) -> None:
        self.eq_rate = value
