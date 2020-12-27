# Team CrazyTrain🚄

- 진행기간: 2020년 12월 14일 ~ 2020년 12월 24일
<img width="933" alt="Screen Shot 2020-12-24 at 5 49 39 PM" src="https://user-images.githubusercontent.com/71719160/103166192-f509ff00-4862-11eb-8038-688e78bbf4f8.png">

## **🏠프로젝트 소개**

> 안녕하세요. 저희는 위코드 1차 프로젝트에서 '오늘의집'클론코딩을 하게된 폭주기관차🚄팀입니다. 
 오늘의집은 원스톱 인테리어 플랫폼으로써 누구나 자신의 공간을 만들어가는 문화가 퍼지길 희망하는 소셜커머스 사이트입니다. 커뮤니티와 스토어를 서로 연결시켜두었다는 점이 큰 특징으로, 커뮤니티에 올린 게시글에 제품들에 대한 정보를 바로 알 수 있고 스토어에서 구매할 수 있다는 특성이 있습니다 . 반대로 스토어에서 커뮤니티의 글을 반영해 해당 피드로 이동하는 것도 가능합니다.

## **🏠**프로젝트 시연영상

[https://www.youtube.com/watch?v=cCLuBCNrrnA&t=25s](https://www.youtube.com/watch?v=cCLuBCNrrnA&t=25s)

## **🏠** 프로젝트 참가자 (Front & Back)

![스크린샷 2020-12-27 12 21 59](https://user-images.githubusercontent.com/71719160/103166205-1bc83580-4863-11eb-99f7-0546712ea68b.png)

### 👍 **FrontEnd**

- 김성훈, 김영재, 하태현

### 👍 **BackEnd**

- 김민철(PM), 이수한, 석여주

## **🌹기술 스택🌹**

### **FrontEnd**

- HTML / CSS / JavaScript (ES6) / React (CRA 세팅) / Sass

### **BackEnd**

- Python / Django / CORS Header / Bcrypt / PyJWT / MySQL / AqeuryTool (데이터베이스 모델링)

### **협업 도구**

- Slack / Git + GitHub / [Trello](https://trello.com/b/m2hECHg6/%EC%98%A4%EB%8A%98%EC%9D%98-%EC%A7%91)를 이용, 일정관리 및 작업 현황 확인 / Postman (API 관리)

---

# ⭐️ **구현한 기능**

## 🌱 Frontend

### **회원가입 & 로그인 (SignUp & SignIn)**

- 회원 가입시 유효성 검사
- 약관 동의 체크 박스

### 네비게이션 바

- 커뮤니티 / 스토어 서브메뉴 구현
- 로그인시 회원정보가 표기되도록 로직 구현

### 커뮤니티 페이지

- 그리드 디스플레이를 이용, 카드 리스트 구현
- 각각의 카드를 컴포넌트 화
- 쿼리스트링을 이용한 필터 기능 구현
- 상세 페이지 상품 태그 기능 구현
- 상세 페이지 댓글 기능 구현

### 스토어 페이지

- 사이드 카테고리
- 슬라이드를 이용한 배너 구현
- 전체상품 리스트에 infinite scroll 적용
- 각각의 카드를 컴포넌트 화
- 필터 버튼
    - 각각의 필터 버튼을 컴포넌트화 하여 타입별 다른 인풋을 출력하도록 디자인
    - 필터 버튼 클릭시 태그 추가
- 가격 필터
    - 필터 선택시 가격 박스에 반영
- 상세페이지
    - 장바구니 상품 추가 기능

### **장바구니**

- 상품 정보 컴포넌트화
- 선택한 상품만 합계 금액에 반영
- 수량 옵션 변경시 Database에 실시간 반영

## 🌱 Backend

### 모델링 구축

<img width="816" alt="모델링 최종" src="https://user-images.githubusercontent.com/71719160/103166208-24b90700-4863-11eb-925c-1bcf72c19ba4.png">

### **회원가입 & 로그인 (SignUp & SignIn)**

- bcrypt를 사용한 암호화
- JWT 로그인 구현 및 @decorator를 이용해서 토큰 인증
- Email&닉네임 정규화를 통한 Validation적용

### **장바구니**

- 상품의 장바구니 등록 (개수 포함)
- 장바구니 내역 조회
- 장바구니 상품 수량 변경 및 가격반영(DB에 전부 반영되도록 설정)

### 스토어 페이지

- 카테고리-서브카테고리 사이드바 (카테고리를 반영하여 상품 나열)
- 상품 상세 페이지 (상품 정보: 가격, 사진, 옵션 )

### 커뮤니티 페이지

- 포스트 작성 API
- 포스트 리스트 API (다중 필터 적용 )
- 포스트 디테일 뷰 API

---

# 🏠후기

## 👩‍💻Frontend

- [김영재](https://velog.io/@kyj2471/%EA%B9%80%EC%98%81%EC%9E%AC-wecode-1%EB%8B%AC1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0%EB%A1%9D)
- 김성훈
- [하태현](https://velog.io/@kingth)

## 🧑‍💻 Backend

- 김민철
- 이수한
- [석여주](https://velog.io/@fhwmqkfl/%EC%9C%84%EC%BD%94%EB%93%9C-1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%98%A4%EB%8A%98%EC%9D%98%EC%A7%91-%ED%81%B4%EB%A1%A0%EC%BD%94%EB%94%A9-%ED%9B%84%EA%B8%B0)

---

# **레퍼런스**

- 이 프로젝트는 [오늘의 집](https://ohou.se/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
