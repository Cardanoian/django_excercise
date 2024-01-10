from django.http.response import HttpResponse
from django.shortcuts import render


def home_view(request):
    return HttpResponse("HOME VIEW")


def my_custom_page_not_found_view(request, exception):
    return render(request, "error_view.html", status=404)
