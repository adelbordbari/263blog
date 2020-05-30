from django.urls import path
from .views import post_list, post_details


urlpatterns = [
    path('', post_list.as_view(), name='home'),
    path('post/<int:pk>', post_details.as_view(), name='details')
]
