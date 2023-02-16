import socket

HOST=''
PORT=8000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    print(f"Server Listeining on Port {PORT}")

    while True:
        conn, addr= s.accept()

        with conn:
            print(f"Connect by address {addr}")

            data= conn.recv(1024)
            if data:
                response=b'HTTP/1.1 200 OK\nContent-Type: text/html\n\nSocket Only Webserver!!'
                conn.sendall(response)
            else:
                break