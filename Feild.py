import Directional

class Feild:
   def __init__(self):
       pass

   def Type(self) -> chr:
       pass

   def IsFree(self) -> bool:
       pass

   def __repr__(self) -> str:
       pass


class Start(Feild):
    def __init__(self):
        pass
    def __repr__(self):
        return "S"
    def IsFree(self) -> bool:
        return True
    def Type(self) -> chr:
        return 'S'


class Finish(Feild):
    f = 0
    def __init__(self):
        f = 0
    def __repr__(self) -> str:
        return "F"
    def IsFree(self) -> bool:
        return True
    def Type(self) -> chr:
        return 'F'


class Wall(Feild):
    def __init__(self):
        pass
    def __repr__(self) -> str:
        return "W"
    def IsFree(self) -> bool:
        return False
    def Type(self) -> chr:
        return 'W'


class Empty(Feild):
    def __init__(self):
        pass
    def __repr__(self) -> str:
        return "."
    def IsFree(self) -> bool:
        return True
    def Type(self) -> chr:
        return 'E'

class Path(Feild):
    let = Directional.Up()

    def __init__(self, direct: Directional.Directional) -> None:
        self.let = direct

    def __repr__(self) -> str:
        return str(self.let.Type())
        #return "*"
    def IsFree(self) -> bool:
        return True
    def Type(self) -> chr:
        return 'P'


class Play(Feild):
    def __init__(self) -> None:
        pass
    def __repr__(self):
        return "P"
    def IsFree(self) -> bool:
        return True
    def Type(self) -> chr:
        return 'G'