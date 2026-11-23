class Room:
    def __init__(self, roomCode, building=None):
        self._roomCode = roomCode
        self._building = building

    def __str__(self):
        return f"Room : {self._roomCode}"

    @property
    def roomCode(self):
        return self._roomCode

    @roomCode.setter
    def roomCode(self, value):
        self._roomCode = value

    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, value):
        self._building = value