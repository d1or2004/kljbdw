from django.urls import path
from .views import LandingView
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
