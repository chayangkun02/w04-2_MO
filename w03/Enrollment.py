class Enrollment:
    def __init__(self, year, semester, student):
        self._year = year
        self._semester = semester
        self._student = student
        self._courses = []

    def addCourse(self, course):
        self._courses.append(course)

    def listCourses(self):
        for c in self._courses:
            print(c)

    def __str__(self):
        total_unit = sum(c.subject.subUnit for c in self._courses)
        return f"{self._student}: Register {total_unit} Unit"

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        self._student = value

    @property
    def courses(self):
        return self._courses