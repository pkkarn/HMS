from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('login/', views.loginuser, name="loginuser"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('user/appointments/', views.user_appointments, name="user_appointments"),
    path('user/iop/', views.user_invoice, name="user_invoice"),
    path('user/profile/', views.user_profile, name="user_profile"),
    path('user/history/', views.user_medical_history, name="user_medical_history"),
    path('doctor/profile/', views.doctor_profile, name="doctor_profile"),
    path('doctor/appointments/', views.doctor_appointments, name="doctor_appointments"),
    path('doctor/prescription/', views.doctor_prescription, name="doctor_prescription"),
    path('receptionist/dashboard/', views.receptionist_dashboard, name="receptionist_dashboard"),
    path('HR/dashboard/', views.hr_dashboard, name="hr_dashboard"),
    path('HR/accounting/', views.hr_accounting, name="hr_accounting"),
    path('create_appointment/', views.create_appointment, name="create_appointment"),
    path('create_patient/', views.create_patient, name="create_patient"),
    path('update_patient/<int:pk>/', views.update_patient, name="update_patient"),
    path('delete_patient/<int:pk>/', views.delete_patient, name="delete_patient"),
    path('create_doctor/', views.create_doctor, name="create_doctor"),
    path('update_doctor/<int:pk>/', views.update_doctor, name="update_doctor"),
    path('delete_doctor/<int:pk>/', views.delete_doctor, name="delete_doctor"),
]
