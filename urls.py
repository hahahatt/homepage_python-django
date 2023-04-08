from django.urls import path

from . import views
from .views import *


urlpatterns=[
        path('',views.index,name='index'),
        path('content_1',views.content_1, name='content_1'),
        path('content_2',views.content_2, name='content_2'),
        path('content_1_1',views.content_1_1, name='content_1_1'),
        path('content_3',views.content_3, name='content_3'),
        path('firstpg', views.firstpg, name='firstpg'),
        path('content_1_2',views.content_1_2,name='content_1_2'),
        path('content_3_1',views.content_3_1,name='content_3_1'),
        path('content_3_2',views.content_3_2,name='content_3_2'),
        path('content_3_3',views.content_3_3,name='content_3_3'),
        path('board',views.board,name='board'),
        path('board/edit/<int:pk>',views.boardEdit,name='edit'),
        path('board/delete/<int:pk>',views.boardDelete,name='delete'),
        path('board/<int:pk>',views.detail_content,name='detail'),
        path('board/<int:pk>/create_reply',views.create_reply,name='create_reply'),
]