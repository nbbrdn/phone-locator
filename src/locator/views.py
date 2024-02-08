from django.shortcuts import render

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
