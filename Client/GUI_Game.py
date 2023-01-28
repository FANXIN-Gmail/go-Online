# coding=utf-8
import Client.Client_Tcp_Game_Connection
import Client.Client_Tcp_Game_Manage
import Client.Client_Class
import Client.GUI_Hall
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class Game(QWidget):

    def __init__(self, State):
        super(Game, self).__init__()
        self.Ui = loadUi("../Ui/Game.ui", self)

        self.mouse_Flag = False
        self.mouse_Position = ""

        self.my_state = State
        self.Rob = ["Unknow", "Unknow"]

        self.black = QPixmap("../Images/Black.png")
        self.white = QPixmap("../Images/White.png")
        self.Unknow = QPixmap("")

        if self.my_state == "Black":
            self.your_state = "White"
            self.turn = True
            self.my_pixmap = self.black
            self.your_pixmap = self.white
        else:
            self.your_state="Black"
            self.turn = False
            self.my_pixmap = self.white
            self.your_pixmap=self.black

        self.chess_pieces_label = [[QLabel(self) for i in range(19)] for j in range(19)]

        self.chessBoard = Client.Client_Class.ChessBoard(self.my_state, self.your_state)

        try:
            self.tcp_game_connection = threading.Thread(
                target=Client.Client_Tcp_Game_Connection.tcp_game_connection_thread,
                args=(self,),
                daemon=True)
            self.tcp_game_connection.start()
        except Exception as thread_tcp_game_connection_error:
            print(thread_tcp_game_connection_error)

        self.setMouseTracking(True)

        self.init_chess_pieces_label()

        self.initUi()

    def initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def init_chess_pieces_label(self):
            x=40
            y=40
            for i in self.chess_pieces_label:
                for j in i:
                    j.setGeometry(x - 20, y - 20, 40, 40)
                    j.setVisible(True)
                    j.setScaledContents(True)
                    x+=40
                x=40
                y+=40

    def mousePressEvent(self, QMouse_Event):
        if QMouse_Event.button() == Qt.RightButton:
            self.mouse_Flag = True
            self.mouse_Position = QMouse_Event.globalPos() - self.pos()
            QMouse_Event.accept()
        if QMouse_Event.button() == Qt.LeftButton:
            index = self.chessBoard.transform(QMouse_Event.x(), QMouse_Event.y())
            if index[0] == "Outer" and index[1] == "Outer":
                if  950 < QMouse_Event.x() < 1000 and 760 < QMouse_Event.y() < 800:
                    Client.Client_Tcp_Game_Manage.Client_Submit()
            else:
                if self.turn:
                    self.check_begin(index[0], index[1])
                else:
                    pass

    def mouseMoveEvent(self, QMouse_Event):
        if self.mouse_Flag:
            self.move(QMouse_Event.globalPos() - self.mouse_Position)
            QMouse_Event.accept()

    def mouseReleaseEvent(self, QMouse_Event):
        self.mouse_Flag = False
        QMouse_Event.accept()

    def paintEvent(self, QPaint_Event):
        painter = QPainter(self)
        painter.fillRect(QRect(0, 0, 1000, 800), QColor(0, 0, 0, 55))
        self.draw_chessboard()
        QPaint_Event.ignore()

    def draw_chessboard(self):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.gray, 1, Qt.SolidLine))
        begin_x = 40
        begin_y = 40
        end_x = 760
        end_y = 40
        for i in range(19):
            painter.drawLine(begin_x, begin_y, end_x, end_y)
            begin_y += 40
            end_y += 40
        begin_x = 40
        begin_y = 40
        end_x = 40
        end_y = 760
        for i in range(19):
            painter.drawLine(begin_x, begin_y, end_x, end_y)
            begin_x += 40
            end_x += 40
        painter.setBrush(QBrush(Qt.gray))
        x = 160
        y = 160
        for i in range(3):
            for j in range(3):
                painter.drawEllipse(QPoint(x, y), 3, 3)
                x += 240
            x = 160
            y += 240
        painter.end()

    def check_begin(self, row, column, flag = 0):
        if row == self.Rob[0] and column == self.Rob[1]:
            return
        else:
            self.Rob=["Unknow", "Unknow"]
        if self.chessBoard.chessboard[row][column][1] == "Unknow":
            self.chessBoard.refresh_Search()
            if flag == 0:
                self.chessBoard.count_Self_Life(row, column, self.my_state)
            elif flag == 1:
                self.chessBoard.count_Self_Life(row, column, self.your_state)
            else:
                pass
            if self.chessBoard.Count_Self_Life > 0:
                if flag == 0:
                    self.fall_pieces(row, column)
                    self.check_1(row, column)
                    self.turn = False
                    Client.Client_Tcp_Game_Manage.Client_Fall(row ,column)
                elif flag == 1:
                    self.fall_pieces(row, column, Flag=1)
                    self.check_1(row, column, 1)
                    self.turn = True
                else:
                    pass
            else:
                if flag == 0:
                    self.fall_pieces(row, column, 1)
                    self.check_0(row, column)
                elif flag == 1:
                    self.fall_pieces(row, column, 1, Flag=1)
                    self.check_0(row, column, 1)
                else:
                    pass
        else:
            pass

    def check_1(self, row, column, flag = 0):
        my_state = ""
        your_state = ""
        if flag == 0:
            my_state = self.my_state
            your_state = self.your_state
        elif flag == 1:
            my_state = self.your_state
            your_state = self.my_state
        else:
            pass
        for i in range(4):
            new_row=row + self.chessBoard.Direction[i][0]
            new_column=column + self.chessBoard.Direction[i][1]
            if 0 <= new_row <= 18 and 0 <= new_column <= 18:
                state = self.chessBoard.chessboard[new_row][new_column][1]
                if state == "Unknow":
                    pass
                elif state == my_state:
                    pass
                else:
                    self.chessBoard.refresh_Search()
                    self.chessBoard.count_Self_Life(new_row, new_column, your_state)
                    if self.chessBoard.Count_Self_Life > 0:
                        pass
                    else:
                        self.kill_pieces()
            else:
                pass

    def check_0(self, row, column, flag = 0):
        my_state = ""
        your_state = ""
        rob = ""
        if flag == 0:
            my_state = self.my_state
            your_state = self.your_state
        elif flag == 1:
            my_state = self.your_state
            your_state = self.my_state
        else:
            pass
        for i in range(4):
            new_row=row + self.chessBoard.Direction[i][0]
            new_column=column + self.chessBoard.Direction[i][1]
            if 0 <= new_row <= 18 and 0 <= new_column <= 18:
                state = self.chessBoard.chessboard[new_row][new_column][1]
                if state == "Unknow":
                    pass
                elif state == my_state:
                    pass
                else:
                    self.chessBoard.refresh_Search()
                    self.chessBoard.count_Self_Life(new_row, new_column, your_state)
                    if self.chessBoard.Count_Self_Life > 0:
                        pass
                    else:
                        if len(self.chessBoard.Dead_Pieces) == 1:
                            if flag == 0:
                                self.kill_pieces()
                                rob = self.check_rob(row, column)
                            elif flag == 1:
                                self.kill_pieces()
                            else:
                                pass
                        else:
                            self.kill_pieces()
            else:
                pass
        self.chessBoard.refresh_Search()
        self.chessBoard.count_Self_Life(row, column, my_state)
        if self.chessBoard.Count_Self_Life > 0:
            if flag == 0:
                self.turn=False
                self.fall_pieces(row, column, 3)
                if rob == 0:
                    Client.Client_Tcp_Game_Manage.Client_Fall(row, column)
                else:
                    Client.Client_Tcp_Game_Manage.Client_Rob(rob[0][0], rob[0][1], row, column)
            elif flag == 1:
                self.turn=True
                self.fall_pieces(row, column, 3, 1)
            else:
                pass
        else:
            print("禁着点")
            if flag == 0:
                self.fall_pieces(row, column, 2)
            elif flag == 1:
                self.fall_pieces(row, column, 2, 1)
            else:
                pass

    def fall_pieces(self, row, column, flag = 0, Flag = 0):
        #flag == 0: 真落子
        #flag == 1: 假落子
        #flag == 2: 撤销假落子
        #flag == 3: 变真假落子
        pixmap = ""
        state = ""
        if Flag == 0:
            pixmap = self.my_pixmap
            state = self.my_state
        elif Flag == 1:
            pixmap = self.your_pixmap
            state = self.your_state
        if flag == 0:
            self.chess_pieces_label[row][column].setPixmap(pixmap)
            self.chessBoard.chessboard[row][column][1]=state
        elif flag == 1:
            self.chessBoard.chessboard[row][column][1]=state
        elif flag == 2:
            self.chessBoard.chessboard[row][column][1]="Unknow"
        elif flag == 3:
            self.chess_pieces_label[row][column].setPixmap(pixmap)
        else:
            pass

    def kill_pieces(self):
        for i in self.chessBoard.Dead_Pieces:
            self.chess_pieces_label[i[0]][i[1]].setPixmap(self.Unknow)
            self.chessBoard.chessboard[i[0]][i[1]][1] = "Unknow"

    def check_rob(self, row, column):
        dead_row = self.chessBoard.Dead_Pieces[0][0]
        dead_column = self.chessBoard.Dead_Pieces[0][1]
        rob = ""
        self.fall_pieces(dead_row, dead_column, 1, 1)
        for i in range(4):
            new_row=dead_row + self.chessBoard.Direction[i][0]
            new_column=dead_column + self.chessBoard.Direction[i][1]
            if 0 <= new_row <= 18 and 0 <= new_column <= 18:
                self.chessBoard.refresh_Search()
                self.chessBoard.count_Self_Life(new_row, new_column, self.my_state)
                if self.chessBoard.Count_Self_Life > 0:
                    pass
                else:
                    if len(self.chessBoard.Dead_Pieces) == 1:
                        if self.chessBoard.Dead_Pieces[0][0] == row and self.chessBoard.Dead_Pieces[0][1] == column:
                            rob = [[dead_row, dead_column], self.your_state]
                    else:
                        pass

        self.fall_pieces(dead_row, dead_column, 2)
        if rob == "":
            return 0
        else:
            return rob























