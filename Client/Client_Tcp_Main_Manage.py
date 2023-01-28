# coding=utf-8
import Client.GUI_Hall
import Client.Client_Tcp_Game_Manage
import socket

Client_Tcp_Main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostbyname(socket.gethostname()), 8888)
Client_Tcp_Main.bind(address)

def Tcp_Main_Connection():
    try:
        Client_Tcp_Main.connect(("47.107.188.208", 8888))
        print("Tcp_Main连接成功!")
    except Exception as Tcp_Main_Connection_Error:
        print(Tcp_Main_Connection_Error)
        print("TCP_Main连接失败!")

def Client_Login(Login_Ui):

    Client_Tcp_Main.send("Login".encode())
    Begin = Client_Tcp_Main.recv(2048).decode()
    if Begin == "Begin_Ok":
        Data = ""
        Data += Login_Ui.lineEdit_ID.text()
        Data += "+"
        Data += Login_Ui.lineEdit_Passworld.text()
        Data += "+"
        Data += "END"
        Client_Tcp_Main.send(Data.encode())
        Message = Client_Tcp_Main.recv(2048).decode()
        if Message == "End_Ok":
            return True
        else:
            return False

def Client_Register(Register_Ui):
    Client_Tcp_Main.send("Register".encode())
    Begin_Ok = Client_Tcp_Main.recv(2048).decode()
    if Begin_Ok == "Begin_Ok":
        Message =[Register_Ui.lineEdit_Mail.text(), "+", Register_Ui.lineEdit_NickName.text(), "+",
                  Register_Ui.lineEdit_Grade.text(), "+", Register_Ui.lineEdit_PassWord.text(), "+", "END"]
        for i in Message:
            Client_Tcp_Main.send(i.encode())
        End_Ok = Client_Tcp_Main.recv(2048).decode()
        if End_Ok == "End_Ok":
            return True
        else:
            return False

def Client_Match(self):
    self.invitation_number = self.client_number - 1
    print(self.invitation_number)
    if self.invitation_number == 0:
        print("匹配结束!")
        Client.GUI_Hall.Hall.Matching_Flag = False
    else:
        Client_Tcp_Main.send("Match".encode())

def Client_Send(self):
    message = self.Ui.lineEdit_Send.text()
    Client_Tcp_Main.send("Message".encode())
    Client_Tcp_Main.send(message.encode())

def Client_Quit():
    Client_Tcp_Main.send("Quit".encode())

def Client_Refuse(Matching_Master):
    Client_Tcp_Main.send("Refuse".encode())
    Client_Tcp_Main.send(Matching_Master.encode())

def Client_Accept(Matching_Master):
    Client_Tcp_Main.send("Accept".encode())
    Client_Tcp_Main.send(Matching_Master.encode())

def Client_Playing(accept_sender):
    Client_Tcp_Main.send("Playing".encode())
    Client_Tcp_Main.send(accept_sender.encode())




    















