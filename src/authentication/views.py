from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import RegistrationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login') 
        else:
            messages.error(request, 'Error creating account. Please check the details and try again.')
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    return render(request, 'directory/registration.html', context)

def login_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            msg = f"Welcome Back! You have successfully logged in as {request.user.username}."
            messages.success(request, msg)
            return redirect('crob-home') 
        else:
            msg = "Username or password is incorrect."
            messages.error(request, msg)
            return redirect('login') 
    else:
        return render(request, 'crob/index.html')

def logout_user(request):
	logout(request)
	return redirect('crob-home')
