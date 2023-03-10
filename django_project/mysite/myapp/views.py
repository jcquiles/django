from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # with xray_recorder.in_subsegment('my-segment'):
        return HttpResponse("Hello, world!")
