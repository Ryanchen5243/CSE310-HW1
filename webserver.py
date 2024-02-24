from socket import *
serverPort = 12000

def handleRequest(connSock):
   http_content = """HTTP/1.1 200 OK\r
Content-Type: text/html\r
\r
<h1>Hello</h1>"""
   connSock.send(http_content.encode())

def main():
   serverSocket = socket(AF_INET,SOCK_STREAM)
   serverSocket.bind(('',serverPort))
   serverSocket.listen(1)
   print ("The server is ready to receive")
   while True:
      connectionSocket, addr = serverSocket.accept()
      print(f"Received connection from {addr}")
      # sentence = connectionSocket.recv(1024).decode()
      # capitalizedSentence = sentence.upper()
      handleRequest(connectionSocket)
      connectionSocket.close()

if __name__ == "__main__":
   main()