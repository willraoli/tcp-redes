import socket

if __name__ == '__main__':
  ip = '0.0.0.0'
  port = 8000

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.connect((ip, port))

  while True:
    string = input('Manda a msg ae dudão\n')
    server.send(bytes(string, 'utf-8'))
    buffer = server.recv(1024)
    buffer = buffer.decode('utf-8')

    print('Recebido:', buffer)