class File_processing:
    """Class that performs statistical processing of a text file (counts characters, words and sentences)"""

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            output = file.read()
            self.__content = output
            self.__chars = len(output)
            self.__words = len(output.split())
            self.__sentences = len(output.split('.'))

    def content(self):
        return self.__content

    def chars(self):
        return self.__chars

    def words(self):
        return self.__words

    def sentences(self):
        return self.__sentences


file1 = File_processing('D:\\PycharmProjects\\lab_2.2\\text.txt')
print(file1.content())
print("Characters: ", file1.chars(), " Words: ", file1.words(), " Sentences: ", file1.sentences())
