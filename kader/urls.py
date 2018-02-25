from django.urls import path

from . import views

urlpatterns = [
    path('', views.MemberListView.as_view(), name='home'),
    path('csv', views.export_members_to_csv, name='csv_export'),
    path('create/', views.MemberCreate.as_view(), name='create'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.MemberUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', views.MemberDelete.as_view(), name='delete'),

    path('training', views.TrainingListView.as_view(), name='training_list'),
    path('training/create', views.TrainingCreateView.as_view(), name='training_create'),
    path('training/<int:pk>/csv', views.export_training_to_csv, name='training_csv'),
    path('training/<int:pk>/edit', views.TrainingUpdateView.as_view(), name='training_edit'),
    path('training/<int:pk>/delete', views.TrainingDeleteView.as_view(), name='training_delete'),

    path('training/<int:training_pk>/fight', views.FightCreateView.as_view(), name='fight_create'),
    path('training/<int:training_pk>/fight/<int:pk>/edit', views.FightUpdateView.as_view(), name='fight_update'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
