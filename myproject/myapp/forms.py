from django import forms
from .models import Listing
from django.http import JsonResponse
import json


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['created_by', 'created_at']
    
    def clean_amenities(self):
        amenities = self.cleaned_data.get('amenities')
        if amenities and isinstance(amenities, str):
            try:
                # Convert amenities to list if it's a JSON string
                amenities = json.loads(amenities)
            except ValueError:
                raise forms.ValidationError("Enter a valid JSON.")
        return amenities