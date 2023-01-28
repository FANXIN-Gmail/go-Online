# coding=utf-8
import Client.Client_Tcp_Main_Manage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class Register(QWidget):

    def __init__(self):
        super(Register, self).__init__()
        self.Ui = loadUi("../Ui/Register.ui", self)
        self.mouse_Flag = False
        self.mouse_Position = ""
        self.initUi(self.Ui)

    def initUi(self, ui):
        self.setWindowFlag(Qt.FramelessWindowHint)
        ui.pushButton_Return.clicked.connect(self.pushButton_Return_clicked)
        ui.pushButton_Submit.clicked.connect(self.pushButton_Submit_clicked)

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

    def pushButton_Return_clicked(self):
        self.close()

    def pushButton_Submit_clicked(self):
        if Client.Client_Tcp_Main_Manage.Client_Register(self.Ui):
            print("注册成功!")
        else:
            print("注册失败!")

    