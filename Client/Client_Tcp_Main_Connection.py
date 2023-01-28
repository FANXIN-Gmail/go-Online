# coding=utf-8
import Client.Client_Tcp_Main_Manage
import Client.GUI_Hall

def tcp_main_connection_thread(self):
    while True:
        message = Client.Client_Tcp_Main_Manage.Client_Tcp_Main.recv(2048).decode()
        print(message)

        if message == "Match":
            self.Matching_Master = Client.Client_Tcp_Main_Manage.Client_Tcp_Main.recv(2018).decode()
            if Client.GUI_Hall.Hall.Matching_Flag or Client.GUI_Hall.Hall.Playing_Flag:
                Client.Client_Tcp_Main_Manage.Client_Refuse(self.Matching_Master)
                continue
            else:
                Client.GUI_Hall.Hall.Matching_Flag = True
            self.Signal.show_invitation_signal.emit()

        elif message == "Refuse":
            self.respond_number += 1
            if self.respond_number == self.invitation_number:
                print("匹配结束!")
                self.invitation_number = 0
                self.respond_number = 0
                Client.GUI_Hall.Hall.Matching_Flag = False

        elif message == "Accept":
            self.accept_sender = Client.Client_Tcp_Main_Manage.Client_Tcp_Main.recv(2048).decode()
            self.respond_number += 1
            if self.respond_number == self.invitation_number:
                print("匹配结束!")
                self.invitation_number = 0
                self.respond_number = 0
                Client.GUI_Hall.Hall.Matching_Flag = False
            else:
                pass
            if Client.GUI_Hall.Hall.Playing_Flag:
                continue
            else:
                print("Send Playing")
                Client.Client_Tcp_Main_Manage.Client_Playing(self.accept_sender)
            Client.GUI_Hall.Hall.Playing_Flag = True
            self.State = "Black"
            self.Signal.show_game_signal.emit()

        elif message == "Playing":
            self.State = "White"
            Client.GUI_Hall.Hall.Playing_Flag = True
            self.Signal.show_game_signal.emit()

        elif message == "Message":
            message = Client.Client_Tcp_Main_Manage.Client_Tcp_Main.recv(2048).decode()
            self.textEdit_Chat.append(message)

        else:
            pass



        





