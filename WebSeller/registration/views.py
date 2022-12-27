from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


# View for handling user registration
def register(request):
    # Initialize a message to be displayed in case of errors
    msg = None
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with the data from the request
        form = RegistrationForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Get the cleaned data from the form
            data = form.cleaned_data
            # Create a new user with the provided data
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
            )
            # Save the new user
            user.save()
            # Authenticate and log in the new user
            user = authenticate(
                request, username=data['username'], password=data['password'])
            login(request, user)
            # Set the success message
            messages = 'Registration successful!'
            # Redirect the user to the products page
            return HttpResponseRedirect(reverse('myapp:products'), {'msg': msg})
        else:
            # Set the error message if the form is invalid
            msg = 'This Username have been taken, please try another one!'
    else:
        # Create an empty form instance if the request method is not POST
        form = RegistrationForm()
    # Render the registration template with the form and message
    return render(request, 'registration/register.html', {'form': form, 'msg': msg})


def user_login(request):
    # Initialize message to display in case of errors
    msg = None
    # If the request method is POST, a form submission has been made
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = LoginForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Retrieve the cleaned form data
            data = form.cleaned_data
            # Authenticate the user with the form data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                # If the user is authenticated, log them in and redirect to the 'products' page
                login(request, user)
                msg = 'Register Success'
                return HttpResponseRedirect('product.html')
            # else:
            #     # If the user is not authenticated, set the message to display
            #     msg = 'Invalid login credentials.'
        else:
            msg = 'Invalid login form data.'
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
