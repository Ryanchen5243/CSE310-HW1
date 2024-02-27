# CSE 310 Spring 2024
# Programming Assignment 1
# Part B - Web Proxy
# Ryan Chen
# SBU_ID: 113200236

from socket import *
PROXY_PORT = 8888
BUFFER_SIZE = 10
HOST = 'localhost'

cache = {}

def handleClient(conn_sock):
  request = ""
  while True:
    chunk = conn_sock.recv(BUFFER_SIZE).decode()
    request += chunk
    if "\r\n\r\n" in request: # end of request
      break
  request_line = request.split("\n")[0].split(" ")
  print("The data from socket is ",request_line)
  req_resource = request_line[1][1:]
  print("the requested resouce is ",req_resource)

  http_response = ""
  response_content = ""
  content_type = "text/html" # default to html

  if req_resource in cache:
    # retrieve resource from cache
    pass
  else:
    # fetch resource from server
    print("the conns ock sisi s,",conn_sock)
    pass

  # add header lines
  http_response += "HTTP/1.1 200 OK\r\n" # status line
  http_response += f"Content-Type: {content_type}\r\n" # headers
  http_response += "Content-Length: {}\r\n".format(len(response_content))
  http_response += "\r\n"
  conn_sock.sendall(http_response.encode())
  # # send file content
  conn_sock.sendall(response_content)



def main():
  proxySocket = socket(AF_INET,SOCK_STREAM)
  proxySocket.bind((HOST,PROXY_PORT))
  proxySocket.listen(1)
  print("The Proxy Server is ready to receive")
  while True:
    conn, addr = proxySocket.accept()
    print("Received connection from ",conn,addr)
    handleClient(conn)
    conn.close()

if __name__ == "__main__":
  main()