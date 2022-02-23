from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import TokenObtainPairView, TokenRefreshView, SignupAPIView, UserViewSet, PasswordChangeView

app_name = "accounts"

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]


urlpatterns += [
    path("api/signup/", SignupAPIView.as_view(), name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_view"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/login/changepassword/", PasswordChangeView.as_view(), name="change_password"),
]