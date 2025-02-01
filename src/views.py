from django.shortcuts import render, redirect
from .forms import ApplicationForm

def apply(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'src/success.html')  # Success Page
    else:
        form = ApplicationForm()
    
    return render(request, 'src/application_form.html', {'form': form})
