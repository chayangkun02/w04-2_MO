from Faculty import Faculty
from Program import Program
from Student import Student
from Building import Building
from Room import Room
from Lecturer import Lecturer
from Subject import Subject
from Course import Course
from Enrollment import Enrollment

f01 = Faculty("วิทยาการคอมพิวเตอร์")
p01 = Program("ภูมิสารสนเทศ", f01)
s01 = Student("6814931002", "นายชยางกูร ขุนอินทอง", p01)

b01 = Building("40")
r434 = Room("434", b01)
r435 = Room("435", b01)
r436 = Room("436", b01)

e1 = Enrollment(2569, 2, s01)
e1.addCourse(Course(Subject('1031051', 'DB', 3), Lecturer('Nitat'), r435, 1))
e1.addCourse(Course(Subject('9042051', 'Web2', 3), Lecturer('Somchai'), r436, 1))

print(e1)
e1.listCourses()