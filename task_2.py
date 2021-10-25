import os.path
import re


class File_processing:
    """Class that performs statistical processing of a text file (counts characters, words and sentences)"""

    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise Exception("there's no such file")
        self.__filepath = filepath

    def chars(self):
        """Characters-counting method of class File_processing"""
        with open(self.__filepath, 'r') as file:
            chars = 0
            for line in file:
                chars += len(line)
        return chars

    def words(self):
        """Words-counting method of class File_processing"""
        with open(self.__filepath, 'r') as file:
            words = 0
            for line in file:
                line = re.sub(r'[,.;@#?!&$]+', ' ', line)
                words += len(line.split())
        return words

    def sentences(self):
        """Sentences-counting method of class File_processing"""
        with open(self.__filepath, 'r') as file:
            sentences = 0
            for line in file:
                line = re.sub(r'[.?!]+', '|', line)
                line = line.lstrip('|')
                sentences += line.count('|')
        return sentences


file1 = File_processing('D:\\PycharmProjects\\lab_2.2\\text.txt')
print("Characters: ", file1.chars(), " Words: ", file1.words(), " Sentences: ", file1.sentences())
