# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate

                                         
def index(request):

    if request.method == 'POST':
        #form = Top_List_Form(request.POST)
        return HttpResponse("Do something") # methods must return HttpResponse
    


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            # Try to load JSON data from request body
            data = json.loads(request.body)
        except json.JSONDecodeError:
            # If error, return a response with status 400 (Bad Request)
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        # Extract username and password from data
        username = data.get('userName')
        password = data.get('password')

        # Check if username and password are not None
        if username is not None and password is not None:
            # Log the received username and password
            logger.info(f"Received username: {username}")
            logger.info(f"Received password: {password}")

            # Try to check if provided credential can be authenticated
            user = authenticate(username=username, password=password)
            if user is not None:
                # If user is valid, call login method to login current user
                login(request, user)
                data = {"userName": username, "status": "Authenticated"}
                return JsonResponse(data)
            else:
                # Log a message if authentication failed
                logger.warning(f"Authentication failed for username: {username}")
                data = {"status": "Failed", "message": "Invalid username or password"}
                return JsonResponse(data, status=401)
        else:
            # If either username or password is None, return a response with status 400
            return JsonResponse({'error': 'Missing username or password'}, status=400)
    else:
        # If request method is not POST, return a response with status 405 (Method Not Allowed)
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to 'home' page
# Redirect to 'home' page


# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...
@csrf_exempt
def registration(request):
    context = {}

    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
