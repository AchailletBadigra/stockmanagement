from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from Inventory import forms
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
#####################
from urllib.parse import urlparse, urlunparse

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import (
    url_has_allowed_host_and_scheme, urlsafe_base64_decode,
)
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
##################
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django import template
from django.contrib import messages #import messages
from email.message import EmailMessage
###################

# Create your views here.

#Index
def index(request):
    count = User.objects.count()
    return render(request,'index.html', {
        'count':count
    })

def contenu(request):
    return render(request,'contenu.html')


def password_reset(request):
	if request.method == "POST":
		form = PasswordReset(request.POST)
		if form.is_valid():
			data = form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data)|Q(username=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					htmltemp = template.loader.get_template('password_reset_email.html')
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					html_content = htmltemp.render(c)
					try:
						msg = EmailMultiAlternatives(subject, text_content, 'basaturninleo@gmail.com', [email])
						msg.attach_alternative(html_content, "text/html")
						msg.send()
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.info(request, "Password reset instructions have been sent to the email address entered.")
					return redirect ("index")
	form = PasswordReset()
	return render(request=request, template_name="password_reset_email.html", context={"form":form})







#Register(signup)
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("Inventory:index")
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            email = form.data['email']
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, f"Declared {email} is not valid")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, f"Selected password: {password1} is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
                    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render (request=request, template_name="register.html", context={"register_form":form})

#Login

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in")
				return redirect("Inventory:contenu")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


#Logout
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("Inventory:index")


#signup
#class SignUp(CreateView):
    #form_class = forms.UserCreateForm
    #success_url = reverse_lazy("login")
    #template_name = "register.html"

#def

def display_Rocky_Railway(request):
    items = Product.objects.filter(Category=1)
    context = {
        'items' : items,
        'header' : 'Rocky_Railway'
    }

    return render(request,'contenu.html',context)

def display_Roar(request):
    items = Product.objects.filter(Category=2)
    context = {
        'items' : items,
        'header' : 'Roar'
    }

    return render(request,'contenu.html',context)

def display_Shipwreched(request):
    items = Product.objects.filter(Category=3)
    context = {
        'items' : items,
        'header' : 'Shipwreched'
    }

    return render(request,'contenu.html',context)

def display_FWN1(request):
    items = Product.objects.filter(Category=4)
    context = {
        'items' : items,
        'header' : 'FWN1'
    }

    return render(request,'contenu.html',context)

def display_FWN2(request):
    items = Product.objects.filter(Category=5)
    context = {
        'items' : items,
        'header' : 'FWN2'
    }

    return render(request,'contenu.html',context)

def display_FWN3(request):
    items = Product.objects.filter(Category=6)
    context = {
        'items' : items,
        'header' : 'FWN3'
    }

    return render(request,'contenu.html',context)

def display_LIFE_OF_JESUS(request):
    items = Product.objects.filter(Category=7)
    context = {
        'items' : items,
        'header' : 'LIFE_OF_JESUS'
    }

    return render(request,'contenu.html',context)


def display_Friends_with_God_Bible_Story(request):
    items = Product.objects.filter(Category=10)
    context = {
        'items' : items,
        'header' : 'Friends_with_God_Bible_Story'
    }

    return render(request,'contenu.html',context)


#adding
def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')
    else:
        form = cls()
        return render(request,'add_new.html', {'form':form})


def add_Rocky_Railway(request):
        return add_device(request, ProductForm)

def add_Roar(request):
        return add_device(request, ProductForm)

def add_Shipwreched(request):
        return add_device(request, ShipwrechedForm)

def add_FWN1(request):
        return add_device(request, FWN1Form)

def add_FWN2(request):
        return add_device(request, FWN2Form)

def add_FWN3(request):
        return add_device(request, FWN3Form)

def add_LIFE_OF_JESUS(request):
        return add_device(request, LIFE_OF_JESUSForm)

def add_Friends_with_God_Bible_Story(request):
        return add_device(request, Friends_with_God_Bible_StoryForm)


#editing
def edit_Rocky_Railway(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

def edit_Roar(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

def edit_Shipwreched(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

def edit_FWN1(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

def edit_FWN2(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

def edit_FWN3(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

def edit_LIFE_OF_JESUS(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})


def edit_Friends_with_God_Bible_Story(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:contenu')

    else:
        form = ProductForm(instance=item)

        return render(request,'edit_item.html', {'form':form})

#DELETE

def delete_Rocky_Railway(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

def delete_Roar(request,pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

def delete_Shipwreched(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

def delete_FWN1(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

def delete_FWN2(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

def delete_FWN3(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

def delete_LIFE_OF_JESUS(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)


def delete_Friends_with_God_Bible_Story(request, pk):
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request,'contenu.html',context)

#class WelcomePage(TemplateView):
    #template_name = "Welcome_Page.html"

#def register(response):
    #if response.method == "POST":
        #form = UserCreateForm(response.POST)
        #if form.is_valid():
            #form.save()

        #return redirect("login_request")
    #else:
        #form = UserCreateForm()

    #return render(response, 'Inventory/register.html', {"form":form})

#search

class SearchResultsView(ListView):
    model = Product
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(Sales__icontains=query) | Q(Product__icontains=query)
            )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


#Notification to display the message to the user about his reset password sent to his email

#def homepage(request):
	#return render (request=request, template_name="index.html")
