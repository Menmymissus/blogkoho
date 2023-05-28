from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from apis.views import BlogView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("",BlogView, basename='blogview')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apis/", include("apis.urls")),
    path("img/",include(route.urls)),
    path("", TemplateView.as_view(template_name="index.html")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
