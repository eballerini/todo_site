# from django.urls import path
# 
# from . import views
# 
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/5/
    path('<int:item_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]