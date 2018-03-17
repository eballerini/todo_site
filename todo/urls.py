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
    # TODO add new endpoint for list of todos
    # ex: /todo/5/
    path('<int:item_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('add_item', views.add_item_to_list, name='add_item'),
    path('clear_list', views.clear_list, name='clear_list'),
    path('list', views.get_items_list, name='get_items_list')
    
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]