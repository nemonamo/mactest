import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
sock.sendall(b'Namho Kim')

student_id_bytes = sock.recv(4)
student_id = struct.unpack('!i', student_id_bytes)[0] # big-endian으로 변환
print(student_id)

sock.close()