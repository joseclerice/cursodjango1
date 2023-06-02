from django.urls import path
# importando de views.py dentro do app
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),  # home
    path('recipes/category/<int:category_id>/',
         views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),

]
