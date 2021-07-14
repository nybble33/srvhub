from django.shortcuts import render

def index (request):
    context = {}
    return render(request, 'cms/index.html', context)

def variant_1 (request):
    context = {}
    return render(request, 'cms/variant_1.html', context)
