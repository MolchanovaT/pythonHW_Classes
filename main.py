class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lesson(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades_from_students:
                lector.grades_from_students[course] += [grade]
            else:
                lector.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

    def __middle_grade(self):
        sum_values = []
        len_values = []
        for value in self.grades.values():
            sum_values.append(sum(value))
            len_values.append(len(value))

        if sum(len_values) == 0:
            res = 0
        else:
            res = str(round(sum(sum_values) / sum(len_values), 2))
        return res

    def __str__(self):
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        middle_grade = self.__middle_grade()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {middle_grade}\nКурсы ' \
              f'в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}\n'
        return res

    def __eq__(self, other):
        if not isinstance(other, Student):
            return
        return self.__middle_grade() == other.__middle_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.__middle_grade() < other.__middle_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return
        return self.__middle_grade() > other.__middle_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_from_students = {}

    def __middle_grade_from_students(self):
        sum_values = []
        len_values = []
        for value in self.grades_from_students.values():
            sum_values.append(sum(value))
            len_values.append(len(value))
        if sum(len_values) == 0:
            res = 0
        else:
            res = str(round(sum(sum_values) / sum(len_values), 2))
        return res

    def __str__(self):
        middle_grade = self.__middle_grade_from_students()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {middle_grade}\n'
        return res

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.__middle_grade_from_students() == other.__middle_grade_from_students()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.__middle_grade_from_students() < other.__middle_grade_from_students()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.__middle_grade_from_students() > other.__middle_grade_from_students()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


python_lecturer = Lecturer('Python', 'Lecturer')
python_lecturer.courses_attached += ['Python']
java_lecturer = Lecturer('Java', 'Lecturer')
java_lecturer.courses_attached += ['Java']
lecturers_list = [python_lecturer, java_lecturer]

python_student = Student('Ruoy', 'Eman', 'your_gender')
python_student.courses_in_progress += ['Python']
python_student.courses_in_progress += ['Java']
python_student.rate_lesson(python_lecturer, 'Python', 9)
python_student.rate_lesson(python_lecturer, 'Python', 10)
python_student.rate_lesson(python_lecturer, 'Python', 6)
python_student.rate_lesson(python_lecturer, 'Java', 6)
python_student.rate_lesson(python_lecturer, 'Java', 8)
python_student.rate_lesson(python_lecturer, 'Java', 7)

java_student = Student('Adam', 'Sendler', 'male')
java_student.courses_in_progress += ['Java']
java_student.finished_courses += ['Python']
java_student.rate_lesson(java_lecturer, 'Java', 10)
java_student.rate_lesson(java_lecturer, 'Java', 10)
java_student.rate_lesson(java_lecturer, 'Java', 8)

students_list = [python_student, java_student]

python_reviewer = Reviewer('Python', 'Reviewer')
python_reviewer.courses_attached += ['Python']
python_reviewer.rate_hw(python_student, 'Python', 10)
python_reviewer.rate_hw(python_student, 'Python', 10)
python_reviewer.rate_hw(python_student, 'Python', 10)

java_reviewer = Reviewer('Java', 'Reviewer')
java_reviewer.courses_attached += ['Java']
java_reviewer.rate_hw(java_student, 'Java', 8)
java_reviewer.rate_hw(java_student, 'Java', 6)
java_reviewer.rate_hw(java_student, 'Java', 10)


def calc_middle_grade_hw(students, course_name):
    sum_values = []
    len_values = []
    for student in students:
        if course_name in student.courses_in_progress:
            for value in student.grades.values():
                sum_values.append(sum(value))
                len_values.append(len(value))
        else:
            continue
    if sum(len_values) == 0:
        res = 0
    else:
        res = str(round(sum(sum_values) / sum(len_values), 2))
    return res


def calc_middle_grade_lecturers(lecturers, course_name):
    sum_values = []
    len_values = []
    for lecturer in lecturers:
        if course_name in lecturer.courses_attached:
            for value in lecturer.grades_from_students.values():
                sum_values.append(sum(value))
                len_values.append(len(value))
        else:
            continue
    if sum(len_values) == 0:
        res = 0
    else:
        res = str(round(sum(sum_values) / sum(len_values), 2))
    return res


print(python_student)
print(java_student)

print(python_reviewer)
print(java_reviewer)

print(python_lecturer)
print(java_lecturer)

print(f"Средняя оценка студентов по курсу Java: {calc_middle_grade_hw(students_list, 'Java')}")
print(f"Средняя оценка лекторов по курсу Python: {calc_middle_grade_lecturers(lecturers_list, 'Python')}")
