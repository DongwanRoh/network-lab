# 🌐 Network Lab (`network-lab`)

> **이론으로 깊게 이해하고, 코드로 직접 구현해보는 컴퓨터 네트워크 & 통신 프로토콜 실습 저장소**

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/DongwanRoh/network-lab/pulls)

---

## 🎯 목표 (Goals)

1. **이론 체계화**: OSI 7 계층 및 TCP/IP 4 계층 모델의 핵심 개념과 동작 원리를 시각화와 함께 정리합니다.
2. **프로토콜 직접 구현**: 추상적인 네트워크 지식을 소켓 프로그래밍과 커스텀 프로토콜 파서/서버를 통해 직접 코드로 구현합니다.
3. **패킷 레벨 분석**: Wireshark, tcpdump, Raw Socket 등을 활용해 실제 네트워크 상에서 오가는 패킷의 헤더와 흐름을 뜯어봅니다.

---

## 🗂️ 프로젝트 구조 (Directory Structure)

```text
network-lab/
├── docs/                           # 📚 컴퓨터 네트워크 이론 및 프로토콜 정리
│   ├── 01-network-basics/          # 네트워크 기본기 (OSI 7계층, TCP/IP 모델, 패킷 교환)
│   ├── 02-application-layer/       # 응용 계층 (HTTP/1.1, HTTP/2, HTTP/3, WebSocket, DNS, TLS/SSL)
│   ├── 03-transport-layer/         # 전송 계층 (TCP, UDP, 3/4-Way Handshake, 흐름/혼잡제어)
│   ├── 04-network-layer/           # 네트워크 계층 (IP 주소 체계, 서브넷팅, 라우팅, ICMP, NAT)
│   └── 05-data-link-layer/         # 데이터 링크 계층 (이더넷, MAC 주소, ARP, CSMA/CD)
│
└── labs/                           # 🛠️ 단계별 프로토콜 & 소켓 실습 프로젝트
    ├── 01-basic-socket/            # TCP / UDP 기본 에코(Echo) 서버 & 클라이언트
    ├── 02-multi-client-chat/       # 멀티스레드 / I/O Multiplexing 기반 채팅 서버
    ├── 03-custom-http-server/      # 소켓 기반 경량 HTTP/1.1 서버 직접 만들기
    ├── 04-packet-capture-analysis/ # 패킷 스니퍼 및 패킷 헤더 파싱 실습
    └── 05-dns-lookup-tool/         # UDP 기반 커스텀 DNS Query 질의기 구현
```

---

## 🗺️ 로드맵 & 학습 체크리스트 (Roadmap)

### 1. 전송 계층 & 소켓 프로그래밍 (Transport Layer)
- [ ] 소켓(Socket) 통신 기본 원리 이해
- [ ] TCP vs UDP 동작 방식 비교 및 특징 정리
- [ ] TCP 3-Way / 4-Way Handshake 및 상태 전이도(State Transition)
- [ ] TCP 흐름 제어 (Sliding Window) & 혼잡 제어 (Slow Start, Fast Retransmit)
- [ ] **[Lab 01]** TCP & UDP Echo Server/Client 구현
- [ ] **[Lab 02]** 멀티스레드/비동기 다중 접속 채팅 서버 구현

### 2. 응용 계층 프로토콜 (Application Layer)
- [ ] HTTP/1.1 동작 원리 (Keep-Alive, Pipelining, Request/Response 구조)
- [ ] HTTP/2 (Multiplexing, Header Compression) vs HTTP/3 (QUIC/UDP)
- [ ] HTTPS와 TLS 1.3 Handshake 암호화 과정
- [ ] WebSocket 실시간 양방향 통신 원리
- [ ] DNS(Domain Name System) 계층 구조 및 질의 과정 (Recursive vs Iterative)
- [ ] **[Lab 03]** 소켓 위에서 동작하는 Simple HTTP Server 구현
- [ ] **[Lab 05]** DNS 요청 패킷을 조립하고 응답을 파싱하는 DNS 클라이언트 구현

### 3. 네트워크 계층 & 라우팅 (Network Layer)
- [ ] IPv4 헤더 구조 및 IPv6 비교
- [ ] 서브넷 마스크(Subnet Mask)와 CIDR 표기법 계산
- [ ] 라우팅 알고리즘 (Distance Vector, Link State) 및 프로토콜 (OSPF, BGP)
- [ ] ICMP 프로토콜과 `ping` / `traceroute` 동작 원리
- [ ] NAT (Network Address Translation) & 포트 포워딩
- [ ] **[Lab 04]** Raw Socket / Scapy를 이용한 ICMP 패킷 송수신 (`ping` 클론)

### 4. 데이터 링크 & 물리 계층 (Data Link & Physical Layer)
- [ ] MAC 주소와 이더넷 프레임 구조
- [ ] ARP(Address Resolution Protocol) 동작 과정 및 ARP Spoofing 원리
- [ ] 스위치(Switch)와 허브(Hub)의 차이, 충돌 도메인(Collision Domain)

---

## 🚀 빠른 시작 (Getting Started)

원하는 실습 디렉토리로 이동하여 실습별 README 가이드를 확인하세요.

```bash
# 저장소 클론
git clone https://github.com/DongwanRoh/network-lab.git
cd network-lab

# 예: 01번 소켓 실습 폴더로 이동
cd labs/01-basic-socket
```

---

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
