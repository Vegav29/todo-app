from django.urls import path
from django.contrib.auth import views as auth_views
from .views import homeView, completeTaskView, editTaskView, deleteTaskView,deleteAllTaskView,signup

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path("", homeView, name="homeView"),
    path("complete/<id>", completeTaskView, name="completeTaskView"),
    path("edit/<id>", editTaskView, name="editTaskView"),
    path("delete/<id>", deleteTaskView, name="deleteTaskView"),
    path("delete/", deleteAllTaskView, name="deleteAllTaskView"),
]
