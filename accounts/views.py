from django.shortcuts import render, redirect
from .forms import RegisterationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login, authenticate, logout
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

# AUTH

def register(request):

    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = CustomUser.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                role = request.POST['role']
            )
            user.save()
            login(request, user)
            return redirect('user_profile')
        else:
            return render(request, 'accounts/auth/register.html',{'error':'Password Or Username Incorrect'})
    else:
      return render(request, 'accounts/auth/register.html')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'accounts/auth/login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/auth/login.html', {'error': 'Password Or Username Did Not Match.'})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# PATIENT

def user_appointments(request):
    return render(request, 'accounts/patient/appointments.html')

def user_invoice(request):
    return render(request, 'accounts/patient/IOP.html')

def user_profile(request):
    return render(request, 'accounts/patient/profile.html')

def user_medical_history(request):
    return render(request, 'accounts/patient/medical_history.html')

# DOCTOR

def doctor_appointments(request):
    return render(request, 'accounts/doctor/appointments.html')

def doctor_prescription(request):
    return render(request, 'accounts/doctor/prescriptions.html')

def doctor_profile(request):
    return render(request, 'accounts/doctor/profile.html')

# RECEPTIONIST

def receptionist_dashboard(request):
    patients = Patient.objects.all()
    appointments = Appointments.objects.all()
    total_appointments = appointments.count()
    appointments_done = appointments.filter(status='completed').count()
    appointments_pending = appointments.filter(status='pending').count()
    context = {
        'patients':patients,
        'appointments':appointments,
        'appointments_pending':appointments_pending,
        'appointments_done':appointments_done,
        'total_appointments':total_appointments,
    }
    return render(request, 'accounts/receptionist/dashboard.html',context)

# HR

def hr_dashboard(request):
    doctors = Doctor.objects.all()
    total_patients = Patient.objects.all().count()
    total_doctors = doctors.count()
    active_doctors = doctors.filter(status="active").count()
    context = {
        'doctors':doctors,
        'total_patients':total_patients,
        'total_doctors':total_doctors,
        'active_doctors':active_doctors,
    }
    return render(request, 'accounts/HR/dashboard.html',context)

def hr_accounting(request):
    return render(request, 'accounts/HR/accounting.html')

def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receptionist_dashboard')

    context = {
        'form':form
    }
    return render(request,'accounts/forms/appointments.html',context)

def create_patient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receptionist_dashboard')

    context = {
        'form':form
    }
    return render(request,'accounts/forms/patient.html',context)

def update_patient(request,pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('receptionist_dashboard')

    context = {
        'form':form
    }
    return render(request,'accounts/forms/patient.html',context)

def delete_patient(request,pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('receptionist_dashboard')

    context = {
        'item':patient
    }
    return render(request, 'accounts/forms/delete.html',context)


def create_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_dashboard')

    context = {
        'form':form
    }
    return render(request,'accounts/forms/patient.html',context)

def update_doctor(request,pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('hr_dashboard')

    context = {
        'form':form
    }
    return render(request,'accounts/forms/patient.html',context)

def delete_doctor(request,pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('hr_dashboard')

    context = {
        'item':doctor
    }
    return render(request, 'accounts/forms/delete_doctor.html',context)

def hr_accounting(request):
    patient_outstandings = Patient_Outstandings.objects.all()
    doctor_outstandings = Doctor_Outstandings.objects.all()
    context = {
        'patient_outstandings':patient_outstandings,
        'doctor_outstandings':doctor_outstandings,
    }
    return render(request,'accounts/hr/accounting.html',context)

def user_profile(request):
    form = PatientForm()
    user = Patient.objects.filter(user=request.user)
    context = {
        'form':form,
        'user':user,
    }

    if request.method == 'POST':
        form = PatientForm(request.POST)
        form.save()
        return redirect('home')

    return render(request,'accounts/patient/profile.html',context)
