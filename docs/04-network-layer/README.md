# 📚 04. 네트워크 계층 (Network Layer)

## 📌 다룰 프로토콜 & 주제
1. **IP (Internet Protocol)**
   - IPv4 헤더 필드 분석 (TTL, Protocol, Header Checksum, Fragmentation Flags 등)
   - IPv6 도입 배경 및 헤더 간소화 특징
2. **IP 주소 체계와 서브넷팅 (Subnetting)**
   - 클래스 기반 주소 지정(Classful) vs CIDR (Classless Inter-Domain Routing)
   - 서브넷 마스크, 네트워크 ID, 브로드캐스트 ID 계산 실습
3. **라우팅 (Routing)**
   - 정적 라우팅 vs 동적 라우팅
   - IGP (OSPF, RIP) vs EGP (BGP)
4. **ICMP & 보조 프로토콜**
   - ICMP Type/Code 메시지 (`Echo Request/Reply`, `Destination Unreachable`, `Time Exceeded`)
   - `ping`과 `traceroute`의 동작 메커니즘
5. **NAT (Network Address Translation)**
   - 사설 IP(Private IP)와 공인 IP(Public IP)
   - NAPT (포트 기반 주소 변환) 및 포트 포워딩
