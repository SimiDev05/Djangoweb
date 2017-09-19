from django.http import HttpResponse

def index(request):
    return HttpResponse('<hi>this is the music app page <hi>')
