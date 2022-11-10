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
            'Студент\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self._average_grade()}\n'
            f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {self.finished_courses}\n'
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректные данные для сравнения!')
            return
        return self._average_grade() < other._average_grade()


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
            'Лектор\n'
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self._average_grade()}\n'
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректные данные для сравнения!')
            return
        return self._average_grade() < other._average_grade()


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
        res = f"Ревьювер\nИмя: {self.name}\nФамилия: {self.surname}"
        return res


best_student = Student('Boris', 'Uhov', 'male')
student_2 = Student('Vlad', 'Segreev', 'male')
cool_lecturer = Lecturer('Ivan', 'Minakov')
lecturer_2 = Lecturer('Sergey', 'Petrov')
reviewer = Reviewer('Mike', 'Vazovzki')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']


best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 9)
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Git', 7)
best_student.rate_lect(cool_lecturer, 'Git', 9)
best_student.rate_lect(lecturer_2, 'Python', 7)
best_student.rate_lect(lecturer_2, 'Python', 6)
best_student.rate_lect(lecturer_2, 'Python', 8)
best_student.rate_lect(lecturer_2, 'Git', 10)
best_student.rate_lect(lecturer_2, 'Git', 9)
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']
reviewer.rate_hw(best_student, 'Python', 7)
reviewer.rate_hw(best_student, 'Python', 5)
reviewer.rate_hw(best_student, 'Python', 9)
reviewer.rate_hw(best_student, 'Git', 8)
reviewer.rate_hw(best_student, 'Git', 9)
reviewer.rate_hw(best_student, 'Git', 8)
reviewer.rate_hw(student_2, 'Python', 6)
reviewer.rate_hw(student_2, 'Python', 8)
reviewer.rate_hw(student_2, 'Python', 9)
reviewer.rate_hw(student_2, 'Python', 4)
reviewer.rate_hw(student_2, 'Git', 6)
reviewer.rate_hw(student_2, 'Git', 9)

print(cool_lecturer)
print(best_student)
print(student_2)
print(best_student < student_2)
print(cool_lecturer < lecturer_2)
