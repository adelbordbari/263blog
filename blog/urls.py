from django.urls import path
from .views import post_list_view, post_details_view, add_post_view


urlpatterns = [
    path('', post_list_view.as_view(), name='home'),
    path('post/<int:pk>', post_details_view.as_view(), name='details'),
    path('/write', add_post_view.as_view(), name='add_post'),
]
