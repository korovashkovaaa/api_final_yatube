from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='post-comments')
router.register(r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
                CommentViewSet, basename='post-comment')
router.register('groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]
