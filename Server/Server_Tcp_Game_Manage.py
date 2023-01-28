# coding=utf-8

def Submit(client):
    client.to_socket.send("Submit".encode())
    client.from_socket.send("Submit".encode())



