# coding=utf-8
import time
import socket

Client_Tcp_Game = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostbyname(socket.gethostname()), 9999)
Client_Tcp_Game.bind(address)

def Tcp_game_Connection():
    try:
        Client_Tcp_Game.connect(("47.107.188.208", 9999))
        print("Tcp_Game连接成功!")
    except Exception as Tcp_Main_Connection_Error:
        print(Tcp_Main_Connection_Error)
        print("TCP_Game连接失败!")

def Client_Quit():
    Client_Tcp_Game.send("Quit".encode())

def Client_Fall(row, column):
    Client_Tcp_Game.send("Fall".encode())
    time.sleep(1/10)
    Client_Tcp_Game.send((str(row) + "." + str(column)).encode())
    
def Client_Rob(dead_row, dead_column, row, column):
    Client_Tcp_Game.send("Rob".encode())
    time.sleep(1/10)
    Client_Tcp_Game.send((str(dead_row) + "." + str(dead_column)).encode())
    time.sleep(1/10)
    Client_Tcp_Game.send((str(row) + "." + str(column)).encode())

def Client_Submit():
    Client_Tcp_Game.send("Submit".encode())
    







