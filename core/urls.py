from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("user.urls", namespace="users")),
    path("api/cabinet/", include("cabinet.urls", namespace="cabinet"))
]
