# coding=utf-8
import Server.Server_Main
import Server.Server_Tcp_Main_Manage


def tcp_main_connection_thread(client, dbconnection):
    while True:
        try:
            message = client.Socket.recv(2048).decode()
        except Exception as tcp_main_connection_error:
            print(tcp_main_connection_error)
            break
        print("main", message)
        if message == "Register":
            Server.Server_Tcp_Main_Manage.resister(client, dbconnection)
        elif message == "Login":
            Server.Server_Tcp_Main_Manage.login(client, dbconnection)
        elif message == "Match":
            Server.Server_Tcp_Main_Manage.Match(client)
        elif message == "Message":
            Server.Server_Tcp_Main_Manage.Message(client)
        elif message == "Refuse":
            Server.Server_Tcp_Main_Manage.Refuse(client)
        elif message == "Accept":
            Server.Server_Tcp_Main_Manage.Accept(client)
        elif message == "Playing":
            Server.Server_Tcp_Main_Manage.Playing(client)
        elif message == "Quit":
            break
        else:
            pass
    try:
        Server.Server_Main.Client_Online_List.remove(client)
    except Exception as remove_error:
        print(remove_error)
    client.Socket.close()
    print("用户断开Tcp_Main连接！")







