import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

def run_tcp_client():
    # 1. TCP 소켓 생성 (IPv4, SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print(f"[TCP Client] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        
        # 2. 서버에 연결 시도 (3-Way Handshake 시작: SYN -> SYN/ACK -> ACK)
        sock.connect((SERVER_HOST, SERVER_PORT))
        print("[TCP Client] Connected to server! Type messages to send (or 'exit' to quit).")
        
        while True:
            msg = input("You > ")
            if msg.lower() == "exit":
                print("[TCP Client] Closing connection...")
                break
            
            # 3. 데이터 송신
            sock.sendall(msg.encode("utf-8"))
            
            # 4. 서버로부터 에코 데이터 수신
            data = sock.recv(1024)
            print(f"Echo Server > {data.decode('utf-8')}")

if __name__ == "__main__":
    run_tcp_client()
