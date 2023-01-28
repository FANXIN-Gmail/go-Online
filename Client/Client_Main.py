# coding=utf-8
import sys
import Client.GUI_Login
import Client.Client_Tcp_Main_Manage
import Client.Client_Tcp_Game_Manage
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    Go_online = QApplication(sys.argv)

    login = Client.GUI_Login.Login()
    login.show()

    Client.Client_Tcp_Main_Manage.Tcp_Main_Connection()


    Signal = Go_online.exec_()

    if Signal == 0:
        print("主程序退出信号: ", Signal)
    else:
        print("主程序退出信号: ", Signal)

    sys.exit(Signal)

    



























