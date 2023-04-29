import socket
import time
HOST = '127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.connect((HOST, 9000))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
        s2.connect((HOST, 9001))
        while True:
            server_choice = input("1번 서버와 2번 서버 중 어떤 서버에 연결하시겠습니까? (1 or 2) quit를 입력하면 종료됩니다.")

            if server_choice == "1":
                expression = "Request"
                s1.sendall(expression.encode("utf-8"))
                data = s1.recv(1024)
                result = data.decode("utf-8")
                temp, humid, illum = result.split()
                with open('data.txt', 'a') as f:
                    f.write(
                        f"{time.strftime('%c', time.localtime(time.time()))}: Device1: Temp={temp}, Humid={humid}, Illum={illum}\n")
                print("결과: ", result)
            elif server_choice == "2":
                expression = "Request"
                s2.sendall(expression.encode("utf-8"))
                data = s2.recv(1024)
                result = data.decode("utf-8")
                beat, step, kcal = result.split()
                with open('data.txt', 'a') as f:
                    f.write(
                        f"{time.strftime('%c', time.localtime(time.time()))}: Device2: Heartbeat={beat}, Steps={step}, kcal={kcal}\n")
                print("결과: ", result)
            elif server_choice == "quit":
                s1.close()
                s2.close()
                exit()
            else:
                print("잘못된 입력입니다.")
