# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from psw.forms import CommandForm, ClientForm

def index(request):
    context = {'boldmessage': "I am bold font from the context"}
    return render(request, 'psw/index.html', context)

def servers(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/psw')
    else:
         form = CommandForm()
    return render(request, 'psw/servers.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/psw')
    else:
         form = ClientForm()
    return render(request, 'psw/register.html', {'form': form})