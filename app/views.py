from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'bristi','age':23}
    return render(request,'data_render.html',context=d)


def if_block(request):
    d={'a':10}
    return render(request,'if_block.html',context=d)


def if_else(request):
    d={'a':10,'b':20}
    return render(request,'if_else.html',context=d)

def if_elif(request):
    d={'a':20,'b':5,'c':10}
    return render(request,'if_elif.html',context=d)

def nested_if(request):
    d={'a':10,'b':15,'c':20}
    return render(request,'nested_if.html',context=d)