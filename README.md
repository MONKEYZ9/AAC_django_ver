#AAC 프로젝트 장고버전

###7/5
- accountapp 추가
- html 작업 분할 완료 extends & include 사용

###7/6
- googlefonts 적용
- bootstrap 적용
- css 따로 만들어서 적용

###0708
- model 생성

###0712
- sql 설치
- 모델의 text 추출
- 모델의 객체 전부 추출
- rediect 설정

###0713
- createView 생성
- 회원가입 폼을 적용 (일단, 실행)
- 로그인(settin.py LOGIN_REDIRECT_URL 다시 설정)

###0715
- 로그인, 회원가입 버튼 생성
- django-bootstrap4 설치 및 해당 form 사용 
- 회원정보 확인 탭 생성
- 회원정보 urls, path 파라메터값 받아주기

###0717
1. Accountapp implementaion
- 회원정보 업데이트 form.py 생성으로 새로운 폼 커스터마이즈
- 회원 탈퇴 detail에 탈퇴버튼 추가
- 회원 탈퇴 urls, path 추가
  
2. Authentication
- Authentication 인증 시스템을 구축
- Decator를 이용한 코드 간소화
- 본인인지 확인 하는 작업 및 타인거 못 건들게 함
- 관리자 계정 생성
  python manage.py createsuperuser
- 미디어 계정 media url 생성
- 장고 이미지 관리 ilb 설치(pillow)

3. Profileapp Implementaion
1. python manage.py startapp profileapp
- Profileapp 디렉토리 설정 
- modelform 생성
- view 랑 model 설정
- # path('profiles/', include('profileapp.urls')),
- python manage.py makemigrations
- python manage.py migrate 가 안된 이유를 찾았다.
- 비어져있는 것으로 연결을 하려다보니까 안되는 건데

### 0719
1. profileapp 
- CreateView 작성
- create urls, view urlspattern 수정
- accountdetail에 profile create 경로 수정
- enctype="multipart/form-data" 을 추가함으로 사진을 추가할 수 있게끔
- model에서 user을 가지고 만들어놨는데
- profile이 update a태그 & update.html 추가
- 사진을 보이게 하는 것은 전체 setting.py에 django.conf.urls.static의 static 추가
- decorator 추가
