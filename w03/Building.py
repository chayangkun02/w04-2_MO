class Building:
    def __init__(self, buildingCode):
        self._buildingCode = buildingCode

    def __str__(self):
        return f"Building : {self._buildingCode}"

    @property
    def buildingCode(self):
        return self._buildingCode

    @buildingCode.setter
    def buildingCode(self, value):
        self._buildingCode = value