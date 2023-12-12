from django.shortcuts import render
from .forms import UserForm, LogForm
from django.http import HttpResponse
from .models import Person


def data(request):
    tom = Person.objects.get_or_create(name='Tom', age=14, date='2015-02-03 10:55:15', agree=False)
    try:
        mike = Person.objects.get(name='Mike')
        mike.delete()
    except:
        mike = Person(name='Mike', age=25, date='2015-02-03 10:55:15', agree=True)
        mike.save()
    data = Person.objects.filter(age__lt=20)
    return render(request, 'app/data.html', context={'data': data})


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponse(f'Name: {name}, Password: {password}, Email: {email}')
            if name == 'User1' and password == 12345678:
                return HttpResponse(f'Поздравляю с успешным входом')

        else:
            return render(request, registr())
    form = UserForm()
    return render(request, 'app/index.html', context={'form': form})

def registr(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponse(f'{name}, Поздравляю с регистрацией! /n Указанные вами данные: Name: {name}, Email: {email}, Password: {password}')