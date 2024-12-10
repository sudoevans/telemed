from django.urls import path
from .views import UserCreateView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register(r"signup", views.RegisterViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('refresh/', views.RefreshViewSet.as_view(), name='refresh')
]