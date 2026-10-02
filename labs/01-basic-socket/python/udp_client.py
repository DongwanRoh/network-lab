import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8081

def run_udp_client():
    # 1. UDP 소켓 생성 (IPv4, SOCK_DGRAM)
    # connect() 호출 없이도 바로 데이터 전송 가능
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        print(f"[UDP Client] Target server {SERVER_HOST}:{SERVER_PORT}")
        print("Type messages to send (or 'exit' to quit).")
        
        while True:
            msg = input("You > ")
            if msg.lower() == "exit":
                break
            
            # 2. 서버 주소를 지정하여 데이터그램 전송
            sock.sendto(msg.encode("utf-8"), (SERVER_HOST, SERVER_PORT))
            
            # 3. 서버로부터 응답 수신
            data, server_addr = sock.recvfrom(1024)
            print(f"Echo Server ({server_addr}) > {data.decode('utf-8')}")

if __name__ == "__main__":
    run_udp_client()
