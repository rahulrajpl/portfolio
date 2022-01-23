from django.shortcuts import render

# Create your views here.

def hello_world(request):
    context = {}
    return render(request, 'hello_world/hello.html', context = context)