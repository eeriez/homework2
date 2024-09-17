class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}

        for item in self.file_names:
            with open(item, encoding='utf-8') as f:
                line = f.read().lower()
                symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for i in symbols_to_remove:
                    line = line.replace(i, '')

                words = line.split()
                all_words[item] = words
        return all_words

    def count(self, word):
        counter = 0
        count = {}
        for name, words in self.get_all_words().items():
            for item in words:
                if item.lower() == word.lower():
                    counter += 1
            count[name] = counter
        return count

    def find(self, word):
        position = {}
        pos = 1
        for name, words in self.get_all_words().items():
            for item in words:
                if item.lower() == word.lower():
                    position[name] = pos
                    break
                else:
                    pos += 1
        return position

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
