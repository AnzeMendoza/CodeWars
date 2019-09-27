import machine
import socket

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket() #declaro el socket
s.bind(addr) #
s.listen(1)

print('listening on', addr)

while True:
    client, address = s.accept()
    print('client connected from', address)
    client_file = client.makefile('rwb', 0)

    while True:
        line = client_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()