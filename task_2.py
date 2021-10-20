import os.path


class File_processing:
    """Class that performs statistical processing of a text file (counts characters, words and sentences)"""

    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise Exception("there's no such file")
        self.__filepath = filepath

    def chars(self):
        """Characters-counting method of class File_processing"""
        with open(self.__filepath, 'r') as file:
            content = file.readlines()
            chars = 0
            for line in content:
                chars += len(line)
        return chars

    def words(self):
        """Words-counting method of class File_processing"""
        with open(self.__filepath, 'r') as file:
            content = file.readlines()
            words = 0
            for line in content:
                words += len(line.split())
        return words

    def sentences(self):
        """Sentences-counting method of class File_processing"""
        with open(self.__filepath, 'r') as file:
            content = file.readlines()
            sentences = 0
            for line in content:
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                line = line.replace('?', '.')
                line = line.replace('!', '.')
                sentences += line.count('.')
        return sentences


file1 = File_processing('D:\\PycharmProjects\\lab_2.2\\text.txt')
print("Characters: ", file1.chars(), " Words: ", file1.words(), " Sentences: ", file1.sentences())
