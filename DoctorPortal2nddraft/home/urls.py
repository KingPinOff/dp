from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("", views.index,name='home'),
    path("pat_login/", views.pat_login,name='patient_login'),
    path("doc_login/", views.doc_login,name='doc_login'),
    path("pat_newreg/", views.pat_newreg,name='pat_newreg'),
    path("doc_newreg/", views.doc_newreg,name='doc_newreg'),
    path("doc_dashboard/", views.doc_dashboard,name='doc_dashboard'),
    path("pat_dashboard/", views.pat_dashboard,name='pat_dashboard'),
    path("pat_newevent/", views.pat_newevent,name='pat_newevent'),
]