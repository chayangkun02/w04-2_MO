class Subject:
    def __init__(self, subCode, subName, subUnit):
        self._subCode = subCode
        self._subName = subName
        self._subUnit = subUnit

    def __str__(self):
        return f"{self._subCode}({self._subName})"

    @property
    def subCode(self):
        return self._subCode

    @subCode.setter
    def subCode(self, value):
        self._subCode = value

    @property
    def subName(self):
        return self._subName

    @subName.setter
    def subName(self, value):
        self._subName = value

    @property
    def subUnit(self):
        return self._subUnit

    @subUnit.setter
    def subUnit(self, value):
        self._subUnit = value