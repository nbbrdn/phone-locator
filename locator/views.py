from django.shortcuts import render

from .forms import PhoneNumberForm


def index(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number", "")
        print(phone_number)
        operator, region = "MTS", "Khabarovsk"
        return render(
            request, "search-result.html", {"operator": operator, "region": region}
        )
    context = {"form": PhoneNumberForm}
    return render(request, "index.html", context)
