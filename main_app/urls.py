# backend/urls.py
# from django.conf.urls import url
# from mysite.core import views as core_views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views
from django.conf import settings
from django.contrib.auth.views import logout

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'product')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/',  include(router.urls)),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
         name='logout'),
    # path("/", include('main_app.urls)
]
