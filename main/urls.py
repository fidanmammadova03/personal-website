from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('blogs/tryanyway/', views.tryanyway, name='tryanyway'),
    path('blogs/cutsugar/', views.cutsugar, name='cutsugar'),
    path('blogs/remsleep/', views.remsleep, name='remsleep'),
    path('blogs/beingok/', views.beingok, name='beingok'),
    path('blogs/idea/', views.idea, name='idea'),
    path('blogs/books/', views.books, name='books'),
    path('projects/sales-dashboard/', views.sales_dashboard, name='sales_dashboard'),
]
