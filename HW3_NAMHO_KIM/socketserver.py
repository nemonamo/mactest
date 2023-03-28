
import socket
import struct
from http import client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))

s.listen(2)

while True:
    client, addr = s.accept()
    print('connection from', addr)
    # 클라이언트에게 인사 메시지 전송
    client.send(b'hello ' + addr[0].encode())
    # 학생의 이름 수신
    name = client.recv(1024).decode()
    print(name)
    # 학생의 학번 전송
    student_id = 20171510  # 학번 입력
    student_id_bytes = struct.pack('!i', student_id)  # big-endian으로 변환
    client.sendall(student_id_bytes)
    client.close()