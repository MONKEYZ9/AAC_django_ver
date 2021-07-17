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
- Profileapp 디렉토리 설정 
- modelform 생성
- view 랑 model 설정
