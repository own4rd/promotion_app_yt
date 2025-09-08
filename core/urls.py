from django.contrib import admin
from django.urls import path, include
from home import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view),
    path('promocoes/', include('promotions.urls')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
