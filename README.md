CSE 310 Spring 2024
Programming Assignment 1
Ryan Chen
SBU_ID: 113200236

• Any external libraries used.
• Instructions on how to run your programs.
• Webpages that your code successfully works for.

Part A - Web Server
The directory features a small number of static resources, which are meant for the client to request for to test out the server. These resources includes:
- HTML page: HelloWorld.html
- Image files: cat1.jpg mario.png
- Plain text file: plain.txt

How to run program?
1) On your computer, open terminal and navigate to the project directory
2) Run the command python3 webserver.py to start the web server [the server will run on localhost on port 6789]
3) On the same computer open a browser such as google chrome and type http://localhost:6789/HelloWorld.html to access the html web page
4) You may replace the "HelloWorld.html" with any of the above resources to check them out directly (for example, http://localhost:6789/mario.png)
5) Any other resource will give 404 error as they are not in the server directory

For completeness sake, please check out the following urls
- http://localhost:6789/HelloWorld.html
- http://localhost:6789/cat1.jpg
- http://localhost:6789/mario.png
- http://localhost:6789/plain.txt
- http://localhost:6789/bamboozle.html

Part B - Web Proxy
The web proxy serves as a simple web server that includes a cache system and works with basic web pages.
The relevant file to test this is proxyserver.py
