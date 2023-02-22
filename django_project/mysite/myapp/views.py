from django.shortcuts import render
from django.http import HttpResponse
from aws_xray_sdk.core import xray_recorder

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def my_view(request):
    # Start an X-Ray segment
    segment_name = 'my_segment'
    xray_recorder.begin_segment(name=segment_name)

    # ... do some work ...

    # Get the current active segment
    segment = xray_recorder.current_segment()

    # ... do some more work ...

    # End the X-Ray segment
    xray_recorder.end_segment()
    
    return HttpResponse('Hello, world!')