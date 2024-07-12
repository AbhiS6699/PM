"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path
from myapp.views import user_login
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from myapp.views import gallery  # Make sure to import the gallery view
from myapp import views
from myapp.views import listings_view, properties_view

 # Ensure this import is correct





pages = {

  "gst": "gst.html",
  "incoroporation-c": "incoroporation-c.html",
  "index": "index.html",
  "login": "login.html",
  "our-team": "our-team.html",
  "pan": "pan.html",
  "password_reset": "password_reset.html",
  "press&news": "press&news.html",
  "project-gallery": "project-gallery.html",
  "property_detail": "property_detail.html",
  "rera-registration": "rera-registration.html",
  "signup": "signup.html",
  "team-gallery": "team-gallery.html",
  "verify_otp": "verify_otp.html",
  "video": "video.html",
  "test": "test.html",
  "post_property": "post_property.html",
  "about-us": "about-us.html",
  "404": "404.html",
  "listing_detail": "listing_detail.html",
  "career": "career.html"
}


    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexPage, name='index'),
    path('login/', user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', views.PasswordReset, name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.logout_view, name='logout'),
    path('project-gallery/', gallery, name='project-gallery'),
    path('save_contact/', views.save_contact_details, name='save_contact'),
    path('save_requirement/', views.save_requirement_details, name='save_requirement'),
    path('press&news/', views.press, name='press&news'),
    path('post-listing/', views.post_listing, name='post_listing'),
    path('listings/', listings_view, name='listings_view'),
    path('properties/', properties_view, name='properties_view'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('index/',views.IndexPage, name='index'),  # Correct URL pattern
    path('search/', views.search, name='search'),  # Make sure this URL is correctly defined
    path('property-details/<int:property_id>/', views.property_detail, name='property_detail'),

    
    
]

urlpatterns += [path(f'{name}/', TemplateView.as_view(template_name=template), name=name) for name, template in pages.items()]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
