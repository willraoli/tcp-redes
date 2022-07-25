import socket
import select

IP = socket.gethostname()
PORT = 1234
HEADER_SIZE = 10
CODIFICATION = 'utf-8'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

def receive_msg(client_socket):
  try:
    msg_header = client_socket.recv(HEADER_SIZE)

    if not len(msg_header):
      return False
    
    msg_length = int(msg_header.decode(CODIFICATION).strip())
    return {'header': msg_header, 'data': client_socket.recv(msg_length)}
  except:
    return False


while True:
  read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

  for notified_socket in read_sockets:
    if notified_socket == server_socket:
      client_socket, client_address = server_socket.accept()

      user = receive_msg(client_socket)

      if user is False:
        continue

      sockets_list.append(client_socket)
      clients[client_socket] = user

      print(f'Accepted new connection from {client_address[0]}:{client_address[1]} username: {user["data"].decode(CODIFICATION)}')

    else:
      msg = receive_msg(notified_socket)

      if msg is False:
        print(f'Closed connection from: {clients[notified_socket]["data"].decode(CODIFICATION)}')
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        continue

      user = clients[notified_socket]
      print(f'Received message from {user["data"].decode(CODIFICATION)}: {msg["data"].decode(CODIFICATION)}')

      for client_socket in clients:
        if client_socket != notified_socket:
          client_socket.send(user['header'] + user['data'] + msg['header'] + msg['data'])
      
  for notified_socket in exception_sockets:
    sockets_list.remove(notified_socket)
    del clients[notified_socket]
