import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ''
port = 1791

BIGNUMBER = 17917

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection....")

current_id = 0
information = {"Type": [0, 0], "High": [0, 0], "Weight": [0, 0], "Lab": ["W", "W"], "Name": ["user1", "user2"],
               "Move": [0, 0], "IsFinish": [0, 0]}


def threaded_client(user):
    global current_id, information
    user.send(str.encode(str(current_id)))
    current_id = 1
    clear_inf = ''
    while True:
        dirty_inf = user.recv(BIGNUMBER)
        clear_inf = dirty_inf.decode("utf-8")
        if not dirty_inf:
            user.send(str.encode("Finish"))
            break
        else:
            print("New Data:" + clear_inf)
            mas = clear_inf.split(" ")
            get_id = int(mas[1])
            command = mas[0]
            if command != "Lab" and command != "Name":
                information[command][get_id] = int(mas[2])
            else:
                information[command][get_id] = mas[2]
            new_id = 1 - get_id
            user.sendall(str.encode(command + " " + str(new_id) + " " + str(information[command][new_id])))
    print("Connection closed.")
    user.close()


while True:
    conn, addr = s.accept()
    print("Connection to: ", addr)
    start_new_thread(threaded_client, (conn,))