from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import *

router = DefaultRouter()
router.register('pets', PetPostModelViewset),
router.register('pet_image', PetImageModelViewSet),


urlpatterns = [
    path('getlist_pets/', PetPostListGenericView.as_view()),
    path('getimage_pets/',PetImageListGenericView.as_view()),
    path('', include(router.urls)),

]