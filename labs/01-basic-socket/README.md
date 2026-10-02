# 🛠️ Lab 01. 기본 소켓 통신 (Basic Socket Programming)

소켓(Socket) API를 사용하여 기본적인 **TCP** 및 **UDP** 에코(Echo) 서버와 클라이언트를 구현하고, 두 프로토콜의 통신 흐름 차이를 직접 확인합니다.

---

## 🎯 학습 목표
1. 소켓 통신의 기본 수명 주기(Lifecycle) 이해
   - TCP: `socket()` -> `bind()` -> `listen()` -> `accept()` -> `recv()`/`send()` -> `close()`
   - UDP: `socket()` -> `bind()` -> `recvfrom()`/`sendto()` -> `close()`
2. TCP의 연결 지향적(Connection-oriented) 특성과 UDP의 비연결형(Connectionless) 특성 비교
3. Wireshark 패킷 캡처를 통해 3-Way Handshake 및 데이터 전송 패킷 분석

---

## 📂 파일 구성
- `python/tcp_server.py`: TCP 에코 서버
- `python/tcp_client.py`: TCP 에코 클라이언트
- `python/udp_server.py`: UDP 에코 서버
- `python/udp_client.py`: UDP 에코 클라이언트

---

## 🚀 실행 방법 (Python 기준)

### 1. TCP 에코 서버 & 클라이언트 실행
```bash
# 터미널 1 (서버 실행)
python python/tcp_server.py

# 터미널 2 (클라이언트 실행)
python python/tcp_client.py
```

### 2. UDP 에코 서버 & 클라이언트 실행
```bash
# 터미널 1 (서버 실행)
python python/udp_server.py

# 터미널 2 (클라이언트 실행)
python python/udp_client.py
```
