# CSE 310 Spring 2024
# Programming Assignment 1
# Part A - Web Server
# Ryan Chen
# SBU_ID: 113200236

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

      with open(os.path.join(os.getcwd(),requested_file),"rb") as f:
         content = f.read()

      content_type = "text/html" # default to html
      # get file extension
      file_extension = requested_file.split(".")[-1].lower()
      if file_extension == "jpg" or file_extension == "jpeg":
         content_type = "image/jpeg"
      elif file_extension == "png":
         content_type = "image/png"
      elif file_extension == "txt":
         content_type = "text/plain"

      # add header lines
      http_response += "HTTP/1.1 200 OK\r\n" # status line
      http_response += f"Content-Type: {content_type}\r\n" # headers
      http_response += "Content-Length: {}\r\n".format(len(content))
      http_response += "\r\n"
      connSock.sendall(http_response.encode())

      # send file content
      connSock.sendall(content)
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
   serverSocket.bind(('localhost',serverPort))
   serverSocket.listen(1)
   print ("The server is ready to receive")
   while True:
      connSock, addr = serverSocket.accept()
      print(f"Received connection from {addr}")
      # print("the connection socekt is ",connSock)
      handleRequest(connSock)

if __name__ == "__main__":
   main()