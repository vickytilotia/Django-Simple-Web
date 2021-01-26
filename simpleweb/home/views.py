from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is a homepage")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("this is a aboutpage")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is a servicespage")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("this is a contactpage")
    return render(request, 'contact.html')
