from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('all_tasks',views.all_tasks,name='all_tasks'),
    # path('<id>/update',views.update_task,name= 'update'),
    path('delete/<int:id>',views.delete_task,name='delete'),
]
