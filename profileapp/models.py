from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # ondelete 연결된 객체가 삭제될때의 정책 부분을 담당하는것
    # CASCADE는 이 프로필이 없어지게
    # related_name으로 바로 연결할 수 있게
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # upload_to 이미지를 저장할 건데 경로를 정해주는 것
    # 미디어 경로를 설정해줄 때 하위 주소로 적히게 된다는 것
    image = models.ImageField(upload_to='profile/', null=True)
    # unique값을 줌으로 유일하게, null은 null이 되지 않으면 null이 되게끔
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
# 따로 프로필 객체를 찾지 않더라도 찾을 수 있게
