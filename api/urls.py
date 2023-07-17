from django.urls import path

from api.views import UserAccessView

urlpatterns = [
    path("", UserAccessView.as_view())
]