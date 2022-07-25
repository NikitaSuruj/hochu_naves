from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import Newform
from .models import newfrm



def HomeView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'index.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'index.html',{'form': form, 'form2': form2})



def SucView(request):
    return render(request, 'success.html')

def CalcView(request):
    return render(request, 'calculator.html')

def CertView(request):
    return render(request, 'certificates.html')

def ContView(request):
    return render(request, 'contacts.html')

def PrivpolView(request):
    return render(request, 'privacy-policy.html')



def ForgView(request):
    if request.method == 'POST':
        form = Firstform(request.POST or  None, request.FILES or None)
        form2 = Secndform(request.POST or None, request.FILES or None)
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'forging.html',{'form': form, 'form2': form2})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'forging.html',{'form': form, 'form2': form2, 'error1':'не менее 10 цифр'})

def MetalprofView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'metal-profile.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'metal-profile.html',{'form': form, 'form2': form2})

def MetaltileView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'metal-tile.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'metal-tile.html',{'form': form, 'form2': form2})

def MonolithView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'monolith.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'monolith.html',{'form': form, 'form2': form2})

def PolycarbView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'polycarbonate.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'polycarbonate.html',{'form': form, 'form2': form2})

def ProfpipeView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'profile-pipe.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'profile-pipe.html',{'form': form, 'form2': form2})

def SoftroofView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'soft-roof.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'soft-roof.html',{'form': form, 'form2': form2})

def WoodView(request):
    if request.method == 'POST':
        form = Firstform(request.POST, request.FILES)
        form2 = Secndform(request.POST, request.FILES)
        
        if form.is_valid() or form2.is_valid():
            if form.is_valid():
                form.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot.py').read())
            else:
                form2.save()
                exec(open('C:/VSprojects/valera/hochu/home/robot2.py').read())
            return HttpResponseRedirect(reverse_lazy('home:suc'))
        else:
            form = Firstform()
            form2 = Secndform()
            return render(request, 'wood.html',{'form': form, 'form2': form2, 'error1':'Не менее 10 цифр'})
    else:
        form = Firstform()
        form2 = Secndform()
        return render(request, 'wood.html',{'form': form, 'form2': form2})






