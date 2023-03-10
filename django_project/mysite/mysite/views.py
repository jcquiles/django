from django.http import HttpResponse
from aws_xray_sdk.core import xray_recorder, exceptions

def about(request):
    try:
        # Begin a new subsegment for the HTTP request
        subsegment = xray_recorder.begin_subsegment('HTTP Request')

        # Add HTTP request metadata to the subsegment
        subsegment.put_http_meta('url', request.build_absolute_uri())
        subsegment.put_http_meta('method', request.method)
        subsegment.put_http_meta('user_agent', request.META.get('HTTP_USER_AGENT'))

        # Perform some work...
        response = HttpResponse('about')

        # End the subsegment for the HTTP request
        xray_recorder.end_subsegment()

        return response

    except Exception as e:
        # Capture the exception and add it to the subsegment
        xray_recorder.end_subsegment(exception=e)

        # Raise the exception to be handled by Django
        raise
