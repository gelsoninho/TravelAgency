from django.urls import path, include
from . import views

urlpatterns = [
    path('offres/', views.offres_list, name='offres_list'),
    path('offres/details/<int:offre_id>/', views.offres_detail, name='offres_detail'),
    path('login/', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
]
