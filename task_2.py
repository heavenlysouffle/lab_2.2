import os.path


class File_processing:
    """Class that performs statistical processing of a text file (counts characters, words and sentences)"""

    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise Exception("there's no such file")
        self.__filepath = filepath
        self.__content = "content"
        self.__chars = 0
        self.__words = 0
        self.__sentences = 0

    def content(self):
        with open(self.__filepath, 'r') as file:
            output = file.readlines()
            for data in output:
                self.__content = output
        return self.__content

    def chars(self):
        with open(self.__filepath, 'r') as file:
            output = file.readlines()
            for data in output:
                self.__chars = len(output)
        return self.__chars

    def words(self):
        with open(self.__filepath, 'r') as file:
            output = file.readlines()
            for data in output:
                self.__words = len(output.split())
        return self.__words

    def sentences(self):
        with open(self.__filepath, 'r') as file:
            output = file.readlines()
            for data in output:
                self.__sentences = len(output.split('.'))
        return self.__sentences


file1 = File_processing('D:\\PycharmProjects\\lab_2.2\\text.txt')
print(file1.content())
print("Characters: ", file1.chars(), " Words: ", file1.words(), " Sentences: ", file1.sentences())
