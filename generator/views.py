from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters_lower_eng = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('engup'):
        characters_lower_eng.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters_lower_eng.extend(list('1234567890'))
    if request.GET.get('special'):
        characters_lower_eng.extend(list('!@#$%^&*()'))
    if request.GET.get('ruslow'):
        characters_lower_eng.extend(list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))
    if request.GET.get('rusup'):
        characters_lower_eng.extend(list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'))

    length = int(request.GET.get('length', 10))

    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters_lower_eng)

    return render(request, 'generator/password.html', {'password': thePassword})
