#from django.shortcuts import render

# Create your views here.
#created while trying to sync gsheets
'''
from django.http import JsonResponse
from .models import student  # Import your student model

def sync_google_sheets(request):
    # Call sync_sheet() method to synchronize data
    student.sync_sheet()

    # Prepare response data
    response_data = {
        'message': 'Google Sheets synchronization initiated successfully.'
    }

    # Return JsonResponse with response data
    return JsonResponse(response_data)
'''
# views.py

from django.shortcuts import redirect
from .models import student
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
def authorize_google_sheets(request):
    # Code to initiate OAuth 2.0 flow
    # Redirect user to Google's authorization endpoint
    # Ensure proper OAuth 2.0 setup, including client ID and secret
    # Redirect URL should be set to a callback URL in your application

    # For demonstration purposes, let's assume redirecting to a placeholder URL
    return redirect('https://example.com/oauth2/authorize')
#view to read data from models
class studentList(ListView):
  model = student

#view to create data from models
class studentCreate(CreateView):
    model = student
    #template_name = "schoolapp/student_create_form.html"
    fields = ["name", "age", "address"]



class studentUpdate(UpdateView):
    model = student
    #template_name = "schoolapp/student_create_form.html"
    fields = ["name", "age", "address"]


class studentDelete(DeleteView):
        model = student