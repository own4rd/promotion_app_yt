from django.urls import path
from promotions.views import detail_promotion

app_name = 'promotions'

urlpatterns = [
    path('<slug:slug>/', detail_promotion, name='detail_promotion'),
]


