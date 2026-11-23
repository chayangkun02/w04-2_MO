class Student:
    def __init__(self, sid, fullname, program):
        self._sid = sid
        self._fullname = fullname
        self._program = program

    def __str__(self):
        return f"รหัสนักศึกษา{self._sid} ชื่อ-นามสกุล {self._fullname} สาขาวิชา {self._program}"

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        self._sid = value

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, value):
        self._program = value