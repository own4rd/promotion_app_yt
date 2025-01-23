from django.contrib import admin
from django.urls import path
from home import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
