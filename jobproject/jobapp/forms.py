from django import forms
from .models import (User, UserProfile, ManagerProfile, JobApplication, Review)

#CUSTOMER MODELS
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('phone', 'profile_pic')

class JobApplicationForm(forms.ModelForm):
    class Meta():
        model = JobApplication
        fields = ('username', 'job_role', 'work_experience', 'skills', 'job_type', 'resume')

#ROOM MANAGER MODELS
class ManagerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class ManagerProfileForm(forms.ModelForm):
    class Meta():
        model = ManagerProfile
        fields = ('mgr_id', 'specification')

class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = ('job_role', 'job_description')
