from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from .models import *


#class UserCreateForm(UserCreationForm):
    #class Meta:
        #fields = ("username","email","password1","password2")
        #model = get_user_model()

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.fields["username"].label = "Display name"
        #self.fields["email"].label = "Email address"

#Create your forms here

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError("the given email is already registered")
		return self.cleaned_data['email']

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	#def save(self, commit=True):
		#user = super(NewUserForm, self).save(commit=False)
		#user.email = self.cleaned_data['email']
		#if commit:
			#user.save()
		#return user



class ProductForm(forms.ModelForm):
    Total_Produced = forms.CharField()
    def get_Total_Produced(self, obj):
        return obj.get_tottal_produced()

    class Meta:
        model = Product
        fields = ("Product","Total_Produced","Sales","Category")


class Rocky_RailwayForm(forms.ModelForm):
    class Meta:
        model = Rocky_Railway
        fields = ("Product","Total_Produced","Sales")

class RoarForm(forms.ModelForm):
    class Meta:
        model = Roar
        fields = ("Product","Total_Produced","Sales")

class ShipwrechedForm(forms.ModelForm):
    class Meta:
        model = Shipwreched
        fields = ("Product","Total_Produced","Sales")

class FWN1Form(forms.ModelForm):
    class Meta:
        model = FWN1
        fields = ("Product","Total_Produced","Sales")

class FWN2Form(forms.ModelForm):
    class Meta:
        model = FWN2
        fields = ("Product","Total_Produced","Sales")

class FWN3Form(forms.ModelForm):
    class Meta:
        model = FWN3
        fields = ("Product","Total_Produced","Sales")

class LIFE_OF_JESUSForm(forms.ModelForm):
    class Meta:
        model = LIFE_OF_JESUS
        fields = ("Product","Total_Produced","Sales")

class Friends_with_God_Bible_StoryForm(forms.ModelForm):
    class Meta:
        model = Friends_with_God_Bible_Story
        fields = ("Product","Total_Produced","Sales")
