from django.shortcuts import render

# Create your views here.
def sample1(request):
    return render(request,"sample.html")