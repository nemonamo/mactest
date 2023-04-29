import socket
import random


def request():
    beat = random.randrange(40, 140)
    step = random.randrange(2000, 6000)
    kcal = random.randrange(1000, 4000)

    result = str(beat)
    result += " "
    result += str(step)
    result += " "
    result += str(kcal)
    return result


HOST = '127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, 9001))
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
