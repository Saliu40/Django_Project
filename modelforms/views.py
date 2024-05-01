from django.shortcuts import render, HttpResponse

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def enrol(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for giving us your data")  # Redirect to a success page after successful submission
    else:
        form = MyModelForm()
    return render(request, 'modelforms/enrol.html', {'form': form})

def success(request):
    return render(request, 'modelforms/success.html')
