class Faculty:
    def __init__(self, facName):
        self._facName = facName

    def __str__(self):
        return f"{self._facName}"

    @property
    def facName(self):
        return self._facName

    @facName.setter
    def facName(self, value):
        self._facName = value