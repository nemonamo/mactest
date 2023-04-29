import socket
import random


def request():
    temp = random.randrange(0, 40)
    humi = random.randrange(0, 100)
    illum = random.randrange(70, 150)

    result = str(temp)
    result += " "
    result += str(humi)
    result += " "
    result += str(illum)
    return result


HOST = '127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, 9000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            expression = data.decode("utf-8")
            if expression == "quit":
                break
            if expression == "Request":
                result = request()
                conn.sendall(str(result).encode("utf-8"))
