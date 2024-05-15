class Directional:
    def __int__(self):
        pass

    def Move(self) -> list:
        pass

    def Type(self) -> chr:
        pass

    def ToX(self) -> int:
        return self.Move()[0]

    def ToY(self) -> int:
        return self.Move()[1]

class Left(Directional):
    def __init__(self):
        pass

    def Move(self) -> list:
        return [0, -1]

    def Type(self) -> chr:
        return '←'


class Right(Directional):
    def __init__(self):
        pass

    def Move(self) -> list:
        return [0, 1]

    def Type(self) -> chr:
        return '→'

class Down(Directional):
    def __init__(self):
        pass

    def Move(self) -> list:
        return [1, 0]

    def Type(self) -> chr:
        return '↓'


class Up(Directional):
    def __init__(self):
        pass

    def Move(self) -> list:
        return [-1, 0]

    def Type(self) -> chr:
        return '↑'
