from django.urls import path

from . import views

urlpatterns = [
    path('', views.MemberListView.as_view(), name='home'),
    path('create/', views.MemberCreate.as_view(), name='create'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.MemberUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', views.MemberDelete.as_view(), name='delete'),

    path('attendance', views.AttendanceListView.as_view(), name='attendance_list'),
    path('attendance/create', views.AttendanceCreateView.as_view(), name='attendance_create'),
    path('attendance/<int:pk>', views.AttendanceDetailView.as_view(), name='attendance_detail'),
    path('attendance/<int:pk>/edit', views.AttendanceUpdateView.as_view(), name='attendance_edit'),
    path('attendance/<int:pk>/delete', views.AttendanceDeleteView.as_view(), name='attendance_delete'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
