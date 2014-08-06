from django.shortcuts import render, redirect
from django.http import HttpResponse


def blank(request):
    return redirect('/Trade/index')


def index(request):
    return render(request, 'Trade/index.html')
