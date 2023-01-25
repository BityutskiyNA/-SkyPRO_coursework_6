from django.urls import include, path

from .views import AdViewSet, CommentViewSet
# TODO настройка роутов для модели
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'ads', AdViewSet)

comments_router = routers.NestedSimpleRouter(router, r'ads', lookup='ads')
comments_router.register(r'comments', CommentViewSet, basename='ads-CommentViewSet')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(comments_router.urls)),
]
