# -*- coding: utf-8 -*-
from django.template import loader, Context, Template
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello')