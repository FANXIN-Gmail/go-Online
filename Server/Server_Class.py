# coding=utf-8


class Client:

    def __init__(self, tcp_main_socket, tcp_main_address, udp_chat_address=(0, 0), udp_show_address=(0, 0)):
        self.Socket = tcp_main_socket
        self.Address = tcp_main_address
        self.user = ""

class User:

    def __init__(self, mail, nick_name, password, rank, win, fail, value = 0):
        self.Mail = mail
        self.NickName = nick_name
        self.PassWord = password
        self.rank = rank
        self.Win = win
        self.Fail = fail
        self.Value = value

class Game_Room:

    def __init__(self, tcp_game_from_socket, tcp_game_from_address, tcp_game_to_socket = "", tcp_game_to_address = ""):
        self.from_socket = tcp_game_from_socket
        self.from_address = tcp_game_from_address
        self.to_socket = tcp_game_to_socket
        self.to_address = tcp_game_to_address












