from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comment', CommentModelViewSet)
router.register('', FavoriteModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('favorite/', include(router.urls)),

]



