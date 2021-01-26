from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is a homepage")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this is a aboutpage")

def services(request):
    return HttpResponse("this is a servicespage")

def contact(request):
    return HttpResponse("this is a contactpage")
