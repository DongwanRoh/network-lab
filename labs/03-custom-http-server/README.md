# 🛠️ Lab 03. 소켓으로 만드는 커스텀 HTTP/1.1 서버

프레임워크(Express, Flask, FastHTTP 등) 없이, **순수 TCP 소켓**만으로 HTTP/1.1 프로토콜의 명세(RFC 7230~7235)를 직접 파싱하고 응답하는 경량 웹 서버를 만듭니다.

---

## 🎯 학습 목표
1. **HTTP Request 파싱**:
   - Request Line (`METHOD`, `PATH`, `HTTP-Version`)
   - Header 파싱 (`Key: Value`)
   - Body 읽기 (`Content-Length` 기반)
2. **HTTP Response 생성**:
   - Status Line (`HTTP/1.1 200 OK`, `404 Not Found` 등)
   - Headers (`Content-Type`, `Content-Length`, `Connection: close/keep-alive`)
   - Payload (HTML 문자열 또는 정적 파일 전송)
3. 브라우저에서 `http://localhost:8080` 접속하여 HTML/CSS 렌더링 확인

---

## 📂 실습 과제
- `python/http_server.py`: 기본 정적 파일 서빙 및 REST-like 응답 HTTP 서버
