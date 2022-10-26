from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    path('crud', views.crudview.as_view(), name='crudview'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),

]
