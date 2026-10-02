# 📚 05. 데이터 링크 계층 (Data Link Layer)

## 📌 다룰 프로토콜 & 주제
1. **이더넷 (Ethernet) & MAC 주소**
   - MAC 주소의 구조 (OUI + UAA/LAA)
   - 이더넷 프레임 구조 (Preamble, SFD, 목적지/출발지 MAC, EtherType, Payload, FCS)
2. **ARP (Address Resolution Protocol)**
   - IP 주소를 MAC 주소로 변환하는 ARP Request(브로드캐스트) & Reply(유니캐스트)
   - ARP Table(캐시)과 ARP Spoofing 취약점
3. **네트워크 장비**
   - 허브(L1) vs 스위치(L2) vs 라우터(L3)
   - 충돌 도메인(Collision Domain)과 브로드캐스트 도메인(Broadcast Domain)
   - 스위칭 방식: Store-and-Forward, Cut-Through
