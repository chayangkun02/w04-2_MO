class Program:
    def __init__(self, progName, faculty):
        self._progName = progName
        self._faculty = faculty

    def __str__(self):
        return f"{self._progName} ({self._faculty})"

    @property
    def progName(self):
        return self._progName

    @progName.setter
    def progName(self, value):
        self._progName = value

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, value):
        self._faculty = value