# coding=utf-8
import Server_Main
import Server_Class

def resister(client, dbconnection):
    client.Socket.send("Begin_Ok".encode())
    message = ""
    while True:
        message += client.Socket.recv(1024).decode()
        if message[-3:] == "END":
            break
    information_list = []
    information = ""
    for i in message:
        if i != "+":
            information += i
        else:
            information_list.append(information)
            information = ""
    cursor = dbconnection.cursor()
    sql = "INSERT INTO user(Mail, NickName, PassWord) VALUES ('%s','%s','%s')" % (information_list[0],
                                                                                  information_list[1],
                                                                                  information_list[3])
    try:
        cursor.execute(sql)
        dbconnection.commit()
        client.Socket.send("End_Ok".encode())
    except Exception as register_sql_execute:
        print(register_sql_execute)
        dbconnection.rollback()
        client.Socket.send("End_ERROR".encode())
    cursor.close()

def login(client, dbconnection):
    client.Socket.send("Begin_Ok".encode())
    message = ""
    while True:
        message += client.Socket.recv(2048).decode()
        if message[-3:] == "END":
            break
    information_list = []
    information = ""
    for i in message:
        if i != "+":
            information += i
        else:
            information_list.append(information)
            information = ""
    cursor = dbconnection.cursor()
    sql = "select * from user where Mail = '%s' and PassWord = '%s'" % (information_list[0], information_list[1])
    if cursor.execute(sql) == 0:
        client.Socket.send("End_Error".encode())
    else:
        client.Socket.send("End_Ok".encode())
        result = cursor.fetchall()
        user = Server_Class.User(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
        client.user = user
        Server_Main.Client_Online_List.append(client)

def Message(client):
    message = client.Socket.recv(2048).decode()
    for i in Server_Main.Client_Online_List:
        i.Socket.send("Message".encode())
        i.Socket.send((i.user.NickName + " : " + message).encode())

def Match(client):
    for i in Server_Main.Client_Online_List:
        if i.Socket == client.Socket:
            continue
        i.Socket.send("Match".encode())
        i.Socket.send((client.Address[0] + ":" + str(client.Address[1])).encode())

def Refuse(client):
    message_to = client.Socket.recv(2048).decode()
    address_list = []
    address = ""
    for i in message_to:
        if i == ":":
            address_list.append(address)
            address = ""
            continue
        else:
            address += i
    address_list.append(address)
    for j in Server_Main.Client_Online_List:
        if j.Address[0] == address_list[0] and str(j.Address[1]) == address_list[1]:
            j.Socket.send("Refuse".encode())

def Accept(client):
    message_to = client.Socket.recv(2048).decode()
    address_list = []
    address = ""
    for i in message_to:
        if i == ":":
            address_list.append(address)
            address = ""
            continue
        else:
            address += i
    address_list.append(address)
    for j in Server_Main.Client_Online_List:
        if j.Address[0] == address_list[0] and str(j.Address[1]) == address_list[1]:
            j.Socket.send("Accept".encode())
            j.Socket.send((client.Address[0] + ":" + str(client.Address[1])).encode())

def Playing(client):
    message_to = client.Socket.recv(2048).decode()
    address_list = []
    address = ""
    for i in message_to:
        if i == ":":
            address_list.append(address)
            address = ""
            continue
        else:
            address += i
    address_list.append(address)
    Bind(client.Address[0], address_list[0])
    for j in Server_Main.Client_Online_List:
        if j.Address[0] == address_list[0] and str(j.Address[1]) == address_list[1]:
            j.Socket.send("Playing".encode())

def Bind(player_A, player_B):
    player_AA = []
    player_BB = []

    for i in Server_Main.Player_Online_List:
        if i.from_address[0] == player_A:
            player_AA.append(i.from_socket)
            player_AA.append(i.from_address)
        else:
            pass
        if i.from_address[0] == player_B:
            player_BB.append(i.from_socket)
            player_BB.append(i.from_address)
        else:
            pass

    for j in Server_Main.Player_Online_List:
        if j.from_address[0] == player_A:
            j.to_socket = player_BB[0]
            j.to_address = player_BB[1]
            print(j.from_address, j.to_address)
        else:
            pass
        if j.from_address[0] == player_B:
            j.to_socket = player_AA[0]
            j.to_address = player_AA[1]
            print(j.from_address, j.to_address)
        else:
            pass



