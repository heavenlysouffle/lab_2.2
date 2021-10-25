import math


class Group:
    """Class that contains a sequence of instances of the class STUDENT"""

    def __init__(self):
        self.__students = []

    def add(self, *students):
        """Method for adding the student(s) to the group"""
        if len(self.__students) + len(students) > 20:
            raise ValueError("the number of people in group can't be more than 20")
        for student in students:
            if not isinstance(student, Student):
                raise TypeError
            for registered in self.__students:
                if student.name == registered.name and student.surname == registered.surname:
                    raise ValueError("this student has been registered already")
            self.__students.append(student)

    def remove(self, *students):
        """Method for removing the student(s) from the group"""
        if len(self.__students) - len(students) < 0:
            raise ValueError("not enough students")
        for student in students:
            if not isinstance(student, Student):
                raise TypeError
            self.__students.remove(student)

    def highest_score(self):
        """Method that find the five students with the highest average score"""
        if len(self.__students) < 5:
            raise ValueError("at least 5 students are needed")
        self.__students.sort()
        return self.__students[:5]


class Student:
    """Class that contains information about the student (surname, name, record_number, grades)"""

    def __init__(self, surname, name, record_number, grades):
        if not isinstance(record_number, int) or not isinstance(grades, dict):
            raise TypeError
        if not grades:
            raise ValueError("no data")
        if record_number < 0:
            raise ValueError("record book number can't be less than zero")
        if int(math.log10(record_number)) + 1 != 7:
            raise TypeError("record book number must be of format XXXXXXX")
        for mark in grades.values():
            if not 1 <= mark <= 12:
                raise ValueError
        self.__surname = surname
        self.__name = name
        self.__record_number = record_number
        self.__grades = grades

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        if not surname:
            raise ValueError("no data")
        if not surname.isalpha():
            raise TypeError("surname can only consists of letters")
        self.__surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("no data")
        if not name.isalpha():
            raise TypeError("name can only consists of letters")
        self.__name = name

    def average(self):
        """Method that calculates the average score of the student"""
        average = 0
        for mark in self.__grades.values():
            average += mark
        average /= len(self.__grades)
        return average

    def __lt__(self, other):
        """Method that changes behaviour of the < operator (that is used by sort) and let use it for an object"""
        return self.average() > other.average()

    def __str__(self):
        """Method that represents a class's objects as a string"""
        return f'{self.__surname} {self.__name}: {"{:,.2f}".format(self.average())}'


student1 = Student("Bykova", "Polina", 1234567, {'Math': 4, 'English': 5})
student2 = Student("Geralt", "ofRivia", 7654321, {'Math': 3, 'English': 4})
student3 = Student("Ciri", "ofCintra", 2345678, {'Math': 5, 'English': 3})
student4 = Student("Yennefer", "ofVengerberg", 3456789, {'Math': 1, 'Literature': 3})
student5 = Student("Triss", "Merigold", 4567890, {'Math': 2, 'Literature': 5})
student6 = Student("Philippa", "Eilhart", 5678901, {'Math': 3, 'English': 3, 'Literature': 4})
student7 = Student("Bykova", "Polina", 1234567, {'Math': 3, 'English': 5})
group1 = Group()
group1.add(student1, student2, student3, student4, student5, student6)
for i in range(5):
    print(group1.highest_score()[i])
