import io
from pprint import pprint
class WordsFinder:
    def __init__(self, *file_names):
        self.file_name = list(file_names)
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - '] 
                for sings in punctuation:
                    info.replace(sings, '')
                words = info.split()
                all_words[file_name] = words  
        return all_words
    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1
        return places
    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters

finder2 = WordsFinder('7.2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
