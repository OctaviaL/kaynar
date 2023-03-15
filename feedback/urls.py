from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter
from feedback.views import FavoriteModelViewSet


router = DefaultRouter()
router.register('', CommentModelViewSet)
router.register('', FavoriteModelViewSet)


app_name = 'yourapp'

urlpatterns = [
    path('', include(router.urls)),
    path('favorite/', include(router.urls)),
    path('comment/', include(router.urls)),
]


