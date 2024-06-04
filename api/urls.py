from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, FriendRequestViewSet

router = DefaultRouter()
router.register(r'friend-requests', FriendRequestViewSet, basename='friendrequest')

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls
