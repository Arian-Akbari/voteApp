from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Food


# Create your views here.


def start(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def select(request, name):
    myFood = Food.objects.all().values()
    template = loader.get_template('voting.html')
    context = {
        "allFoods": myFood,
        "foodType": name,
    }
    return HttpResponse(template.render(context, request))


def finish(request):
    templates = loader.get_template('finish.html')
    return HttpResponse(templates.render())


def results(request):
    myFood = Food.objects.all().values()
    template = loader.get_template('results.html')
    context = {
        "allFoods": myFood,
    }
    return HttpResponse(template.render(context, request))
