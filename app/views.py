from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'bristi','age':23}
    return render(request,'data_render.html',context=d)


def if_block(request):
    d={'a':10}
    return render(request,'if_block.html',context=d)