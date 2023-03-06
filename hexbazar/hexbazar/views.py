from django.http import HttpResponse

def index(request):
    return HttpResponse('This is Homepage')

def about(request):
    return HttpResponse('This is About page')