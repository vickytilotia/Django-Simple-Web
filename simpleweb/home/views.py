from django.shortcuts import render, HttpResponse
from home.models import Contact

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
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        contact = Contact(name=name, email =email, phone=phone, desc=desc)
        contact.save()
    
    
    return render(request, 'contact.html')
