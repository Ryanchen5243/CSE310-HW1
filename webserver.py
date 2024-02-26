from socket import *
import os
serverPort = 6789
BUFFER_SIZE = 4096

def handleRequest(connSock):
   # should we handle requests in chunks?
   request = connSock.recv(BUFFER_SIZE)

   requested_file = request.decode().split("\n")[0].split(" ")[1][1:]
   # print("Requested File",requested_file)
   http_response = ""
   if os.path.isfile(os.path.join(os.getcwd(),requested_file)): # if file exists
      with open(os.path.join(os.getcwd(),requested_file),"rb") as html_file:
         html_content = html_file.read()
         # print(html_content)
         # add header lines
         http_response += "HTTP/1.1 200 OK\r\n" # status line
         http_response += "Content-Type: text/html\r\n" # headers
         http_response += "Content-Length: {}\r\n".format(len(html_content))
         http_response += "\r\n"
         connSock.sendall(http_response.encode())

         # send file content
         connSock.sendall(html_content)
   else:
      html_content = b"<h1>404 Error Not Found</h1>"
      http_response += "HTTP/1.1 404 Not Found\r\n" # status line
      http_response += "Content-Type: text/html\r\n" # headers
      http_response += "Content-Length: {}\r\n".format(len(html_content))
      http_response += "\r\n"
      connSock.sendall(http_response.encode())
      connSock.sendall(html_content)
   connSock.close()


def main():
   serverSocket = socket(AF_INET,SOCK_STREAM)
   serverSocket.bind(('',serverPort))
   serverSocket.listen(1)
   print ("The server is ready to receive")
   while True:
      connSock, addr = serverSocket.accept()
      print(f"Received connection from {addr}")
      # print("the connection socekt is ",connSock)
      handleRequest(connSock)

if __name__ == "__main__":
   main()