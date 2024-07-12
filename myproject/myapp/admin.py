from django.contrib import admin
from .models import Property 
from .models import Project, ProjectImage, Press, PressImage
from .models import Amenity, HomeLoanOffer, CustomerReview, PropertyImage, Listing







class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
    ]

class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1

class HomeLoanOfferInline(admin.TabularInline):
    model = HomeLoanOffer
    extra = 1

class CustomerReviewInline(admin.TabularInline):
    model = CustomerReview
    extra = 1

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # The number of empty forms to display


class PressImageInline(admin.TabularInline):
    model = PressImage
    extra = 1  # The number of empty forms to display

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'location', 'expected_price', 'created_at')
    search_fields = ('project_name', 'location')





class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_range', 'builder_name', 'location')
    search_fields = ('name', 'builder_name')
    inlines = [AmenityInline, HomeLoanOfferInline, CustomerReviewInline, PropertyImageInline]

class PressAdmin(admin.ModelAdmin):
    inlines = [PressImageInline,]




admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Press, PressAdmin)




# Register your models here.
