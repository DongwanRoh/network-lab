# 🛠️ Lab 05. DNS 질의기 직접 만들기 (Custom DNS Client)

표준 라이브러리(`gethostbyname` 등)를 쓰지 않고, 순수 UDP 소켓으로 DNS 서버(예: `8.8.8.8`)에 DNS Query 바이너리 패킷을 직접 만들어 전송하고 응답 레코드를 파싱하는 `nslookup` / `dig` 클론을 만듭니다.

---

## 🎯 학습 목표
1. **DNS 패킷 구조 (RFC 1035)** 이해:
   - Header (Transaction ID, Flags, QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT)
   - Question Section (QNAME 라벨 인코딩, QTYPE, QCLASS)
   - Answer Section (Name 포인터 압축 기법, Type, TTL, RDATA)
2. **바이너리 프로토콜 직렬화 & 역직렬화(Serialization/Deserialization)** 실습
3. 도메인 네임 문자열의 DNS 포맷 변환 (예: `google.com` -> `\x06google\x03com\x00`)
