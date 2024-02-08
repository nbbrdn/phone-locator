from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import PhoneNumberForm
from .models import DEFCode


def index(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = request.POST.get("phone_number", "")
            if phone_number.startswith("7"):
                phone_number = phone_number[1:]

            try:
                def_code = DEFCode.objects.get(
                    code=int(phone_number[:3]),
                    start_range__lte=int(phone_number[3:]),
                    end_range__gte=int(phone_number[3:]),
                )

                operator, region = def_code.operator, def_code.region
                return render(
                    request,
                    "search-result.html",
                    {
                        "phone_number": phone_number,
                        "operator": operator,
                        "region": region,
                    },
                )
            except DEFCode.DoesNotExist:
                return render(template_name="404.html", status=404, request=request)

    context = {"form": PhoneNumberForm}
    return render(request, "index.html", context)


class PhoneInfoAPIView(APIView):
    def get(self, request, phone_number):
        if request.method == "GET":
            try:
                if phone_number.startswith("7"):
                    phone_number = phone_number[1:]

                    def_code = DEFCode.objects.get(
                        code=int(phone_number[:3]),
                        start_range__lte=int(phone_number[3:]),
                        end_range__gte=int(phone_number[3:]),
                    )

                    response_data = {
                        "phone_number": phone_number,
                        "operator": def_code.operator,
                        "region": def_code.region,
                    }

                    return Response(response_data, status=status.HTTP_200_OK)

                return Response(
                    {"error": "Bad phone number format"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except DEFCode.DoesNotExist:
                return Response(
                    {"error": "Not found"}, status=status.HTTP_404_NOT_FOUND
                )

        return Response(
            {"error": "Bad request method"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
