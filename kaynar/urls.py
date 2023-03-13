from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
    title='Kaynar',
    default_version='v1',
    description='blog'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    # path('api/v1/acount/', include('account.urls')),
    # path('api/v1/post/', include('feedback.urls')),
    # # path('api/v1/feedback/', include('.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
