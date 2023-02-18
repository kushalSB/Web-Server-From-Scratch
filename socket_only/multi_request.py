import socket

HOST=''
PORT=8000

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
                    print(f"Servicing a GET Request at /{request_path}")
                    response=f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n You requested {request_path} and we will give it to you'
                    conn.sendall(response.encode())
                elif request_type=="POST":
                    print(f"Servicing a POST Request at / {request_path}")
                    response= f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n You send {request_path} and we will save it'
                    conn.sendall(response.encode())
                
            else:
                break

