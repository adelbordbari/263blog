from django.urls import path
from .views import *
from uhf.views import *

urlpatterns = [
    path('', post_list_view.as_view(), name='home'),
    path('post/<int:pk>/', post_details_view.as_view(), name='details'),
    path('write/', add_post_view.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', update_post_view.as_view(), name='update_post'),
    path('post/<int:pk>/delete/',
         delete_post_view.as_view(), name='delete_post'),
    path('register/', signup_view.as_view(), name='register'),
    path('like/<int:pk>', like_view, name='like_post')
]
