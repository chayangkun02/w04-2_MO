class Lecturer:
    def __init__(self, fullname):
        self._fullname = fullname

    def __str__(self):
        return f"{self._fullname}"

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value