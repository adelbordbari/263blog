from django.urls import path
from .views import *
from uhf.views import *

urlpatterns = [
    path('', post_list_view.as_view(), name='home'),
    path('post/<slug:slug>/', post_details_view.as_view(), name='details'),
    path('write/', add_post_view.as_view(), name='add_post'),
    path('category/', add_category_view.as_view(), name='add_category'),
    path('post/edit/<slug:slug>/', update_post_view.as_view(), name='update_post'),
    path('post/<slug:slug>/delete/',
         delete_post_view.as_view(), name='delete_post'),
    path('register/', signup_view.as_view(), name='register'),
]
