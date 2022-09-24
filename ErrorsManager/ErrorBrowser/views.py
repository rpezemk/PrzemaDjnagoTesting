from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def doc_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args)
    print(kwargs)
    return render(request, "docTemplate.html", {})


    