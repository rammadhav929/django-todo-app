from django.urls import path
from . import views

urlpatterns = [
 #   path('', views.home, name='home'),   # calls your view when URL = "/"
    #path('/todo',views.todo)
    path('',views.direct),
    path('todo/', views.todo, name='todo'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update_task/<int:id>/', views.update_task, name='update_task'),


]
