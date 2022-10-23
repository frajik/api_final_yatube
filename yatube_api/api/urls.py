from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)
jwt_patterns = [
    path("verify/", TokenVerifyView.as_view(), name='token_verify'),
    path("create/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]
v1_router = DefaultRouter()
v1_router.register(r"posts", PostViewSet)
v1_router.register(r"groups", GroupViewSet)
v1_router.register(r"follow", FollowViewSet, basename="follow")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
    basename="comments"
)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/jwt/", include(jwt_patterns)),
]
