import socket
import json


def status_door():
    host = "192.168.1.240"
    port = 3000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    # GET CURRENT STATUS
    s.sendall(b'{"config":"GET_DOOR_STATUS","msgId":5,"dir":"p2d"}')
    data = s.recv(1024)
    my_json = json.loads(data.decode('utf8').replace("'", '"'))
    print('Status\n', json.dumps(my_json, indent=2))
    # GET SETTINGS
    s.sendall(b'{"config":"GET_SETTINGS","msgId":6,"dir":"p2d"}')
    data = s.recv(1024)
    my_json = json.loads(data.decode('utf8').replace("'", '"'))
    print('Config\n', json.dumps(my_json, indent=2))
    # HW INFO
    s.sendall(b'{"config":"GET_HW_INFO","msgId":7,"dir":"p2d"}')
    data = s.recv(1024)
    my_json = json.loads(data.decode('utf8').replace("'", '"'))
    print('HW INFO\n', json.dumps(my_json, indent=2))
    s.close()
    
status_door()