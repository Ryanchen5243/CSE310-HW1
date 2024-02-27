# CSE 310 Spring 2024 - Programming Assignment 1

## Name: Ryan Chen
## SBU_ID: 113200236

### Part A - Web Server

The directory features a small number of static resources meant for client testing. These resources include:

- **HTML page:** HelloWorld.html
- **Image files:** cat1.jpg, mario.png
- **Plain text file:** plain.txt

**How to run the program?**

1. On your computer, open the terminal and navigate to the project directory.
2. Run the command `python3 webserver.py` to start the web server (it will run on localhost on port 6789).
3. Open a browser (e.g., Google Chrome) on the same computer and type `http://localhost:6789/HelloWorld.html` to access the HTML web page.
4. Replace "HelloWorld.html" in the URL with any of the above resources to view them directly (e.g., `http://localhost:6789/mario.png`).
5. Accessing any other resource will result in a 404 error as they are not in the server directory.

**For completeness, check out the following URLs:**

- http://localhost:6789/HelloWorld.html
- http://localhost:6789/cat1.jpg
- http://localhost:6789/mario.png
- http://localhost:6789/plain.txt
- http://localhost:6789/bamboozle.html

### Part B - Web Proxy

The web proxy serves as a simple web server with a cache system for basic web pages. The relevant file to test this is `proxyserver.py`.

**How to run the program?**

1. On your computer, open the terminal and navigate to the project directory.
2. Run the command `python3 proxyserver.py` to start the web proxy (it will run on localhost on port 8888).
3. Open a browser (e.g., Google Chrome) on the same computer and access web pages such as:

- http://localhost:8888/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
- http://localhost:8888/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html
- http://localhost:8888/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
- http://localhost:8888/gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html

4. On the initial request from the client, it may take some time for the web proxy to fetch content from the origin server.
5. Subsequent requests (e.g., refreshing the page) will provide the content quickly.

The program also handles invalid domain names, so the following URL will result in a 502 Bad Gateway Error:
- http://localhost:8888/fopbar
