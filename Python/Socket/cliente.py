import socket

my_socket = socket.socket()
my_socket.connect(('localhost', 8000))

my_socket.send('hola te saludo desde el cliente')
respuesta = my_socket.recv(1024)

print(respuesta)
my_socket.close()
