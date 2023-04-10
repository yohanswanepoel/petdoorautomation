import socket

@service
def open_door():
    host = "192.168.1.240"
    port = 3000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'{"cmd":"OPEN","msgId":799,"dir":"p2d"}')
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))