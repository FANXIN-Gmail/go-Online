# coding=utf-8
import Server.Server_Tcp_Main_Listening
import Server.Server_Tcp_Game_Listening
import threading
import pymysql
import socket

# 8888 Tcp_Main
# 9999 Tcp_Game
# 8800 Udp_Chat
# 9900 Udp_Show

#402433422@qq.com
#373128165@qq.com
#875665483@qq.com

DbConnection = pymysql.connect(host="localhost", port=3306, user="root", password="580231", db="go-online",
                               charset="utf8")
Client_Online_List = []
Player_Online_List = []

Tcp_Main_Address = (socket.gethostbyname(socket.gethostname()), 8888)
Tcp_Game_Address = (socket.gethostbyname(socket.gethostname()), 9999)

if __name__ == '__main__':
    Server_Tcp_Main_Listing = threading.Thread(target=Server.Server_Tcp_Main_Listening.listening,
                                            args=(Tcp_Main_Address, ))
    Server_Tcp_Main_Listing.start()

    Server_Tcp_Game_Listing = threading.Thread(target=Server.Server_Tcp_Game_Listening.listening,
                                               args=(Tcp_Game_Address, ))
    Server_Tcp_Game_Listing.start()



















    

    



