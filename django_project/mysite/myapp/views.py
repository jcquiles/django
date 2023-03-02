from django.shortcuts import render
from django.http import HttpResponse
# from aws_xray_sdk.core import xray_recorder

# Create your views here.
def index(request):
    # with xray_recorder.in_subsegment('my-segment'):
        return HttpResponse("Hello, world!")