from django.urls import path, include
from feedback.views import *
from rest_framework.routers import DefaultRouter
# from feedb.views import add_comment_to_post

router = DefaultRouter()
router.register('', CommentModelViewSet)

app_name = 'yourapp'

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('feedback/<int:pk>/like/', include('')),
    # path('feedback/', include('feedback.urls')),
    #   path('post//comment/', add_comment_to_post, name='add_comment_to_post'),

]


