import Directional as Dir

class Player:
    x = 0
    y = 0
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def Move(self, direct: Dir.Directional) -> None:
        self.x += direct.Move()[0]
        self.y += direct.Move()[1]

    def GetX(self) -> int:
        return self.x

    def GetY(self) -> int:
        return self.y