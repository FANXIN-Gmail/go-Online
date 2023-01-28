# coding=utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
import Client.Client_Tcp_Main_Manage
import Client.Client_Tcp_Main_Connection
import Client.Client_Tcp_Game_Manage
import Client.GUI_Invitation
import Client.GUI_Login
import Client.GUI_Game
import threading

class Signal_All(QObject):
    show_game_signal = pyqtSignal()
    show_invitation_signal = pyqtSignal()
    clear_textEdit_client_signal = pyqtSignal()

class Hall(QWidget):
    Matching_Flag = False
    Playing_Flag = False

    def __init__(self):
        super(Hall, self).__init__()

        self.Ui = loadUi("../Ui/Hall.ui", self)
        self.game = ""
        self.invitation = ""

        self.mouse_Flag = False
        self.mouse_Position = ""

        self.client_number = 0
        self.respond_number = 0
        self.invitation_number = 0

        self.Matching_Master = ""
        self.accept_sender = ""
        self.State = ""

        self.Signal = Signal_All()
        self.Signal.show_game_signal.connect(self.show_game)
        self.Signal.show_invitation_signal.connect(self.show_invitation)
        self.Signal.clear_textEdit_client_signal.connect(self.clear_textEdit_client)

        self.scrollArea_Chat = QScrollArea(self)
        self.scrollArea_Chat.setGeometry(0, 0, 400, 600)
        self.scrollArea_Chat.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_Chat.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_Chat.setFrameShape(QFrame.NoFrame)
        self.textEdit_Chat = QTextEdit(self.scrollArea_Chat)
        self.textEdit_Chat.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_Chat.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_Chat.setFrameShape(QFrame.NoFrame)
        self.textEdit_Chat.setGeometry(0, 0, 400, 600)
        self.textEdit_Chat.setStyleSheet("color: rgb(100, 100, 100)")
        self.textEdit_Chat.setReadOnly(True)
        self.scrollArea_Chat.setWidget(self.textEdit_Chat)

        self.initUi(self.Ui)

        try:
            tcp_main_connection = threading.Thread(target=Client.Client_Tcp_Main_Connection.tcp_main_connection_thread,
                                                   args=(self, ),
                                                   daemon=True)
            tcp_main_connection.start()
        except Exception as thread_tcp_main_connection_error:
            print(thread_tcp_main_connection_error)

        Client.Client_Tcp_Game_Manage.Tcp_game_Connection()

    def initUi(self, ui):
        self.setWindowFlag(Qt.FramelessWindowHint)
        ui.pushButton_Send.clicked.connect(self.pushButton_Send_clicked)
        ui.pushButton_Quit.clicked.connect(self.pushButton_Quit_clicked)
        ui.pushButton_Matching.clicked.connect(self.pushButton_Matching_clicked)


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

    def pushButton_Send_clicked(self):
        Client.Client_Tcp_Main_Manage.Client_Send(self)
        self.lineEdit_Send.clear()

    def pushButton_Quit_clicked(self):
        Client.Client_Tcp_Main_Manage.Client_Quit()
        Client.Client_Tcp_Game_Manage.Client_Quit()
        self.close()

    def pushButton_Matching_clicked(self):
        if Hall.Matching_Flag or Hall.Playing_Flag:
            pass
        else:
            print("Matchin...")
            Hall.Matching_Flag = True
            Client.Client_Tcp_Main_Manage.Client_Match(self)

    def clear_textEdit_client(self):
        self.textEdit_Client.clear()

    def show_invitation(self):
        self.invitation = Client.GUI_Invitation.Invitation(self.Matching_Master)
        self.invitation.show()

    def show_game(self):
        print("Show Chess")
        try:
            game = Client.GUI_Game.Game(self.State)
            game.show()
        except Exception as show_game_error:
            print(show_game_error)










