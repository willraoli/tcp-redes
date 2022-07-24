import socket
import random
import time

MAX_LEVEL = 20

def notifyTechnician(id):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.connect((ip, port))

  server.send(bytes('[' + str(id) + '] NOK', 'utf-8'))
  buffer = server.recv(2048)
  buffer = buffer.decode('utf-8')
  if(buffer != '' or buffer != null):
    print(buffer)  
  else:
   print('vazio')
  server.close()
    


def moveElevator():
  stops = random.randint(2,19)
  for i in range(1, MAX_LEVEL):
    print("Subindo para o andar " + str(i))
    time.sleep(1)
    if (i == stops):
      print('Elevador está com problemas')
      notifyTechnician(1000)
      break

if __name__ == '__main__':
  ip = '192.168.1.100'
  port = 5000

  moveElevator()

  # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # server.connect((ip, port))

  # while True:
  #   try:
  #     # string = input('Manda a msg ae dudão\n')
      
  #     if string != 'quit':
  #       server.send(bytes(string, 'utf-8'))
  #       buffer = server.recv(2048)
  #       buffer = buffer.decode('utf-8')
  #       print('Recebido:', buffer)
  #     else:
  #       server.close()
  #       print('conexão com servidor fechada')
  #       break
  #   except Exception as e:
  #     print('zuou')
  #     print(e)
  #     break

  