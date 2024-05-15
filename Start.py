import Map
import Directional
import Network as con
import time

class Game:
    #mp = Map.Map(10, 10, 1)

    def __init__(self, string: int, colums: int, type: int):
        self.mp = Map.Map(string, colums, type, "W")
        self.net = con.Network()
        self.name = ""

    def Download(self, string: str):
        self.mp.Download(string)

    def ToConsole(self):
        print(self)

    def PrintToFile(self, string: str):
        self.PrintToFile(string)

    def Move(self, direct: Directional.Directional):
        self.mp.Moving(direct)

    def BuildPath(self):
        self.mp.Path()

    def DeletePath(self):
        self.mp.DeletePath()

    def CreateNew(self, strings: int, colums: int, type: int, map: str):
        self.mp = Map.Map(strings, colums, type, map)

    def PrintCommand(self):
        #print("Create -> Create <strings> <colums> <type>")
        print("Tips -> T")
        print("Move Up -> W")
        print("Move Down -> S")
        print("Move Right -> D")
        print("Move Left -> A")
        #print("Build Path -> Help")
        #print("Delete Path -> Delete")
        #print("Print To File -> Load <string>")
        #print("Download from file -> Download <string>")

    def PrintCommandAfterFinish(self):
        print("Build Path -> Help")
        print("Delete Path -> Delete")
        print("Print To File -> Load <string>")
        print("Exit -> Exit")
    '''def Play(self, gen=False):
        self.PrintCommand()
        if gen:
            print("Before the game create map")
            com = input().split()
            if com[0].lower() == "create":
                self.mp = Map.Map(int(com[1]), int(com[2]), int(com[3]))
            elif com[0].lower() == "download":
                self.mp.Download(com[1])
            else:
                print("Incorrect. Try again")
                self.Play()
                return
        fl = True
        while not self.mp.End():
            if fl:
                print(self.mp)
            fl = True
            com = input().split()
            if com[0].lower() == "create":
                self.mp = Map.Map(int(com[1]), int(com[2]), int(com[3]))
            if com[0].lower() == "t":
                fl = False
                self.PrintCommand()
            if com[0].lower() == "w":
                self.Move(Directional.Up())
            if com[0].lower() == "s":
                self.Move(Directional.Down())
            if com[0].lower() == "d":
                self.Move(Directional.Right())
            if com[0].lower() == "a":
                self.Move(Directional.Left())
            if com[0].lower() == "help":
                self.BuildPath()
            if com[0].lower() == "delete":
                self.DeletePath()
            if com[0].lower() == "download":
                self.mp.Download(com[1])
            if com[0].lower() == "load":
                self.mp.PrintToFile(com[1])
        print("It is over. Do you want to play again")
        string = input("yes/no ")
        if string == "yes":
            self.Play()
        return
    '''
    def send(self, info, strings: str):
        information = strings + " " + str(self.net.id) + " " + str(info)
        coding = self.net.send(information)
        return coding

    def parse(self, dirty_info):
        return dirty_info.split(" ")

    def prev_game(self):
        #self.PrintCommand()
        local_type = 0
        local_high = 0
        local_width = 0
        local_string = ""
        self.name = input("Your name: ")
        self.send(self.name, "Name")
        if self.net.id == 0:
            type = input("DFS or Tree: ")
            if type == "DFS":
                local_type += 1
            else:
                local_type += 2
            self.send(local_type, "Type")
        else:
            print("Waiting opponent...")
            while self.parse(self.send(0, "Type"))[2] == "0":
                local_type += int(self.parse(self.send(0, "Type"))[2])
            local_type = int(self.parse(self.send(0, "Type"))[2])
        if self.net.id == 1:
            local_high += int(input("Choose hieght: "))
            self.send(local_high, "High")
        else:
            print("Waiting opponent...")
            while self.parse(self.send(0, "High"))[2] == "0":
                local_high += int(self.parse(self.send(0, "High"))[2])
            local_high = int(self.parse(self.send(0, "High"))[2])
        if self.net.id == 0:
            local_width += int(input("Choose weight: "))
            self.send(local_width, "Weight")
        else:
            print("Waiting opponent...")
            while self.parse(self.send(0, "Weight"))[2] == "0":
                local_width += int(self.parse(self.send(0, "Weight"))[2])
            local_width = int(self.parse(self.send(0, "Weight"))[2])
        print("Starting generation")
        self.send(local_type, "Type")
        self.send(local_high, "High")
        self.send(local_width, "Weight")
        if self.net.id == 1:
            self.CreateNew(local_high, local_width, local_type, "W")
            string = str(self.mp)[:-1]
            self.send(string, "Lab")
        else:
            while self.parse(self.send("W", "Lab"))[2] == "W":
                local_string = self.parse(self.send("W", "Lab"))[2]
            local_string = self.parse(self.send("W", "Lab"))[2]
            self.send(local_string, "Lab")
            self.CreateNew(local_high, local_width, local_type, local_string)
        self.Playing()

    def Playing(self):
        self.PrintCommand()
        print("Become ready")
        time.sleep(2)
        moves = 0
        while not self.mp.End():
            print(self.mp)
            command = input("Command: ")
            if command.lower() == "t":
                self.PrintCommand()
                continue
            if command.lower() == "s":
                self.Move(Directional.Down())
            if command.lower() == "w":
                self.Move(Directional.Up())
            if command.lower() == "d":
                self.Move(Directional.Right())
            if command.lower() == "a":
                self.Move(Directional.Left())
            moves += 1
            self.send(moves, "Move")
        if self.parse(self.send(1, "IsFinish"))[2] == "0":
            print("You opponent is not finish maze ...")
        while self.parse(self.send(1, "IsFinish"))[2] == "0":
            x = 0
        print("You opponent finish maze...")
        second_moves = int(self.parse(self.send(moves, "Move"))[2])
        if second_moves > moves:
            print("You win")
        elif second_moves == moves:
            print("Draw")
        else:
            print("You loose")
        print("Now you can see this maze without player")
        time.sleep(2)
        self.AfterPlay()

    def AfterPlay(self):
        self.PrintCommandAfterFinish()
        self.mp.DeletePlayer()
        command = input("Your command: ")
        while command.lower() != "exit":
            if command.lower() == "help":
                self.BuildPath()
                print(self.mp)
            if command.lower() == "delete":
                self.DeletePath()
                print(self.mp)
            if "load" in command:
                command = command.split()
                self.PrintToFile(command[1])
            command = input("Your command: ")
        print("Exit")

