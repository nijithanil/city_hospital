from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Department
from .models import Department
from .models import Doctor
from .forms import BookingForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dic_form = {
        'form': form
    }
    return render(request, 'booking.html', dic_form)


def doctor(request):
    doctor_doc = {
        'doc': Doctor.objects.all()
    }
    return render(request, 'doctor.html', doctor_doc)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    depart = {
        'dept_ment': Department.objects.all()
    }
    return render(request, 'department.html', depart)
