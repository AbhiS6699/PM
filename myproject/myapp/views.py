from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth import logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import random
from django.conf import settings
from django.db.models import Q
from .models import Project
import os
from django.http import HttpRequest
import csv
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Amenity, HomeLoanOffer, CustomerReview, Property, PropertyImage, Press, PressImage
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm
from django.contrib.auth.decorators import login_required




def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    images = PropertyImage.objects.filter(property=property)
    amenities = Amenity.objects.filter(property=property)
    loan_offers = HomeLoanOffer.objects.filter(property=property)
    reviews = CustomerReview.objects.filter(property=property)

    context = {
        'property': property,
        'images': images,
        'amenities': amenities,
        'loan_offers': loan_offers,
        'reviews': reviews,
    }
    return render(request, 'property_detail.html', context)
    


def gallery(request):
    projects = Project.objects.all()  # Fetching all projects from the database
    return render(request, 'project-gallery.html', {'projects': projects})





def IndexPage(request):
    properties = Property.objects.all()
    listings = Listing.objects.all()
    return render(request, 'index.html', {'listings': listings, 'properties': properties})

def PasswordReset(request):

    return render (request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        login_input = request.POST.get('username') # 'username' field can be either username or email
        password = request.POST.get('password')
        
        # Helper function to check if the input is an email
        def is_email(input):
            try:
                validate_email(input)
                return True
            except ValidationError:
                return False

        # Determine if user is logging in with email or username
        if is_email(login_input):
            user = authenticate(request, email=login_input, password=password)
        else:
            user = authenticate(request, username=login_input, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('index'))  # Assuming 'index' is the correct route name
        else:
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'login.html')

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})


@login_required
def profile_view(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Log the user in
                return redirect(reverse('login'))  # Redirect to the home page or dashboard
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
    else:
        return render(request, 'signup.html')  # Ensure you have a template named signup.html


# In the view that renders the template with the {% url %} ta

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the home page after logout



def press(request):
    press = Press.objects.all()  # Fetching all projects from the database
    return render(request, 'press&news.html', {'press': press})

def search(request):
    query = request.GET.get('q', '').lower()
    predefined_keywords = {
        "plots in Indore": "/listings/?type=plot&location=Indore",
        "residential plots": "/listings/?type=plot&category=residential",
        "commercial plots": "/listings/?type=plot&category=commercial",
        "property in Indore": "/properties/?location=Indore",
        "plots": "/listings/?type=plot",
        "property": "/properties/",
        "home in indore": "/properties/?type=home&location=Indore",
        "house in indore": "/properties/?type=house&location=Indore"
    }

    results = []

    if query:
        # Search within the database
        properties = Property.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(price_range__icontains=query) |
            Q(location__icontains=query) |
            Q(builder_name__icontains=query) |
            Q(property_type__icontains=query) |
            Q(project_size__icontains=query) |
            Q(project_type__icontains=query) |
            Q(plot_size__icontains=query) |
            Q(project_status__icontains=query) |
            Q(rera_registraion__icontains=query)
        ).distinct()

        results = [{'name': prop.name, 'url': f'/property-details/{prop.id}', 'image': prop.image.url if prop.image else None} for prop in properties]

        # Include predefined keywords if they match the query
        for keyword, url in predefined_keywords.items():
            if query in keyword.lower():
                results.append({'name': keyword, 'url': url})

    return JsonResponse(results, safe=False)

def listings_view(request):
    listing_type = request.GET.get('type')
    location = request.GET.get('location')
    category = request.GET.get('category')

    filters = {}
    if listing_type:
        filters['listing_type'] = listing_type
    if location:
        filters['location__icontains'] = location
    if category:
        filters['plot_type__icontains'] = category

    listings = Listing.objects.filter(**filters)
    return render(request, 'listings.html', {'listings': listings})

def properties_view(request):
    property_type = request.GET.get('type')
    location = request.GET.get('location')

    filters = {}
    if property_type:
        filters['property_type__icontains'] = property_type
    if location:
        filters['location__icontains'] = location

    properties = Property.objects.filter(**filters)
    return render(request, 'properties.html', {'properties': properties})


def post_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user
            listing.save()
            return redirect('index')  # Redirect to the index page after submission
        else:
            print(form.errors)  # Print form errors if the form is not valid
    else:
        form = ListingForm()
    return render(request, 'post_property.html', {'form': form})

def save_contact_details(request):
    if request.method == 'POST':
        name = request.POST.get('contactName')
        email = request.POST.get('contactEmail')
        contact_number = request.POST.get('contactNumber')
        message = request.POST.get('contactMessage')

        print(f"Received data: Name={name}, Email={email}, Contact Number={contact_number}, Message={message}")

        media_root = settings.MEDIA_ROOT
        file_path = os.path.join(media_root, 'contact_details.csv')

        # Check if media directory exists, if not, create it
        if not os.path.exists(media_root):
            try:
                os.makedirs(media_root)
                print(f"Created media directory at: {media_root}")
            except Exception as e:
                print(f"Error creating media directory: {e}")
                return JsonResponse({'status': 'fail', 'error': 'Error creating media directory'})

        # Write the data to the CSV file
        try:
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, email, contact_number, message])
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error writing to file: {e}")
            return JsonResponse({'status': 'fail', 'error': 'Error writing to file'})

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'})

def save_requirement_details(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        contact_number = request.POST.get('number')
        email = request.POST.get('email')
        requirement = request.POST.get('requirement')

        print(f"Received data: Full Name={full_name}, Contact Number={contact_number}, Email={email}, Requirement={requirement}")

        media_root = settings.MEDIA_ROOT
        csv_folder = os.path.join(media_root, 'requirement_details')
        file_path = os.path.join(csv_folder, 'requirement_details.csv')

        if not os.path.exists(csv_folder):
            try:
                os.makedirs(csv_folder)
                print(f"Created directory at: {csv_folder}")
            except Exception as e:
                print(f"Error creating directory: {e}")
                return JsonResponse({'status': 'fail', 'error': 'Error creating directory'})

        try:
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([full_name, contact_number, email, requirement])
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error writing to file: {e}")
            return JsonResponse({'status': 'fail', 'error': 'Error writing to file'})

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'})


