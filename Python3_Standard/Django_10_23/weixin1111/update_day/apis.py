from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return render(request, "hello world")
    return HttpResponse(b"hello world!")