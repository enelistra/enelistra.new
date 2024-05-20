from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('addcars/',views.addcars,name='addcars'),
    path('newcars/',views.newcars,name='newcars'),
    path('add_featuredcars/',views.add_featuredcars,name='add_featuredcars'),
    path('car_details/<int:car_id>/', views.car_details, name='car_details'),
    path('updatenewcars/<int:pk>/', views.updatenewcars, name='updatenewcars'),
    path('featuredcars/',views.featuredcars,name='featuredcars'),
    path('featuredcar_details/<int:car_id>/', views.featuredcar_details, name='featuredcar_details'),
    path('edit_featuredcar/<int:car_id>/', views.edit_featuredcar, name='edit_featuredcar'),
    path('viewfeatured/<int:car_id>/', views.viewfeatured, name='viewfeatured'),
    path('viewnewcars/<int:car_id>/', views.viewnewcars, name='viewnewcars'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('delete_newcar/<int:car_id>/', views.delete_newcar, name='delete_newcar'),
]
