from django.shortcuts import render

# Create your views here.
def laddu(request):
    return render(request,'laddu.html')

def pandu(request):
    return render(request,'pandu.html')