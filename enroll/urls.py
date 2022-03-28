from django.urls import path
from enroll import views

urlpatterns = [
    path("", views.add_show, name="home"),    
    path("delete/<int:id>/", views.delete, name="delete"),   
    path("update/<int:id>/", views.update, name="update")    
]
