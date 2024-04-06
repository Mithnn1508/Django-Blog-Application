from django.urls import path
from .views import UserRegister,CheckGet
from rest_framework_simplejwt import views as jwt_views 

urlpatterns = [
    path("register",UserRegister.as_view()),
    path('login',jwt_views.TokenObtainPairView.as_view()),
    path('login/refresh',jwt_views.TokenRefreshView.as_view()),
    path('check',CheckGet.as_view())
]