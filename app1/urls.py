from django.urls import path
from .views import *

urlpatterns= [
    path('', index, name='index'),
    path('category/<slug>/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('view/<int:pk>/', view, name='view'),
    path('404/',page_not_found, name='404'),
    path('login/', login_page, name='login')
] 