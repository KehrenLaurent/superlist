from django.urls import path
import lists.views as views

app_name = 'lists'

urlpatterns = [
    path('lists/<int:pk>/',
         views.view_list, name='view_list'),
    path('lists/<int:pk>/add_item', views.add_item, name='add_item'),
    path('lists/new', views.new_list, name='new_list'),
]
