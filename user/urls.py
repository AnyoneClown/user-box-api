from django.urls import path

from user.views import UserView, CreateTokenView

urlpatterns = [
    path("", UserView.as_view(), name="user-list-create"),
    path("<int:pk>/", UserView.as_view(), name="user-detail"),
    path("token-auth/", CreateTokenView.as_view(), name="token-auth")
]

app_name = "users"
