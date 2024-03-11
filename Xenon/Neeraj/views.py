from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ContactForm

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contact') 
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})





def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the contact page with a success message
            return render(request, 'contact.html', {'success_message': 'Your message has been sent successfully.'})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
