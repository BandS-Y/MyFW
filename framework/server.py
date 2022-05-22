import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8001)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    print('Server redy')
    client, address = server_socket.accept()
    print(f'Connection from address {address}')
    data = client.recv(1024).decode()
    print(f' receive data: {data}')
    client.sendall(b'Hello from server \n')
    print(f'Connections from {address} ', end='')
    client.close()
    print('closed')