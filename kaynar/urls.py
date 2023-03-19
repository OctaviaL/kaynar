from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Kaynar",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('user.urls')),
    path('api/v1/post/', include('post.urls')),
    path('api/v1/spam/', include('spam.urls')),
    path('api/v1/volunteering/', include('volunteering.urls')),
   #  path('social-auth/', include('social_django.urls', namespace="social")),
    # path('api/v1/post/', include('feedback.urls')),
    path('api/v1/feedback/', include('feedback.urls')),
   #  path('api/v1/review/', include('review.urls')),

   #  re_path('rest-auth/', include('rest_auth.urls')),
   #  re_path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

