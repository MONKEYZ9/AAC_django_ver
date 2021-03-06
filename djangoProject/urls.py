"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accountapp.urls')),
                  path('profiles/', include('profileapp.urls')),
                  path('articleapp/', include('articleapp.urls')),
                  #     미디어 관련 셋팅
                  #     이런식으로 저장해줘야 서버에서 이걸 찾아준다는 거야
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
