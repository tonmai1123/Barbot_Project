from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('menu.html')
    template = loader.get_template('test.html')
    template = loader.get_template('Delete.html')
    template = loader.get_template('insert.html')
    template = loader.get_template('login.html')
    template = loader.get_template('Update.html')
    return HttpResponse(template.render())