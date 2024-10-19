from django.shortcuts import render

import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

# Create your views here.

def index(request):
    template = 'dashboard.html'
    c = {
        'titulo': 'ESTA ES TU CASA',
        'mensaje': 'Este es un mensaje desde la vista home'
    }
    return render(request, template, c)

