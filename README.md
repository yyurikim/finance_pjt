## 금융 관통 프로젝트
## Mingle(밍글)

## 목차
1. [프로젝트 배경 및 서비스 소개](#프로젝트-배경-및-서비스-소개)
2. [팀원 정보 및 업무 분담 내역](#팀원-정보-및-업무-분담-내역)
3. [데이터베이스 모델링 및 컴포넌트 구조](#데이터베이스-모델링-및-컴포넌트-구조)
4. [개발 일지 및 이슈 관리](#개발-일지-및-이슈-관리)
5. [서비스 소개](#서비스-소개)
6. [소감](#소감)

<br>

## 프로젝트 배경 및 서비스 소개
### 금융 상품 추천 서비스 Mingle 🙌
![mingle__1_-removebg-preview](https://github.com/yyurikim/finance_pjt/assets/156268560/aaec753b-3d46-437d-b3a2-0dde11f8356c)

'재테크'가 처음인 사회 초년생들에게 든든한 입문서이자 개론이 될 수 있는 서비스를 만들고자 했습니다.
돈을 모으는 것보다 '소비하는 것'에 더 익숙한 사회 초년생들에게 먼저 '소비 성향 테스트'를 통해 자신이 어떻게 돈관리를 해 왔는지 파악할 수 있도록 하였고, 그 결과를 기반으로 개개인에게 맞는 예적금 상품 추천과 앞으로의 재테크를 위한 포트폴리오 구성 조언까지 제공하며 서비스를 발전시켰습니다.

또한 Mingle이라는 이름처럼, 함께 사용하는 다른 유저들과 함께 소비 경험을 공유하고 서로의 제태크 전략을 배울 수 있는 커뮤니티를 통해 금융 습관을 이해 및 개선할 수 있도록 다양한 콘텐츠를 제공하는 종합 금융 플랫폼이 되고자 합니다.

<br>


## 팀원 정보 및 업무 분담 내역

### 🤼‍♀️ 팀원
| 이름  | 역할 및 구현 기능 |
|-------|-------|
| 김유리 | 기획, 환율 계산기 및 게시판 기능 구현, 추천 알고리즘 설계|
| 문자영 | 기획, 은행 찾기 및 예적금 조회 기능 구현, 소비 성향 조사 구현 |

<br>

### 🕕 개발 기간

> 24.05.08(WED) ~ 24.05.23(THU)

<br>

### ⚙ 개발 환경

### 사용 언어

> - python
> - javascript

<br>

### 주요 Libraries 및 Framework

> - Vue.js 3.4.21
> - Vue Router 4.3.0
> - Pinia 2.1.7
> - Vuetify 3.6.6

<br>

### 🧷 협업 tool

> - Notion
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/035b0fe0-f031-45eb-80fa-770494cce4df.png" width="600"/>

- 노션 내 보드 활용해 작업 현황 파악

<br>
<br>

## 데이터베이스 모델링 및 컴포넌트 구조

<img src="https://github.com/yyurikim/finance_pjt/assets/156268560/5ff97c85-fd52-44af-9a00-fe62f03df8a7.png" width="600"/>

## API 명세서

> 클릭 시 확대 가능
> 
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/4597fba0-eea9-428d-a42d-907f100114f3.png" height="400"/>

## 개발 일지 및 이슈 관리

### 🏋️‍♀️ 개발 목표
- [x] 환율 API를 활용한 환율 계산기
- [x] 예적금 API를 활용한 예적금 비교 페이지
- [x] kakao API를 이용한 지도
- [x] 사용자의 소비 습관 파악을 위한 소비 성향 테스트
- [x] 소비 성향을 기반으로 한 예적금 추천 알고리즘

<br>

### 🤔 개발 일지

| 날짜 | 김유리 | 문자영 |
| --- | --- | --- |
| ~05/12 | 서비스 구상 및 기획 | 서비스 구상 및 기획 |
| 05/13 | 깃 레포지토리 생성 및 프로젝트 기본 구성, ERD 작성 | 깃 레포지토리 생성 및 프로젝트 기본 구성, ERD 작성 |
| 05/14 | 환율 API DB 저장, 환율 계산기 구현 | 인증(로그인, 로그아웃, 비밀번호 변경) 페이지 |
| 05/15 | 양방향 환율 계산 기능 구현 | kakao API를 통해 지도 및 위치 기반 은행 찾기 |
| 05/16 | 게시판 모델 작성, 게시글 목록 조회 기능 구현 | 회원 탈퇴, 토큰 활용 인증 |
| 05/17 | 게시판 CRUD 기능 기본 구현 | 비밀번호 변경 기능 보완, 예적금 목록 불러오기 |
| 05/18 | 게시판 CRUD 기능 보완, 댓글 기능 구현 | 지도 기능(현재 위치, 검색) 추가 |
| 05/19 | 게시판 게시글, 댓글 기능 완료, 소비게시판 좋아요 기능 구현 | 회원 정보 수정, 소비 성향 검사 기능 |
| 05/20 | 유저 인증 기반 게시판 조회 기능 구현, 예적금 추천 알고리즘 설계 | 예적금 좋아요 기능 및 디자인, 메인 페이지 구성 |
| 05/21 | 소비 성향 검사 기반 예적금 추천 알고리즘 구현, 프로필 페이지 구성 | 소비 성향 검사 화면 구성, 예적금 가입, 금액 계산 및 상품 검색 기능 |
| 05/22 | 프로필 페이지 내 사용자 사진, 추천 상품, 가입 상품 조회 구현 | 프로필 수정 기능, 메인 페이지 디자인 및 소비 성향 검사 결과 화면 |
| 05/23 | 전반적인 디자인 및 기능 보완 | 전반적인 디자인 및 기능 보완 |

<br>

### 🎧 이슈 관리

| 날짜       | 이슈                                                       | 해결 방법        | 해결 여부            |
|------------|------------------------------------------------------------------|-------------|-----------------|
| 2024-05-18 | 게시판 수정/삭제 기능 - 게시글을 작성한 사용자에게만 수정, 삭제 버튼을 보여주는 기능을 구현에 어려움을 겪음 | 로그인 시 LocalStorage에 토큰과 함께 유저 아이디(중복불가) 저장, 게시글 작성자 아이디와 현재 로그인 유저 아이디를 비교하여 동일할 시에만 수정, 삭제 버튼 출력 | ✔|
| 2024-05-19 | 게시판 좋아요(사세요/사지 마세요) 기능 - DB에 저장은 되지만 새로고침 시 좋아요 수 조회가 되지 않음 | 처음 게시글 디테일 페이지에 들어왔을 때 get 요청을 보내 좋아요 수 조회, 그 이후 사용자가 좋아요 버튼을 눌러 post 요청이 있을 때마다 get요청을 보내 좋아요 수 갱신| ✔ | 
| 2024-05-20 | 예적금 좋아요 기능이 화면에 지속적으로 출력되지 않고 새로고침 후에 적용되어 어려움을 겪음 | 좋아요 상태를 확인할 수 있는 변수를 js 파일 내 만들고, 좋아요 상태를 true/false로 나타내 LocalStorage에 지속적으로 좋아요 상태를 저장 | ✔ |
| 2024-05-21 | 프로필 페이지 사용자 프로필 사진 출력 기능 - DB media 파일에 저장되어있는 사용자가 업로드한 프로필 사진이 출력되지 않음 | 이미지 태그의 src 값을 변경, 절대경로화하여 출력 | ✔ |   

<br>

## 서비스 소개

### 1) 메인 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/abfb7d8b-7794-488b-bd8a-af6c83ff2cce.png" width="600"/>

- 로그인 전/후 헤더 구성 변화
- Carousel : 은행 페이지 바로가기
<br>

  
### 2) 예적금 비교 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/bc26624f-fd51-4948-ba51-c26350616a00.png" width="600"/>
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/4bf8466b-9368-41de-842e-756ffe2e4dab.png" width="600"/>

- 예적금 금리 조회
- 모달창 통해 금리 옵션 확인 및 확장 기능 통해 상세 정보 확인
- 예적금 / 단복리 별 만기액 계산 기능

<br>

### 3) 지도 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/b1af0e7c-91f5-4672-a473-c67eb9044194.png" width="600"/>
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/95f41314-7fbc-4b05-badf-e8b25312946c.png" width="600"/>

- 현재 위치 설정 및 이동 시 현재 시점 고정
- 근처 은행 검색
- 지도 확대/축소

<br>

### 4) 커뮤니티 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/156268560/f97a0c5f-2563-43ac-a33a-1880f9d24ac6" width="600"/>
<img src="https://github.com/yyurikim/finance_pjt/assets/156268560/0e3852b0-ec10-4b2d-8dce-50545a42d5ac" width="600"/>

- 자유게시판, 소비게시판, 7일 소비습관 챌린지 게시판에서 글(이미지 포함), 댓글 작성 가능
- 사세요 / 사지 마세요 버튼(좋아요 기능과 유사)으로 사용자 참여 유도
- 로그인 한 사용자만 게시글 및 댓글 작성 가능, 게시글 및 댓글 작성자만 수정 및 삭제 가능

<br>

5) 환율 계산 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/156268560/d8d2f1fd-6ac3-4666-8483-b466b74e4757" width="600"/>

- 원화에서 다른 통화로, 혹은 다른 통화에서 원화로 양방향 계산 구현
- 환율 정보는 실시간 반영, 만약 영업일이 아니거나 오전 10시 이전일 경우 이전 영업일 환율 데이터 활용
- 사용자가 선택한 통화와 원화 간 환율 그래프 제공

<br>

6) 소비 성향 테스트 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/152594481/3ab24036-321a-430d-b1a8-0f803713e7ce.png" width="600"/>

- router 사용해 소비 성향 테스트 구현 및 DB 저장
- 테스트 결과 통해 예적금 상품 추천

<br>

7) 프로필 페이지
<img src="https://github.com/yyurikim/finance_pjt/assets/156268560/81d6e7f0-7f8c-4afa-87bd-ed08f5d6eed1" width="600"/>

- 고객 프로필 사진 및 정보 제공
- 고객 소비 성향에 따른 맞춤 예적금 상품 추천 및 추천에 대한 설명
- 고객이 가입한 상품, 관심 있는 상품 조회

<br>

...

## 소감
🌴김유리

약 5개월 간 배워왔던 내용들을 하나로 연결해 볼 수 있었던 기회였습니다. 기능 별로 구현하며 처음에는 back와 front를 연결하는 과정에서 많은 에러와 어려움을 만나기도 했지만, 이를 해결해 나가는 과정에서 서비스를 어떻게 구현해 나가야 할지에 대해 조금씩 알아갈 수 있었습니다. 개념을 배우는 것도 중요하지만, 실제로 프로젝트를 통해 적용시켜 나가는 것도 중요함을 느꼈습니다. 

프로젝트를 진행하며 어려움이 있을 때마다 '할 수 있다!'고 이야기해준 세계 최고 페어에게 감사합니다🥰 


🎧문자영

배운 내용을 토대로 관통 프로젝트에 녹여가며 부족한 부분을 다시 한 번 점검할 수 있는 기회가 되어 좋았습니다. 백과 프론트를 다 경험해보고자 기능 별로 업무를 분담하게 되었는데, djnago를 통해 vue로 데이터를 불러오는 과정에서 model과 serializer의 역할의 중요성을 다시금 느낄 수 있었습니다. 

첫 프로젝트라 아쉬움이 많이 남지만, 앞으로의 프로젝트에서 더 좋은 역량을 발휘할 수 있는 밑거름이 된 것 같습니다. 최고의 페어와 함께 할 수 있어 즐거웠던 프로젝트였습니다! 😊

...
