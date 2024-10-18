import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for i in range(0, len(self.file_names)):
            lines_in_file = []
            with open(self.file_names[i], encoding='utf-8') as file:
                for line in file:
                    re_line = re.sub(r'[,.=!?;:-]', ' ', line)
                    lines_in_file += re_line.lower().split()
            all_words[self.file_names[i]] = lines_in_file
        return all_words

    def find(self, word):
        word_position = {}
        all_words = WordsFinder.get_all_words(self)
        for i in range(0, len(self.file_names)):
            word_position[self.file_names[i]] = all_words[self.file_names[i]].index(word.lower())+1
        return word_position

    def count(self, word):
        word_count = {}
        all_words = WordsFinder.get_all_words(self)
        for i in range(0, len(self.file_names)):
            word_count[self.file_names[i]] = all_words[self.file_names[i]].count(word.lower())
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
