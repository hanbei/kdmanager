from django.urls import path

from . import views

urlpatterns = [
    path('', views.MemberListView.as_view(), name='home'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
