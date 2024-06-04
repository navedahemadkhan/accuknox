from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer
from .models import FriendRequest
from .serializers import FriendRequestSerializer
from rest_framework import viewsets


class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email').lower()
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def perform_create(self, serializer):
        from_user = self.request.user
        to_user_id = self.request.data.get('to_user')
        to_user = CustomUser.objects.get(id=to_user_id)
        serializer.save(from_user=from_user, to_user=to_user)

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user, is_accepted=False)
