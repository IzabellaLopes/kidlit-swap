"""Views"""

from django.shortcuts import render
from django.http import HttpResponse


def add(request):
    return HttpResponse('Hello')