import socket

my_socket = socket.socket()
my_socket.bind(('localhost', 8000))
my_socket.listen(5)

while True:
    conexion, addres = my_socket.accept()
    print("nueva conexion establecida con la direccion %s", addres)

    conexion.send('Hola te saludo desde el servidor')
    conexion.close()

    