from django.shortcuts import render

def mynewapp(request):
    # Your view logic here
    return render(request, 'index.html')
def about(request):
    # Your view logic here
    return render(request, 'about-us.html')
    
    
