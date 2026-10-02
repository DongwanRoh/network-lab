# 🛠️ Lab 02. 다중 접속 채팅 서버 (Multi-Client Chat Server)

기본 블로킹 소켓의 한계(한 번에 1개의 클라이언트만 처리 가능)를 극복하고, 여러 클라이언트가 동시에 접속하여 대화할 수 있는 채팅 서버를 구현합니다.

---

## 🎯 학습 목표
1. **동시성 모델(Concurrency Models)** 이해:
   - **멀티스레딩(Multi-Threading)**: 클라이언트 연결마다 별도 스레드 할당
   - **I/O Multiplexing (`select`, `epoll`, `kqueue`)**: 단일 스레드로 수많은 소켓 이벤트 감지
   - **비동기 I/O (`asyncio`)**: 이벤트 루프 기반 비차단 통신
2. 브로드캐스팅(Broadcasting) 및 동기화/락(Locking) 기법
3. 클라이언트 비정상 종료 처리 및 소켓 리소스 정리

---

## 📂 실습 과제
- `python/threading_chat_server.py`: 스레드 기반 브로드캐스트 채팅 서버
- `python/asyncio_chat_server.py`: `asyncio` 기반 고성능 채팅 서버
- `python/chat_client.py`: 실시간 메시지 송수신 클라이언트
