# ![logo](README.assets/navlogo.png) 산책 메이트

<img src="README.assets/logo.png" alt="logo" style="zoom:67%;" />

## 링크

[<img src="https://allvectorlogo.com/img/2021/12/github-logo-vector.png" alt="github" style="zoom: 25%;" />](https://github.com/kimbap918/sanme_proj)





## 멤버

[![image-20221121173712473](README.assets/image-20221121173712473.png)](https://github.com/kimbap918/sanme_proj/graphs/contributors)

+ 최준혁 https://github.com/kimbap918
+ 간정진 https://github.com/JeongJinGan
+ 김다솔 https://github.com/solightnsalt
+ 신우철 https://github.com/woocheolll
+ 이제준 https://github.com/jejoonlee


### 역할 분담

#### Front-end

+ 김다솔 



#### Back-end

+ 이제준 
+ 신우철 
+ 간정진 
+ 최준혁 





## 프로젝트 개요

### 목적

+ 웹 프레임워크 Django와 HTML / CSS / JavaScript를 활용한 콘텐츠 기반 커뮤니티 웹 플랫폼 개발



### 프로젝트 기간

+ 2022.11.10(목) ~ 2022.11.21(월)



### 주제

근처의 **산책 메이트**를 찾는 웹 서비스 (친구 말고 산책 메이트 👩‍❤️‍👨)





## 사용 기술

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![jquery](https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)  

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![bootstrap](https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

![git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white) ![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)





## 호스팅

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) 





## 주요 기능

### 추천 유저 

1. 가입 시 작성한 mbti를 반영한 추천 유저를 보여줍니다. 
2. 산책 매너 점수가 높은 순으로 3명의 유저를 보여줍니다.



### 전국 공원 정보

1. 전국 도시 공원 정보 표준 데이터 정보를 사용하여 전국의 공원을 조회할 수 있습니다.
2. 내 현재 위치 기반으로 공원 거리를 계산하여 가까운 공원 순으로 나열합니다.



### 산책 메이트 찾기

1. 글쓰기 버튼을 누르면 지도 페이지로 이동하여 근처의 원하는 공원을 선택할 수 있습니다.
2. 공원 선택 후 원하는 날짜와 시간, 인원 등의 정보를 포함한 글을 작성합니다. 
3. 참여를 원하는 사용자는 댓글로 참여 의사를 표시합니다.
4. 작성자는 댓글을 작성한 사용자 중 원하는 사용자를 산책에 참여시킬 수 있습니다.



### 유저

1. 가입은 프로그래스바를 사용하여 가입 진행 정도를 알아볼 수 있습니다.
2. 원하는 유저를 팔로우, 차단 할 수 있습니다.
3. 유저 간 평가를 당근마켓 온도점수를 차용해 보여줍니다.





## 화면 구성

<img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white" align="left">





## 참고 자료

- 참고 사이트

  [WIPPY : 위피 - 동네 친구가 필요할 때](https://www.wippy.io/)

- 데이터

  [전국도시공원정보표준데이터](https://www.data.go.kr/data/15012890/standard.do)

  [오픈API](https://www.vworld.kr/dev/v4dv_2ddataguide2_s002.do?svcIde=uq162)

  [Daum 우편번호 서비스](https://postcode.map.daum.net/guide#usage)

- ERD

  [산메](https://www.erdcloud.com/d/5bSqa7ABTAapJgmkm)




## DB 모델링
![1](https://user-images.githubusercontent.com/75712723/203453936-4e07d889-7681-4302-9d45-3d2533ec2b5c.png)





## 기능 소개
+ 해당 서비스를 사용을 하기 위해서는 기본적으로 로그인을 해야 서비스 이용이 가능합니다.


![0](https://user-images.githubusercontent.com/75712723/203454406-a5dcb373-2d72-4dd4-bea8-0e88974b9583.png)


+ 회원가입 할 때에는 필요한 정보가 여러가지로 있기때문에 사용자의 편의를 위해 페이지를 넘기면서 이용자 정보를 입력합니다.


![2](https://user-images.githubusercontent.com/75712723/203453949-784fb821-6848-4c7c-aa74-45c31028cb03.png)


- 메인 페이지 기능
    - 검색 기능
    - 추천 기능
        - 유저의 MBTI와 잘 맞는 MBTI들을 모아서, 랜덤으로 돌려 추천 메이트를 보여줍니다.
        - 그리고 유저 온도가 높은 사람들 위주로 추천 리스트를 보여줍니다.


![3](https://user-images.githubusercontent.com/75712723/203453958-2a4de647-42b7-4dee-b149-5eb81c6d615b.png)


- 공원 선택
    - 공원 검색
        - 공원 이름 또는 주소를 위주로 검색을 할 수 있습니다. (비동기 처리)
        - 내 위치를 기준으로 제일 가까운 공원 순서대로 검색 결과가 나옵니다.
    - 현재 위치 추적
        - 내 위치를 누르는 순간 반경 5km 내에 있는 공원들의 마커가 찍힙니다.
    - 공원 마커
        - 공원 마커를 누르면, 공원 이름, 주소 그리고 내 위치부터의 거리가 나옵니다.
        - 산책하기 버튼을 클릭하면 산책할 메이트를 구하기 위한 글을 쓰는 페이지로 이동하게 됩니다.
        


![4](https://user-images.githubusercontent.com/75712723/203453971-d8737df2-4aa2-4bd1-b6e7-5691012fe3c9.png)


- 게시글 
    - 게시글 작성
        - 지도에 만날 장소의 마커를 표시하고 장소, 날짜, 시간, 애완동물 유/무, 참여자의 수, 내용을 작성합니다. 
    - 게시글 목록
        - 작성된 게시글은 게시판에 리스트의 형태로 표시됩니다.
    
![Untitled](https://user-images.githubusercontent.com/75712723/203455414-00e1a512-65b9-427f-8b0d-f88e14d37283.png)




+ 고객지원 페이지에서는 해당 사이트에서 자주 묻는 질문을 확인할 수 있습니다.


![5](https://user-images.githubusercontent.com/75712723/203453972-b5aa46e1-fcf0-40ef-9033-aab3eeaaaef4.png)


+ 회원정보 페이지에서는 회원가입시 작성한 ID, 닉네임, 사는지역, MBTI 등을 확인할 수 있으며 수정 및 회원탈퇴가 가능합니다.
- 회원정보 
    - 정보 수정페이지 이동
        - 작성한 개인정보를 수정하는 페이지로 이동합니다.
    - 탈퇴하기
        - 회원을 탈퇴할 수 있습니다. 탈퇴 시 정보는 삭제되며, 산책 메이트의 기능을 사용할 수 없습니다.
    - 차단목록
        - 내가 차단한 유저의 목록을 확인할 수 있습니다.


![6](https://user-images.githubusercontent.com/75712723/203453977-7ce59b3a-01a3-474f-8a6a-597099a7633b.png)


- 회원정보 수정하기
    - 정보 수정
        - 작성한 개인정보를 수정할 수 있습니다. MBTI, 유저 프로필, 주소등을 수정할 수 있습니다.

![7](https://user-images.githubusercontent.com/75712723/203453987-eaf2943a-5560-4a08-9196-4f63020cb24d.png)


- 회원 상세정보
    - 팔로우
        - 마음에 드는 유저를 팔로우할 수 있습니다. 팔로우된 유저는 매너온도가 상승합니다.
    - 차단
        - 마음에 들지않는 유저를 차단할 수 있습니다. 차단된 유저는 매너온도가 하락합니다.
    - 차단 취소
        - 차단을 취소합니다. 취소 시 매너온도는 다시 상승합니다.        

![8](https://user-images.githubusercontent.com/75712723/203454004-66f89b8a-cb3e-4940-94ae-848a8cef3241.png)




## 프로젝트 후기 ✏️

- 김다솔
    
    CSS가 어색해서 원하는대로 화면 구성이 잘 되지 않았고, 자바스크립트랑 연결하는 것도 어려워서 하나하나 하는데 오래 걸린게 너무 많았습니다. 그래도 좋은 팀원들 만나서 마지막까지 웃으면서 할 수 있었던 것 같아요. 
    
- 간정진
    
    개인적으로 아이디어 제공이나, 직접 코드로 구현하는데 부족한 점이 있었지만 좋은 팀원분들을 만나 잘 마무리 할 수 있었습니다.
    
    첫번째 세미 프로젝트보다 기간이 길어진만큼 전보다 나은 프로젝트를 보여주기 위해 많은 노력하는 모습이 빛이 났습니다. 
    
- 신우철
    
    2주간 다들 고생 많으셨습니다.  9 to 6 지만 다들 새벽까지 너무 열심히 해주셔서 감사했습니다.
    
    새로운 기능들을 도전하다 하려고 하던 기능들을 잘 못한 부분이 아쉬웠지만 그래도 많이 배워가는 2주 였던거 같습니다. 
    
- 이제준
    
    새로운 기능을 많이 구현 할 수 있는 세미 프로젝트였다. 특히 비동기를 하면서, JavaScript를 혼자 많이 배운 것 같다. 
    
    이번 프로젝트를 통해 파이썬도 중요하지만 JavaScript도 매우 중요하다는 것을 느꼈다.
    
    팀원 분들도, 결과적으로는 매끄럽지 못 했지만 그래도 처음에 소통 도 잘 되었던 것 같다. 덕분에 재미있게 프로젝트를 할 수 있었다
    
- 최준혁
    
    2주간 9 to 6로, 때로는 새벽까지 팀원들과 작업을 했습니다! 제 생에 팀장이 처음이라 모자란 점이 많았는데 제준님, 다솔님, 우철님, 정진님 모두 잘 이끌어주시고 좋은 의견을 많이 내주셔서 개발하면서 즐겁게 소통도 하고 좀 더 개발을 즐길수 있었습니다.
    
    아쉬운점은 제 실력 문제로 원하는 페이지를 구현하지 못한것 같아 팀원분들께도 미안하네요. 배포도 문제가 생겨 완전하지 못한 개발이 된것같아 아쉽습니다. 다음에는 좀 더 시간적 여유를 두고 배포를 해봐야할것 같네요.
    
    완벽하지 못했을지라도, 2주간 우리 팀은 정말 최고였다고 생각해요! 멋지고, 잘하셨고, 수고하셨습니다!

