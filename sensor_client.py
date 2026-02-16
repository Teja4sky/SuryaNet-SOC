import socket
from config import SERVER_IP,SERVER_PORT

def send(data):

    try:

        s=socket.socket()

        s.connect((SERVER_IP,SERVER_PORT))

        s.send(data.encode())

        s.close()

    except:
        pass
