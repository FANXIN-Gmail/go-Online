# coding=utf-8
import Server_Tcp_Game_Connection
import Server_Class
import Server_Main
import threading
import socket

Server_Tcp_Game = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listening(server_tcp_game_address):
    Server_Tcp_Game.bind(server_tcp_game_address)
    Server_Tcp_Game.listen(100)
    while True:
        print("Game_Listening...")
        new_tcp_game_connection = Server_Tcp_Game.accept()
        new_client = Server_Class.Game_Room(new_tcp_game_connection[0], new_tcp_game_connection[1])
        Server_Main.Player_Online_List.append(new_client)
        new_tcp_game_connection_thread = threading.Thread(
            target=Server_Tcp_Game_Connection.tcp_game_connection_thread,
            args=(new_client, Server_Main.DbConnection)
        )
        new_tcp_game_connection_thread.start()

        