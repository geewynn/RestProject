from django.urls import path, include
from restapp import views, api_views

urlpatterns = [

    path('api/v1/menu', api_views.MenuList.as_view()),
    path('api/v1/menu/new', api_views.CreateMenu.as_view()),
    path('api/v1/menu/<id>/', api_views.MenuRetrieveUpdateDestroy.as_view()),
    path('api/v1/menu/<id>/stats', api_views.MenuStats.as_view()),
    path('', views.showRestaurants, name='restaurants'),
    path('add/', views.addRestaurants, name='add'),
    path('edit/<id>', views.editRestaurants, name='edit'),
    path('<id>/delete/', views.deleteRestaurants, name='delete'),
    path('menu/<id>', views.showMenu, name='menu'),
    path('addmenu/<id>/', views.addMenu, name='addmenu'),
    path('menu/edit/<id>', views.editMenu, name='editmenu'),
    path('menu/<id>/delete', views.deleteMenu, name='deletemenu'),

]