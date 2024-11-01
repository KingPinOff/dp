# views.py
from django.contrib.auth.decorators import login_required
import home.firebase_setup 
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from home.backends import FirebaseBackend  
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


def index(request):
    return render(request, 'homepage/index.html')

def pat_login(request):
    return render(request, 'pat_login/index.html')

def doc_login(request):
    return render(request, 'doc_login/index.html')

def pat_newreg(request):
    return render(request, 'pat_newreg/index.html')

def doc_newreg(request):
    return render(request, 'doc_newreg/index.html')

def doc_dashboard(request):
    if not firebase_admin._apps:
        print('initializing')
        cred = credentials.Certificate("lastest.json")
        app = firebase_admin.initialize_app(cred, name='authentication_app')
        print(app.name)


    if request.method == 'POST':
        doc_email = request.POST.get('doc_email')
        doc_pw = request.POST.get('doc_pw')
        print(doc_email,doc_pw)
        user = authenticate(request, username=doc_email, password=doc_pw)
        if user is not None:
            login(request, user)
            return redirect('doc_dashboard')
        else:
            return render(request, 'doc_login/index.html', {'error': 'Invalid credentials'})
    return render(request, 'doc_dashboard/index.html')


def pat_dashboard(request):
    return render(request, 'pat_dashboard/index.html')

def pat_newevent(request):
    return render(request, 'pat_newevent/index.html')
