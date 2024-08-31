from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def presentation(request):
    template = loader.get_template('presentation.html')
    return HttpResponse(template.render())

def personalinfo(request):
    template = loader.get_template('personal_info.html')
    return HttpResponse(template.render())

def education(requests):
    template = loader.get_template('estudios.html')
    return HttpResponse(template.render())

def skills(request):
    template = loader.get_template('skills.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def backtpresentation(request):
    template = loader.get_template('presentation.html')
    return HttpResponse(template.render())

def backtinforperonsal(request):
    template = loader.get_template('personal_info.html')
    return HttpResponse(template.render())
    
def backtstudies(request):
    template = loader.get_template('estudios.html')
    return HttpResponse(template.render())

def backstskills(request):
    template = loader.get_template('skills.html')
    return HttpResponse(template.render())