from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainView,name='mainView'),
    path('board',views.board)
]
