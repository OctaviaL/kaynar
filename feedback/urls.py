from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comment', CommentModelViewSet,basename='comment')
router.register('favorite', FavoriteModelViewSet,basename='favorite')

app_name = 'yourapp'
urlpatterns = [
    path('', include(router.urls)),]


