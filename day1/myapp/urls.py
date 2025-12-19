from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from . import views
#from .views import StudentViewSet, simple_page
from .views import simple_page, student_api, ProfileAPI
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



# router = DefaultRouter()
# router.register(r'students', StudentViewSet)
urlpatterns = [
    # path('hello/', views.hello),   # default route
    # path('bye/', views.bye),   # default route
    # path('echo/', views.echo),
    # path('update/', views.update_echo),     # PUT
    # path('delete/', views.delete_echo), 
    # path('cbv-post/', views.SimplePostView.as_view()), 
    # path('cbv-get/', views.SimplePostView.as_view()), 
    # path('', include(router.urls)),
    path('simple-products/', simple_page),
    path('newstudents/', student_api),
    path("login/", views.login_page),
    path("home/", views.home),
    path("profile/", ProfileAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),  
    path("jwt/login/", TokenObtainPairView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view()),      
]


