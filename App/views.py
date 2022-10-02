from django.shortcuts import render

# Create your views here.

def Statements(request):
    d={'a':15,'b':26,'c':17}
    return render(request,'Statements.html',context=d)