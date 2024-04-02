# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('gsheets/authorize/', views.authorize_google_sheets, name='authorize_google_sheets'),
    path("students/", views.studentList.as_view(),name="studentlist"),
    path("students/create", views.studentCreate.as_view(),name='studentcreate'),
    path("students/update", views.studentUpdate.as_view(),name='studentupdate'),
    path("students/delete", views.studentDelete.as_view(), name='studentdelete'),

]
