from django.urls import path
from .views import *
from uhf.views import *

urlpatterns = [
    path('', Post_List_View.as_view(), name='home'),
    path('post/<int:pk>/', Post_Details_View.as_view(), name='details'),
    path('write/', Add_Post_View.as_view(), name='add_post'),
    path('post/edit/<int:pk>/', Update_Post_View.as_view(), name='update_post'),
    path('post/<int:pk>/delete/',
         Delete_Post_View.as_view(), name='delete_post'),
    path('register/', Signup_View.as_view(), name='register'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('dislike/<int:pk>', dislike_view, name='dislike_post'),
]
