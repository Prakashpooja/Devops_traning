from django.urls import path
from .views_v1 import user_info_v1
from .views_v2 import user_info_v2

urlpatterns = [
    path('v1/user/', user_info_v1),
    path('v2/user/', user_info_v2),
]
