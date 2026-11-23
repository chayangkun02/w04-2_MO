class Course:
    def __init__(self, subject, lecturer, room, section=1):
        self._subject = subject
        self._lecturer = lecturer
        self._room = room
        self._section = section

    def __str__(self):
        return f"{self._subject} : Section {self._section} ห้อง : {self._room}"

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        self._section = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def lecturer(self):
        return self._lecturer

    @lecturer.setter
    def lecturer(self, value):
        self._lecturer = value

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        self._room = value