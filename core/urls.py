from django.contrib import admin
from django.urls import path
from home import views
from debug_toolbar.toolbar import debug_toolbar_urls
<<<<<<< Updated upstream
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> Stashed changes

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
<<<<<<< Updated upstream

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
>>>>>>> Stashed changes
