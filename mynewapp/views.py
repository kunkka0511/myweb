from django.shortcuts import render
from django.http import HttpResponse

def mynewapp(request):
    # Your view logic here
    return render(request, 'index.html')   
    
def services(request):
    # index хуудсанд ажиллах кодыг энд бичнэ
    return render(request, 'services.html')

def about(request):
    # about хуудсанд ажиллах кодыг энд бичнэ
    return render(request, 'about.html')

def contact(request):
    # contact хуудсанд ажиллах кодыг энд бичнэ
    return render(request, 'contact.html')