import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', int(sys.argv[1])))
sock.listen(5)

try:
    while True:
        conn, info = sock.accept()

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)

        conn.close()
except KeyboardInterrupt:
    sock.close()
