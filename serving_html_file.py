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
                if request_type=="GET" and request_path=="":
                    with open("./dummy_files/index.html","r",encoding="utf-8") as file:
                        html_content= file.read()                    
                    html_bytes=html_content.encode()
                    response=b'HTTP/1.1 200 OK\nContent-Type: text/html\n\n ' + html_bytes
                    conn.sendall(response)
            else:
                break