"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required

from app.models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


@login_required
def schedule(request):
    
    assert isinstance(request, HttpRequest)

    st = Student.objects.get(user=request.user)
    schedule = Schedule.objects.get(student=st)
    _class1 = Class.objects.get(id=schedule.period1class)
    _class2 = Class.objects.get(id=schedule.period2class)
    _class3 = Class.objects.get(id=schedule.period3class)
    _class4 = Class.objects.get(id=schedule.period4class)
    _class5 = Class.objects.get(id=schedule.period5class)
    _class6 = Class.objects.get(id=schedule.period6class)
    _class7 = Class.objects.get(id=schedule.period7class)
    context = { 
        'title':'Schedule',
        'message':'Your application description page.',
        'year':datetime.now().year,
        'schedule':schedule,
        'class1':_class1,
        'class2':_class2,
        'class3':_class3,
        'class4':_class4,
        'class5':_class5,
        'class6':_class6,
        'class7':_class7
        }

    return render(
        request,
        'app/schedule.html',
        context
    )
    