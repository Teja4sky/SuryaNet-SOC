import socket

server=socket.socket()

server.bind(("0.0.0.0",9999))

server.listen()

print("SOC Server running")

while True:

    client,addr=server.accept()

    data=client.recv(4096)

    print("Sensor:",addr,data.decode())
