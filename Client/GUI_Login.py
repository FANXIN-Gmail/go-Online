# coding=utf-8
import Client.Client_Tcp_Main_Manage
import Client.GUI_Register
import Client.GUI_Hall
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.Ui = loadUi("../Ui/Login.ui", self)
        self.init_ui(self.Ui)
        self.mouse_Flag = False
        self.mouse_Position = ""


    def init_ui(self, ui):
        self.setWindowFlag(Qt.FramelessWindowHint)
        ui.pushButton_Quit.clicked.connect(self.pushButton_Quit_clicked)
        ui.pushButton_Login.clicked.connect(self.pushButton_Login_clicked)
        ui.pushbutton_Register.clicked.connect(self.pushbutton_Register_clicked)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.mouse_Flag = True
            self.mouse_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if self.mouse_Flag:
            self.move(QMouseEvent.globalPos() - self.mouse_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_Flag = False

    def pushButton_Quit_clicked(self):
        Client.Client_Tcp_Main_Manage.Client_Quit()
        self.close()

    def pushButton_Login_clicked(self):
        if Client.Client_Tcp_Main_Manage.Client_Login(self.Ui):
            print("用户登陆成功!")
            self.close()
            hall = Client.GUI_Hall.Hall()
            hall.show()
        else:
            print("用户登陆失败!")

            self.Ui.lineEdit_ID.clear()
            self.Ui.lineEdit_Passworld.clear()

    @staticmethod
    def pushbutton_Register_clicked():
        register = Client.GUI_Register.Register()
        register.show()










