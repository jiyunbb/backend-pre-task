"""backend URL Configuration

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
from apps.contact import views as contact_views
from apps.user import views as user_view
from django.urls import path

urlpatterns = [
    # 주소록 유저 목록 조회/입력
    path("contacts/<int:contact_id>/users", contact_views.ContactUserListView.as_view()),

    # 유저 상세 조회
    path("users/<int:user_id>", user_view.UserDetailView.as_view()),
]
