from django.urls import path
from . import views
urlpatterns = [
    path('play',views.playLocal,name='playLocal'),
    path('ai',views.playAI,name='playAI'),
    path('',views.chooseMode,name='chooseMode'),
    path('board',views.board),
    path('reset',views.resetBoard,name='resetBoard')
]
