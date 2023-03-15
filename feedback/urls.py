from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', CommentModelViewSet)

app_name = 'yourapp'

urlpatterns = [
    path('', include(router.urls)),
]


from rest_framework.routers import DefaultRouter
from feedback.views import FavoriteModelViewSet

router = DefaultRouter()
router.register('', FavoriteModelViewSet)

urlpatterns = [
    path('favorite/', include(router.urls))

]

