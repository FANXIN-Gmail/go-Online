# coding=utf-8
import Server_Main
import Server_Tcp_Game_Manage

def tcp_game_connection_thread(client, dbconnection):
    while True:
        try:
            message = client.from_socket.recv(2048).decode()
        except Exception as tcp_game_connection_error:
            print(tcp_game_connection_error)
            break
        print("Game", message)
        if message == "Quit":
            break
        elif message == "Fall":
            Server_Tcp_Game_Manage.Fall(client)
        elif message == "Rob":
            Server_Tcp_Game_Manage.Rob(client)
        elif message == "Submit":
            Server_Tcp_Game_Manage.Submit(client)
        else:
            pass
    try:
        Server_Main.Player_Online_List.remove(client)
    except Exception as remove_error:
        print(remove_error)
    client.from_socket.close()
    print("用户断开Tcp_Game连接!")


    