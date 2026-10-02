import socket

HOST = "127.0.0.1"  # 루프백(로컬호스트) 주소
PORT = 8080         # 임의의 비특권 포트 (1024 이상)

def run_tcp_server():
    # 1. TCP 소켓 생성 (IPv4, SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        # 포트 재사용 옵션 설정 (서버 재시작 시 Address already in use 방지)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # 2. IP 및 포트 바인딩
        server_sock.bind((HOST, PORT))
        
        # 3. 연결 수신 대기 (Backlog queue 크기 설정)
        server_sock.listen(5)
        print(f"[TCP Server] Listening on {HOST}:{PORT}...")
        
        while True:
            # 4. 클라이언트 연결 수락 (블로킹: 연결 올 때까지 대기)
            # 3-Way Handshake가 완료되면 새 소켓(client_sock)과 주소 반환
            client_sock, client_addr = server_sock.accept()
            print(f"[TCP Server] Connection accepted from {client_addr}")
            
            with client_sock:
                while True:
                    # 5. 데이터 수신 (최대 1024 바이트)
                    data = client_sock.recv(1024)
                    if not data:
                        print(f"[TCP Server] Client {client_addr} disconnected.")
                        break
                    
                    message = data.decode("utf-8")
                    print(f"[TCP Server] Received from {client_addr}: {message.strip()}")
                    
                    # 6. 에코 (수신한 데이터를 그대로 전송)
                    client_sock.sendall(data)

if __name__ == "__main__":
    run_tcp_server()
