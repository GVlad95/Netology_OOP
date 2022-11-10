class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        res = " ".join(self.finished_courses)
        return res

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        count = 0
        avg = 0
        for grade in self.grades.values():
            avg += sum(grade) / len(grade)
            count += 1
        average = round(avg / count, 1)
        return average

    def __str__(self):
        res = (
            '\nСтудент\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self._average_grade()}\n'
            f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректные данные для сравнения!')
            return
        if self._average_grade() < other._average_grade():
            res = f'Средний балл студента {self.surname} ниже, чем у {other.surname}'
            return res
        else:
            res = f'Средний балл студента {other.surname} ниже, чем у {self.surname}'
            return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}

    def _average_grade(self):
        count = 0
        avg = 0
        for grade in self.lect_grades.values():
            avg += sum(grade) / len(grade)
            count += 1
        average = round(avg/count, 1)
        return average

    def __str__(self):
        res = (
            '\nЛектор\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self._average_grade()}'
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректные данные для сравнения!')
            return
        if self._average_grade() < other._average_grade():
            res = f'Средняя оценка лектора {self.surname} ниже, чем у {other.surname}'
            return res
        else:
            res = f'Средняя оценка лектора {other.surname} ниже, чем у {self.surname}'
            return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"\nРевьювер\nИмя: {self.name}\nФамилия: {self.surname}"
        return res


# def students_avg_rate(students, course):




Igor_Ivanov = Student('Igor', 'Ivanov', 'male')
Ira_Petrova = Student('Ira', 'Petrova', 'female')

Ivan_Minakov = Lecturer('Ivan', 'Minakov')
Gleb_Pavlov = Lecturer('Gleb', 'Pavlov')

Max_Vasin = Reviewer('Max', 'Vasin')
Kirill_Markov = Reviewer('Kirill', 'Markov')

Ivan_Minakov.courses_attached += ['Python']
Gleb_Pavlov.courses_attached += ['Git']

Max_Vasin.courses_attached += ['Python']
Kirill_Markov.courses_attached += ['Git']

Igor_Ivanov.courses_in_progress += ['Python']
Igor_Ivanov.courses_in_progress += ['Git']
Igor_Ivanov.add_courses('Basic Programming')
Ira_Petrova.courses_in_progress += ['Python']
Ira_Petrova.courses_in_progress += ['Git']
Ira_Petrova.add_courses('Basic Programming')

Igor_Ivanov.rate_lect(Ivan_Minakov, 'Python', 7)
Igor_Ivanov.rate_lect(Ivan_Minakov, 'Python', 9)
Ira_Petrova.rate_lect(Ivan_Minakov, 'Python', 8)
Ira_Petrova.rate_lect(Ivan_Minakov, 'Python', 6)
Igor_Ivanov.rate_lect(Gleb_Pavlov, 'Git', 9)
Igor_Ivanov.rate_lect(Gleb_Pavlov, 'Git', 8)
Ira_Petrova.rate_lect(Gleb_Pavlov, 'Git', 10)
Ira_Petrova.rate_lect(Gleb_Pavlov, 'Git', 6)

Max_Vasin.rate_hw(Igor_Ivanov, 'Python', 7)
Max_Vasin.rate_hw(Igor_Ivanov, 'Python', 6)
Max_Vasin.rate_hw(Ira_Petrova, 'Python', 9)
Max_Vasin.rate_hw(Ira_Petrova, 'Python', 8)
Kirill_Markov.rate_hw(Igor_Ivanov, 'Git', 8)
Kirill_Markov.rate_hw(Igor_Ivanov, 'Git', 7)
Kirill_Markov.rate_hw(Ira_Petrova, 'Git', 9)
Kirill_Markov.rate_hw(Ira_Petrova, 'Git', 9)

print(Ira_Petrova)
print(Igor_Ivanov)
print(Ira_Petrova < Igor_Ivanov)
print(Ivan_Minakov)
print(Gleb_Pavlov)
print(Ivan_Minakov < Gleb_Pavlov)
print(Max_Vasin)
print(Kirill_Markov)
