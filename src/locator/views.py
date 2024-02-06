from django.shortcuts import get_object_or_404, render

from .forms import PhoneNumberForm
from .models import DEFCode


def index(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = request.POST.get("phone_number", "")
            if phone_number.startswith("7"):
                phone_number = phone_number[1:]

            def_code = get_object_or_404(
                DEFCode,
                code=int(phone_number[:3]),
                start_range__lte=int(phone_number[3:]),
                end_range__gte=int(phone_number[3:]),
            )

            operator, region = def_code.operator, def_code.region
            return render(
                request, "search-result.html", {"operator": operator, "region": region}
            )

    context = {"form": PhoneNumberForm}
    return render(request, "index.html", context)


def not_found(request, exception):
    return render(request, "404.html", status=404)
