from django.shortcuts import render, redirect
from .forms import UserRegisterForm #creates html from form
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request): #create a form that will be a template
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() #saves user
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been created! You are now able to log in.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile (request):
	return render(request, 'users/profile.html')
