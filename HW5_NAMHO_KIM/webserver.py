from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 80))

s.listen(10)

print('Server is running...')
while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')    

    try:
             path = req[0].split()[1]
    except IndexError:
            continue


    if path == '/index.html':
        with open('index.html', 'rb') as f:
             response = f.read()
        content_type = 'text/html'
        response_headers = 'HTTP/1.1 200 OK\nContent-Type: {}; charset=utf-8\n\n'.format(content_type).encode()
    elif path == '/iot.png':
        with open('iot.png', 'rb') as f:
            response = f.read()
        content_type = 'image/png'
        response_headers = 'HTTP/1.1 200 OK\nContent-Type: {}; charset=utf-8\n\n'.format(content_type).encode()
    elif path == '/favicon.ico':
        with open('favicon.ico', 'rb') as f:
            response = f.read()
        content_type = 'image/x-icon'
        response_headers = 'HTTP/1.1 200 OK\nContent-Type: {}; charset=utf-8\n\n'.format(content_type).encode()
    else:
        response = b'Not Found'
        content_type = 'text/plain'
        response_headers = 'HTTP/1.1 404 Not Found\nContent-Type: {}; charset=utf-8\n\n'.format(content_type).encode()



    
    c.sendall(response_headers + response)
    c.close()

