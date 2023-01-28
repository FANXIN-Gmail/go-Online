# coding=utf-8
import Client.Client_Tcp_Main_Manage
import Client.GUI_Hall
import Client.GUI_Game
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class Invitation(QWidget):

    def __init__(self, Matching_Master):
        super(Invitation, self).__init__()
        self.Ui = loadUi("../Ui/Invitation.ui", self)
        self.mouse_Flag = False
        self.mouse_Position = ""
        self.Matching_Master = Matching_Master
        self.initUi()
        self.setMouseTracking(True)

    def initUi(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.Ui.pushButton_Accept.clicked.connect(self.pushButton_Accept_clicked)
        self.Ui.pushButton_Refuse.clicked.connect(self.pushButton_Refuse_clicked)



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

    def pushButton_Accept_clicked(self):
        Client.Client_Tcp_Main_Manage.Client_Accept(self.Matching_Master)
        Client.GUI_Hall.Hall.Matching_Flag = False
        self.close()

    def pushButton_Refuse_clicked(self):
        Client.Client_Tcp_Main_Manage.Client_Refuse(self.Matching_Master, )
        Client.GUI_Hall.Hall.Matching_Flag = False
        self.close()

