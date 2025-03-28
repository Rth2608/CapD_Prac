LLM 기반 뉴스 요약 & 검색 서비스 구현현

--- 현재 기능 ---
사용자 (웹)
  ↓↑ (Axios + React + Tailwind)
프론트엔드 (Vite + React + TypeScript)
  ↓↑ HTTP API 호출
백엔드 (FastAPI)
  ├─ PostgreSQL        → 뉴스 원문, 요약 저장
  ├─ Qdrant            → 뉴스 임베딩 벡터 저장 및 검색
  └─ OpenAI API        → 뉴스 본문 요약 생성

  
--- 목표 기능 ---
사용자 → (URL 입력) → FastAPI (/news)
            ↓
    뉴스 웹사이트 크롤링
            ↓
      title + content 추출
            ↓
     → OpenAI 요약 생성
     → PostgreSQL 저장
     → Qdrant 임베딩 저장


    
# 가상환경 (CapD)
python -m venv CapD
.\CapD\Scripts\activate
pip install -r requirements.txt

# FastAPI 백엔드

/news/ : 뉴스 저장 + 요약 생성

/search/?q=... : 유사 뉴스 요약 검색

# React 프론트엔드
/ 뉴스 입력 화면, /search 검색어 입력 → 요약 결과 표시

# 기타	
Axios로 API 연동, Tailwind로 UI 구성, Qdrant + OpenAI + DB 연동

# 추천 개발 순서
다음 단계 추천
🔐 로그인(JWT or Firebase)

📄 뉴스 크롤링 자동화

🧠 LLM 기반 Q&A

💾 사용자별 뉴스 저장

 추천 다음 단계
✅ 사용자 로그인 (Firebase or FastAPI JWT)

✅ 뉴스 작성/검색시 로딩 UI 추가

✅ 뉴스에 좋아요, 북마크 기능 추가

✅ 관리자용 대시보드 or 크롤링 자동화

✅ 자동 테스트 도입 (pytest, React Testing Library)

---
cd backend
uvicorn app.main:app --reload

http://localhost:8000
---
cd frontend
npm run dev
http://localhost:5173/
---
docker-compose down
docker-compose up --build