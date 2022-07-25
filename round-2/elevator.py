import socket
import errno
import sys
import random
import time

IP = socket.gethostname()
PORT = 1234
BUFFER_SIZE = 16
CODIFICATION = 'utf-8'
HEADER_SIZE = 10
MAX_LEVEL = 20
ELEVATOR_STATUS = 0

# username = input('Username: ')
username = 'Elevador'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = username.encode(CODIFICATION)
username_header = f'{len(username):<{HEADER_SIZE}}'.encode(CODIFICATION)
client_socket.send(username_header + username)

def moveElevator():
  stops = random.randint(2,19)
  for i in range(1, MAX_LEVEL):
    if (i != stops):
      print("Subindo para o andar " + str(i))
      # msg = f'Andar {i}'.encode(CODIFICATION)
      # msg_header = f'{len(msg):<{HEADER_SIZE}}'.encode(CODIFICATION)
      # client_socket.send(msg_header + msg) # ainda n funciona
      time.sleep(1)
    else:
      print('Seu elevador está com problemas')
      print('Abrindo chat com um técnico')
      # notifyTechnician(1000)
      break

while True:
  if ELEVATOR_STATUS == 0:
    moveElevator()
    ELEVATOR_STATUS = 1
  msg = input('> ')
  
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

      # username_length = int(username_header.decode(CODIFICATION).strip())
      # username = client_socket.recv(username_length).decode(CODIFICATION)

      # msg_header = client_socket.recv(HEADER_SIZE)
      # msg_length = int(msg_header.decode(CODIFICATION).strip())
      # msg = client_socket.recv(msg_length).decode(CODIFICATION)

      # print(f'{username} > {msg}')

  except IOError as e:
    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
      print('Reading error: {}'.format(str(e)))
      sys.exit()
    continue

  except Exception as e:
    print(e)
    sys.exit()