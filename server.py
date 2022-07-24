from ast import Try
import socket
from _thread import *

if __name__ == '__main__':
  ip = '192.168.1.100'
  port = 5000
  clients = []	

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((ip, port))
  server.listen(1)

  def notifyTech(conn, string):
    for client in clients:
      if (client != client):
        try:
          client.send(bytes(string, 'utf-8'))
        except:
          print("não enviou")

  def newClient(conn, address):
    while True:
      string = client.recv(2048)
      string = string.decode('utf-8')
      if(string.find('NOK') or string.find('OK')):
        notifyTech(conn, string)
        aux = string[:6] + ' OK'
        conn.send(bytes(aux, 'utf-8'))

      # try:
      #   conn.send(bytes(string, 'utf-8'))
      # except:
      #   print("não conectou")

  while True:
    client, address = server.accept()
    clients.append(client)
    start_new_thread(newClient, (client, address))
    print('Client connected from:', address[0], ':', address[1])

