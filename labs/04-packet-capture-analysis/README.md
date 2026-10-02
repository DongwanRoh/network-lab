# 🛠️ Lab 04. 패킷 캡처 및 헤더 분석 (Packet Sniffing & Analysis)

Scapy 라이브러리 또는 Raw Socket을 활용해 네트워크 인터페이스를 통과하는 패킷을 캡처하고, L2(Ethernet), L3(IP/ICMP), L4(TCP/UDP) 헤더를 바이트 단위로 뜯어봅니다.

---

## 🎯 학습 목표
1. **Raw Socket / Scapy 기초**: Promiscuous Mode 및 패킷 캡처 메커니즘
2. **패킷 헤더 바이트 언패킹(Unpacking)**:
   - Python `struct` 모듈을 이용한 바이너리 헤더 파싱
   - IP Version, IHL, Total Length, TTL, Protocol 번호 해석
3. **`ping` (ICMP Echo Request/Reply) 직접 구현**:
   - ICMP Checksum 계산 알고리즘 이해
   - RTT(Round Trip Time) 측정
