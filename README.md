# This Project is to create a Web-Server

## What is a Web Server?

    The Basic Idea is that it is just a program that listeins to requests incoming from the internet and sends response back to them.

## What we will be doing?

### First Basic_server File will do the following

    - We will use python to create our own basic webserver
    - We will use http.server and socketserver modules for this
    - We will then define a port number and create a handler class that inherits from http.server.SimpleHTTPRequestHandler class
    - This class will have a do_GET() function which will have the response
    - Then we will create a TCPserver instance with the Handler and start the server

### socket_only File

    - This file is also a basic webserver
    - We try to create this using socket module instead of http.server module
    - Here we use a Socket Object that use IPv4 and TCP connection
    - We bind the socket object to the desired HOST and PORT
    - the socket object then listeins for any request
    - When a request is actually send we create a new socket object conn and a tuple addr which stores client ip and port
    - Now we read request data sent by user in a single chunk, not exceding 1024 bytes
    - We then return the reponse to the client using the client socket conn

### multi_request File

    - In this file we recieve multiple request and send different response
    - Here we used the socket only example
    - We here decode the data byte file and extract, two key fields from it
    - the path
    - the request type
    - now we can send response accordingly

### Responding with HTML file

    - in the file serving_html_file.py we send different html files for different requests
    - to send an html file, just attach the byte encoded html file to reponse and send it

### Responding with Multiple files

    - here we send html,js and css file
    - to do so, one must send each files seperately i.e if i want to send main.js file i send it when path /main.js is requested...
    - i can request this by just putting src="localhost:8000/main.js" and the file will be loaded

Now we have completed the basics
We can right now send files that we want
Let us now build api

### Building Api

    - So, now we create api that seraches a querry and return a data.. the code is self explanatory
    - We need Post request, jsonify the data in back end and send response by checking the data in request
    - We also need to write a js script to request the data

### Now lets start some real projects... lets build a group chat application

- First We need to make login sytem
- We need to make a common room where everyone can chat

### Next up is using flask
