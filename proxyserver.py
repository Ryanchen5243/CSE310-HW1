# CSE 310 Spring 2024
# Programming Assignment 1
# Part B - Web Proxy
# Ryan Chen
# SBU_ID: 113200236

from socket import *
PROXY_PORT = 8888
BUFFER_SIZE = 4096
HOST = 'localhost'

cache = {}

def handleClient(conn_sock):
  # read entire request
  request = ""
  while True:
    chunk = conn_sock.recv(BUFFER_SIZE).decode()
    request += chunk
    if "\r\n\r\n" in request: # end of request
      break
  request_url = request.split("\n")[0].split(" ")[1]

  # construct HTTP response to send back to requesting client

  if request_url in cache:
    # check modification date, fetch if new, otherwise retrieve resource from cache
    print("Requested url {} was found in cache...now retrieving...".format(request_url))
    # logic for fetching from cache
    cached_response = cache[request_url]

    conn_sock.sendall(cached_response.encode())

  else:
    # fetch resource from server using GET request
    try:
      # retrieve domain name
      domain_name = request_url.split('/')[1]
      # print("the domain name is ",domain_name)
      if (domain_name == ''):
        domain_name = "www.google.com" # default case
      print("the domain name is ",domain_name)

      # retrieve resource path
      resource_path = ""
      if len(request_url.split('/')) > 2:
        for path_el in request_url.split('/')[2:]:
          resource_path += "/" + path_el
      else:
        resource_path = "/"
      print("the retreived resource path is ", resource_path)
      # done domain name and resource path

      # send GET request to origin server
      clientSocket = socket(AF_INET, SOCK_STREAM)
      clientSocket.connect((domain_name,80))
      get_req_to_origin = f"GET {resource_path} HTTP/1.1\r\n" \
                    f"Host: {domain_name}\r\n" \
                    "Connection: keep-alive\r\n" \
                    "\r\n"

      clientSocket.sendall(get_req_to_origin.encode())
      print("Requested: {} {} .... fetching response from the origin server".format(domain_name,resource_path))

      origin_server_response = ""
      while True:
        data = clientSocket.recv(BUFFER_SIZE)
        if not data:
            break
        origin_server_response += data.decode()
      clientSocket.close()

      print("The origin server response is {}".format(origin_server_response))
      print("Now caching... {} -> origin server response".format(request_url))
      # cache origin server response
      cache[request_url] = origin_server_response
      
      # send response back to client
      conn_sock.sendall(origin_server_response.encode())

    except gaierror as e:
      # bad dns lookup (invalid domain name)
      pass


  # http_response = ""
  # response_content = ""
  # content_type = "text/html" # default to html

  # # add header lines
  # http_response += "HTTP/1.1 200 OK\r\n" # status line
  # http_response += f"Content-Type: {content_type}\r\n" # headers
  # http_response += "Content-Length: {}\r\n".format(len(response_content))
  # http_response += "\r\n"
  # conn_sock.sendall(http_response.encode())
  # # # send file content
  # conn_sock.sendall(response_content.encode())


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