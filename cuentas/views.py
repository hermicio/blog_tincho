from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def logup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuentas:login')
    else:
        form = UserCreationForm()
    return render(request,'cuentas/logup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('articulos:lista')
    else:
        form = AuthenticationForm()
    return render(request,'cuentas/login.html', {'form':form})