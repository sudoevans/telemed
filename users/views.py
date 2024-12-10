from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create your views here.


class RegisterViewSet( UserViewSet):
    pass

class LoginViewSet(TokenObtainPairView):
    pass

class RefreshViewSet(TokenRefreshView):
    pass
