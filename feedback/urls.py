from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('comment', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

]


