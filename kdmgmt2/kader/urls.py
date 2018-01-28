from django.urls import path

from . import views

urlpatterns = [
    path('', views.MemberListView.as_view(), name='home'),
    path('create/', views.MemberCreate.as_view(), name='create'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.MemberUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.MemberDelete.as_view(), name='delete'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
