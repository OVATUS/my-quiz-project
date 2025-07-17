from quiz import views
from django.urls import path

urlpatterns = [
   path("question/",views.question),
   path("question/create/",views.create_question),
   path("",views.home)
   
]