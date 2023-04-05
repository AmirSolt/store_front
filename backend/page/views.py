from django.shortcuts import render, HttpResponse

# Create your views here.



def page(request, page_name):
    return HttpResponse(f"This is the {page_name}")


def edit(request, page_name):
    return HttpResponse(f"This is the edit for {page_name}")
