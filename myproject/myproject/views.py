from django.http import HttpResponse

def home(req):
    return HttpResponse("Hola Mundo!")