from django.urls import path
import lists.views as views

app_name = 'lists'

urlpatterns = [
    path('<int:pk>/',
         views.view_list, name='view_list'),
    path('new', views.new_list, name='new_list'),
]
