import socket
import select
import errno
import sys

IP = socket.gethostname()
PORT = 1234
BUFFER_SIZE = 16
CODIFICATION = 'utf-8'
HEADER_SIZE = 10

username = 'Reader'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = username.encode(CODIFICATION)
username_header = f'{len(username):<{HEADER_SIZE}}'.encode(CODIFICATION)
client_socket.send(username_header + username)

while True:
  msg = ''
  
  if msg:
    msg = msg.encode(CODIFICATION)
    msg_header = f'{len(msg):<{HEADER_SIZE}}'.encode(CODIFICATION)
    client_socket.send(msg_header + msg)

  try:
    while True:
      username_header = client_socket.recv(HEADER_SIZE)
      if not len(username_header):
        print('Connection closed by the server')
        sys.exit()

      username_length = int(username_header.decode(CODIFICATION).strip())
      username = client_socket.recv(username_length).decode(CODIFICATION)

      msg_header = client_socket.recv(HEADER_SIZE)
      msg_length = int(msg_header.decode(CODIFICATION).strip())
      msg = client_socket.recv(msg_length).decode(CODIFICATION)

      print(f'{username} > {msg}')

  except IOError as e:
    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
      print('Reading error: {}'.format(str(e)))
      sys.exit()
    continue

  except Exception as e:
    print(e)
    sys.exit()