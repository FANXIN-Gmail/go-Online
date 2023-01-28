# coding=utf-8
import Client.Client_Tcp_Game_Manage
import Client.GUI_Hall


def tcp_game_connection_thread(self):
    while True:
        try:
            message = Client.Client_Tcp_Game_Manage.Client_Tcp_Game.recv(2048).decode()
        except Exception as recv_error:
            print(recv_error)
            break
        print(message)
        if message == "Fall":
            spot = Client.Client_Tcp_Game_Manage.Client_Tcp_Game.recv(2048).decode()
            x = ""
            y = ""
            information = ""
            for i in spot:
                if i == ".":
                    x = information
                    information = ""
                    continue
                else:
                    information+=i

            y = information
            self.check_begin(int(x), int(y), 1)
        elif message == "Rob":
            dead_spot = Client.Client_Tcp_Game_Manage.Client_Tcp_Game.recv(2048).decode()
            spot = Client.Client_Tcp_Game_Manage.Client_Tcp_Game.recv(2048).decode()
            information = ""
            x = ""
            y = ""
            for i in spot:
                if i == ".":
                    x = information
                    information = ""
                    continue
                else:
                    information+=i
            y = information
            information = ""
            dead_x = ""
            dead_y = ""
            for i in dead_spot:
                if i == ".":
                    dead_x = information
                    information = ""
                    continue
                else:
                    information+=i
            dead_y = information
            self.check_begin(int(x), int(y), 1)
            self.Rob = [int(dead_x), int(dead_y)]
        elif message == "Submit":
            Client.GUI_Hall.Hall.Playing_Flag = False
            self.close()
            break
        else:
            pass

        

