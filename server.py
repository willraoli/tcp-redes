import socket
from _thread import *

if __name__ == '__main__':
  ip = '0.0.0.0'
  port = 8000

  # TCP = SOCK_STREAM, UDP = SOCK_DGRAM
  # AF_INET = IPv4
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((ip, port))
  server.listen(5)

  def newClient(conn, address):
    while True:
      string = client.recv(2048)
      string = string.decode('utf-8')
      conn.send(bytes(string, 'utf-8'))
      
  while True:
    client, address = server.accept()
    start_new_thread(newClient, (client, address))
    print('Client connected from:', address[0], ':', address[1])

