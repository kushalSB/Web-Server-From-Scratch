import json
import socket

HOST=''
PORT=8000
SEARCH_LIST={
    "Kushal":"Yeah he is a Admin",
    "Rupesh":"Yeah he is a bitch",
    "Key":"Oh i cant give you key now can I",
    "Apasara":"Hahahahaha....Cough Cough"
}


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    print(f"Listeing on Port {PORT}")
    
    while True:
        conn, addr = s.accept()

        with conn:

            data=conn.recv(1024)

            if data:
                data_str= data.decode()
                request_type=data_str.split(' ')[0]
                request_path=data_str.split('/')[1].split(" ")[0]
                if request_type=="GET":
                    if request_path == "":
                        # Send the HTML file
                        with open("./dummy_files/api/index.html", "r", encoding="utf-8") as file:
                            html_content = file.read()

                        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                        response = response_header.encode() + html_content.encode()

                        conn.sendall(response)
                    elif request_path == "main.css":
                        # Send the CSS file
                        with open("./dummy_files/api/main.css", "rb") as file:
                            css_content = file.read()

                        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"
                        response = response_header.encode() + css_content

                        conn.sendall(response)
                    elif request_path == "main.js":
                        # Send the JS file
                        with open("./dummy_files/api/main.js", "rb") as file:
                            js_content = file.read()

                        response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/javascript\r\n\r\n"
                        response = response_header.encode() + js_content

                        conn.sendall(response)

                if request_type=="POST":
                    if request_path=="api":
                        
                        

                        search_querry=json.loads(data_str.split("\n")[-1])['searchQuerry']
                        try:
                            if SEARCH_LIST[search_querry]:
                                response_data = {"data":SEARCH_LIST[search_querry]}
                        except KeyError:
                            response_data= {"data":"No such item found"}
                        
                        response_header="HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
                        response=response_header.encode() +json.dumps(response_data).encode()
                        conn.send(response)

                        


            else:
                break