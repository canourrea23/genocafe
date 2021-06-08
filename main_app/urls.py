# backend/urls.py
from django.conf.urls import url
# from mysite.core import views as core_views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views
# from django.conf import settings
# from django.contrib.auth.views import logout

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'product')
router.register(r'blog', views.BlogView, 'blog')
router.register(r'user', views.UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # url(r'api/users^$', views.UserCreate.as_view(), name='main_app-create'),
    # url(r'^users/register', 'main_app.views.create_auth'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name="signup")
]
