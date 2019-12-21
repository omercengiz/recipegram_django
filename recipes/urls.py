#new

from django.contrib import admin
from django.urls import path
from . import views

app_name = "recipes"


urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addrecipe/',views.addRecipe, name = "addrecipe"),
    path('recipe/<int:id>',views.detail, name = "detail"),  
    path('update/<int:id>',views.updateRecipe, name = "update"),  
    path('delete/<int:id>',views.deleteRecipe, name = "delete"),  
    path('',views.recipes, name = "recipes"),  
    path('comment/<int:id>',views.addComment, name = "comment"),  
]

