# coding=utf-8
import Server.Server_Tcp_Main_Connection
import Server.Server_Class
import Server.Server_Main
import threading
import socket

Server_Tcp_Main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listening(server_tcp_main_address):
    Server_Tcp_Main.bind(server_tcp_main_address)
    Server_Tcp_Main.listen(100)
    while True:
        print("Main_Listening...")
        new_tcp_main_connection = Server_Tcp_Main.accept()
        new_client = Server.Server_Class.Client(new_tcp_main_connection[0], new_tcp_main_connection[1])
        print(new_client.Address)
        new_tcp_main_connection_thread = threading.Thread(
            target=Server.Server_Tcp_Main_Connection.tcp_main_connection_thread,
            args=(new_client, Server.Server_Main.DbConnection)
        )
        new_tcp_main_connection_thread.start()

