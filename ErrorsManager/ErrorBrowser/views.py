from django.http import HttpResponse
from django.shortcuts import render
from ErrorBrowser.models import ErrorCategory, ErrorDefinition, ErrorFilter, StackFilter

# Create your views here.

def doc_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args)
    print(kwargs)
    return render(request, "docTemplate.html", {})

def doc_view2(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args)
    print(kwargs)
    return render(request, "docTemplate2.html", {})


def browseFilters_view(request, *args, **kwargs):
    defs = ErrorDefinition.objects.all()
    l = len(defs)
    context = {"definitions" : defs}
    return render(request, "browseFilters.html", context)

