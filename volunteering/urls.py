from rest_framework.routers import DefaultRouter
from django.urls import path, include
from volunteering.views import *


router = DefaultRouter()
router.register('', VolunteerModelViewSet)

urlpatterns = [
    path('volonteer_confirm/<uuid:code>', VolunteerConfirmAPIView.as_view()),
    path('', include(router.urls))

]