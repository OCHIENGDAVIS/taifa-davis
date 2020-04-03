from django.urls import path
from . import views

app_name = 'scrapings'

urlpatterns = [
    path('', views.citizen, name='citizen'),
    path('ntv/', views.ntv, name='ntv'),
    path('ktn/', views.ktn_news, name='ktn_news'),
    path('k24/', views.k24, name='k24'),
]