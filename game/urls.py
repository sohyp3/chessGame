from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainView,name='boardView'),
    path('board',views.board),
    path('reset',views.resetBoard,name='resetBoard')
]
