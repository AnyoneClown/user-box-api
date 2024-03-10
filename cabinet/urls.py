from django.urls import path

from cabinet.views import BoxDetailUpdateView, MyBoxesListView

urlpatterns = [
    path("boxes/<int:pk>/", BoxDetailUpdateView.as_view(), name="boxes-detail"),
    path("my-boxes/", MyBoxesListView.as_view(), name="my-boxes-list")
]

app_name = "cabinet"
