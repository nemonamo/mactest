import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))

s.listen(2)

while True:
    client, addr = s.accept()
    print('connection from', addr)
    client.send(b'hello ' + addr[0].encode())
    name = client.recv(1024).decode()
    print(name)
    student_id = 20171510  
    student_id_bytes = student_id.to_bytes(4,'big')
    
    client.sendall(student_id_bytes)
    client.close()