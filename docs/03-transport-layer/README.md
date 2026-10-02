# 📚 03. 전송 계층 (Transport Layer)

## 📌 다룰 프로토콜 & 주제
1. **TCP (Transmission Control Protocol)**
   - 신뢰성 보장 원리: 시퀀스 번호(Seq Num), 확인 응답(ACK Num), 재전송(Retransmission)
   - 연결 설정 및 해제:
     - 3-Way Handshake (SYN, SYN-ACK, ACK)
     - 4-Way Handshake (FIN, ACK, FIN, ACK) 및 `TIME_WAIT` 상태
   - 흐름 제어 (Flow Control): 슬라이딩 윈도우 (Sliding Window), 수신 버퍼
   - 혼잡 제어 (Congestion Control): AIMD, Slow Start, Congestion Avoidance, Fast Recovery
2. **UDP (User Datagram Protocol)**
   - 비연결형, 비신뢰성, 체크섬(Checksum)을 통한 최소한의 오류 검사
   - 실시간 스트리밍, 게임, DNS, QUIC 등에서 UDP가 선호되는 이유
3. **포트 번호와 소켓 다중화 (Multiplexing & Demultiplexing)**
   - Well-known (0-1023), Registered (1024-49151), Dynamic/Private (49152-65535)
