from django.urls import path
import lists.views as views

app_name = 'lists'

urlpatterns = [
    path('', views.home_page, name='home'),
]
