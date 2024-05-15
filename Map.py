import Feild
import Directional
import random
import sys
import Player

sys.setrecursionlimit(1000000000)

class Map:
    map = [[]]
    cnt_strings = 0
    cnt_colums = 0
    last = Feild.Start()

    def __init__(self, string: int, col: int, type: int, maze: str):
        self.last = Feild.Start()
        self.cnt_colums = col
        self.cnt_strings = string
        self.map = [[Feild.Wall() for x in range(col)] for i in range(string)]
        if maze.count('P') == 1:
            arr = maze.split('\n')
            for i in range(self.cnt_strings):
                for j in range(self.cnt_colums):
                    if arr[i][j] == 'S' or arr[i][j] == 'P':
                        self.map[i][j] = Feild.Play()
                    elif arr[i][j] == 'F':
                        self.map[i][j] = Feild.Finish()
                    elif arr[i][j] == '.':
                        self.map[i][j] = Feild.Empty()
                    else:
                        self.map[i][j] = Feild.Wall()
            return
        if type == 1:
            self.DFS(1, 1)
        elif type == 0:
            return
        else:
            self.TreeGenerate()
        self.map[1][1] = Feild.Play()
        for i in range(self.cnt_strings):
            for j in range(self.cnt_colums):
                if self.map[self.cnt_strings - 1 - i][self.cnt_colums - 1 - j].IsFree():
                    self.map[self.cnt_strings - 1 - i][self.cnt_colums - 1 - j] = Feild.Finish()
                    return

    def DFS(self, x: int, y: int) -> None:
        hod = [Directional.Left(), Directional.Right(), Directional.Up(), Directional.Down()]
        cnt = 0
        for item in hod:
            xn = x + item.ToX()
            yn = y + item.ToY()
            if self.map[xn][yn].IsFree():
                cnt += 1
        if cnt > 1:
            return
        self.map[x][y] = Feild.Empty()
        random.shuffle(hod)
        for item in hod:
            xn = x + item.ToX()
            yn = y + item.ToY()
            if xn == 0 or yn == 0 or xn == self.cnt_strings - 1 or yn == self.cnt_colums - 1 or self.map[xn][yn].IsFree():
                continue
            self.DFS(xn, yn)

    def ChangeColor(self, color: list[list[int]], old: int, new: int):
        for i in range(len(color)):
            for j in range(len(color[i])):
                if color[i][j] == old:
                    color[i][j] = new

    def TreeGenerate(self):
        color = [[0 for i in range(self.cnt_colums)] for j in range(self.cnt_strings)]
        cnt = 1
        for i in range(1, self.cnt_strings - 1, 2):
            for j in range(1, self.cnt_colums - 1, 2):
                self.map[i][j] = Feild.Empty()
                color[i][j] = cnt
                cnt += 1
        bridge = []
        for i in range(1, self.cnt_strings - 1):
            for j in range(1 + i % 2, self.cnt_colums - 1, 2):
                bridge.append([i, j])
        random.shuffle(bridge)
        while len(bridge) > 0:
            place = bridge[-1]
            bridge.pop()
            x, y = place[0], place[1]
            up, left = 0, 0
            if place[0] % 2 == 1:
                up, left = 0, 1
            else:
                up, left = 1, 0
            if color[x + up][y + left] == color[x - up][y - left]:
                continue
            self.map[x][y] = Feild.Empty()
            if color[x + up][y + left] != 0:
                self.ChangeColor(color, color[x + up][y + left], color[x - up][y - left])



    def DeletePath(self):
        for i in range(self.cnt_strings):
            for j in range(self.cnt_colums):
                if self.map[i][j].Type() == 'P':
                    self.map[i][j] = Feild.Empty()
        if self.last.Type() == 'P':
            self.last = Feild.Empty()


    def Build(self, x: int, y: int, used: list) -> bool:
        hod = [Directional.Left(), Directional.Right(), Directional.Up(), Directional.Down()]
        used[x][y] = 1
        if self.map[x][y].Type() == 'F':
            return True
        if not self.map[x][y].IsFree():
            return False
        for i in hod:
            xnew = x + i.ToX()
            ynew = y + i.ToY()
            if xnew == len(used) or xnew == -1 or ynew == len(used[0]) or ynew == -1 or used[xnew][ynew] == 1:
                continue
            if self.Build(xnew, ynew, used) and self.map[x][y].Type() != 'S':
                if self.map[x][y].Type() != 'G':
                    self.map[x][y] = Feild.Path(i)
                else:
                    self.last = Feild.Path(i)
                return True
        return False

    def Path(self) -> None:
        used = [[0 for i in range(self.cnt_strings)] for j in range(self.cnt_colums)]
        self.Build(1, 1, used)
        return

    def __repr__(self):
        string = ""
        for i in range(self.cnt_strings):
            for j in range(self.cnt_colums):
                string += str(self.map[i][j])
            string += '\n'
        return string

    def __str__(self):
        string = ""
        for i in range(self.cnt_strings):
            for j in range(self.cnt_colums):
                string += str(self.map[i][j])
            string += '\n'
        return string

    def PrintToFile(self, file: str) -> None:
        with open(file, "w", encoding='utf-8') as f:
            print(self, file=f)

    def DeletePlayer(self):
        player = self.FindPlayer()
        self.map[player.GetX()][player.GetY()] = self.last
        self.last = Feild.Play()

    def Download(self, file: str) -> None:
        with open(file, "r", encoding='utf-8') as f:
            helps = f.readlines()
        for i in range(len(helps)):
            helps[i] = helps[i].rsplit()
        helps.pop()
        self.map = [[Feild.Wall() for i in range(len(helps[0][0]))] for j in range(len(helps))]
        self.cnt_strings = len(helps)
        self.cnt_colums = len(helps[0][0])
        fl = False
        for i in range(len(helps)):
            for j in range(len(helps[i][0])):
                if helps[i][0][j] == 'W':
                    continue
                if helps[i][0][j] == 'S':
                    self.map[i][j] = Feild.Start()
                elif helps[i][0][j] == 'F':
                    self.map[i][j] = Feild.Finish()
                elif helps[i][0][j] == 'P':
                    self.map[i][j] = Feild.Play()
                else:
                    if helps[i][0][j] != '.':
                        fl = True
                    self.map[i][j] = Feild.Empty()
        self.last = Feild.Empty()
        if fl:
            self.Path()
        if self.map[1][1].Type() == 'G':
            self.last = Feild.Start()

    def FindPlayer(self) -> Player.Player:
        for i in range(self.cnt_strings):
            for j in range(self.cnt_colums):
                if self.map[i][j].Type() == 'G':
                    return Player.Player(i, j)

    def CanMove(self, play: Player.Player, direct: Directional.Directional) -> bool:
        return self.map[play.GetX() + direct.ToX()][play.GetY() + direct.ToY()].IsFree()

    def Moving(self, direct: Directional.Directional):
        player = self.FindPlayer()
        if self.CanMove(player, direct):
            self.map[player.GetX()][player.GetY()] = self.last
            player.Move(direct)
            self.last = self.map[player.GetX()][player.GetY()]
            self.map[player.GetX()][player.GetY()] = Feild.Play()
        else:
            print("You can not move to this way")

    def End(self) -> bool:
        return self.last.Type() == 'F'
