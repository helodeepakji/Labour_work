from django.urls import path, include
from .import views

urlpatterns = [
    path('signin', views.loginView.as_view(), name='signin'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
