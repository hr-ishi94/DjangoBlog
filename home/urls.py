from django.urls import path
from . import views

app_name= 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('category/',views.category,name='category'),
    path('editors_pick/',views.editors_pick,name='editors_pick'),
]
