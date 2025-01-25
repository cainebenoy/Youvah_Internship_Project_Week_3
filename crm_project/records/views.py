from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Record
from .forms import RecordForm

def index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records})


def add_record(request):
    if request.user.is_authenticated:  # Ensure the user is logged in
        form = RecordForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect('index')  # Redirect to the homepage after adding a record
        return render(request, 'records/add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('index')