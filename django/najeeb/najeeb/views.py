from django.shortcuts import render
def index(request):
    return render(request,'home.html')
def page(request):
    return render(request,'subpage.html')