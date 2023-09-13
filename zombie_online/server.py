import socket
from _thread import *
import pickle

server = "192.168.0.16"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [(30, 500, 1), (30, 500, 1)]
key_exist = [1, 1]
def threaded_client(conn, player):
    global p1Ready
    global p2Ready
    global key_exist
    print(player)
    if player == 0:
        p1Ready = True
    else:
        p2Ready = True
    
    while not (p1Ready and p2Ready):
        pass

    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:    
            data = pickle.loads(conn.recv(2048*2))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received Pos: ", data)
                print("Sending Pos: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

        try:    
            data = pickle.loads(conn.recv(2048*2))
            print(data)
            key_exist = [key_exist[i] * data[i] for i in range(len(key_exist))]
            print(key_exist)
            if not data:
                print("Disconnected")
                break
            else:
                reply = key_exist
                print("Received keys: ", data)
                print("Sending keys: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


p1Ready = False
p2Ready = False
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1