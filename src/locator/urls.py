from django.urls import path

from .views import PhoneInfoAPIView, index

urlpatterns = [
    path("", index, name="index"),
    path(
        "api/phone-info/<str:phone_number>",
        PhoneInfoAPIView.as_view(),
        name="phone_info",
    ),
]
