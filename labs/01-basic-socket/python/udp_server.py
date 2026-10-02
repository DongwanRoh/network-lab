import socket

HOST = "127.0.0.1"
PORT = 8081

def run_udp_server():
    # 1. UDP 소켓 생성 (IPv4, SOCK_DGRAM)
    # TCP와 달리 listen()이나 accept() 과정이 필요 없음 (Connectionless)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
        # 2. IP 및 포트 바인딩
        server_sock.bind((HOST, PORT))
        print(f"[UDP Server] Listening for datagrams on {HOST}:{PORT}...")
        
        while True:
            # 3. 데이터 및 발신자 주소 수신 (recvfrom 사용)
            data, client_addr = server_sock.recvfrom(1024)
            message = data.decode("utf-8")
            print(f"[UDP Server] Received from {client_addr}: {message.strip()}")
            
            # 4. 수신자 주소로 바로 데이터 송신 (sendto 사용)
            server_sock.sendto(data, client_addr)

if __name__ == "__main__":
    run_udp_server()
