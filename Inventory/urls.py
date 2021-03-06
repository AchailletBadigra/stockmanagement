from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.conf.urls import url
from .views import *
from Inventory import views
from .views import index
from Inventory.views import SearchResultsView
from django.urls import path


app_name = "Inventory"

urlpatterns =[

    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name= 'logout'),
    path('register/', views.register_request, name="register"),
    path('SearchResultsView', SearchResultsView.as_view(), name='search_results'),    

    #url(r'Login/$', auth_views.LoginView.as_view(template_name="templates/registration/login.html"),name="login"),
    #url(r'Logout/$', auth_views.LogoutView.as_view(),name="logout"),
    #url(r'SignUp/$', views.SignUp.as_view(template_name = "templates/registration/signup.html"),name="signup"),

    url(r"^$", index, name="index"),
    url(r"^contenu$", contenu, name="contenu"),

    #url(r"^$", WelcomePage.as_view(template_name = "Welcome_Page.html"), name="welcomepage"),
    #path("", WelcomePage.as_view(template_name = "Welcome_Page.html"), name="welcomepage"),


    url(r"^display_Rocky_Railway$", display_Rocky_Railway, name='display_Rocky_Railway'),
    url(r"^display_Roar$", display_Roar, name='display_Roar'),
    url(r"^display_Shipwreched$", display_Shipwreched, name='display_Shipwreched'),
    url(r"^display_FWN1$", display_FWN1, name='display_FWN1'),
    url(r"^display_FWN2$", display_FWN2, name='display_FWN2'),
    url(r"^display_FWN3$", display_FWN3, name='display_FWN3'),
    url(r"^display_LIFE_OF_JESUS$", display_LIFE_OF_JESUS, name='display_LIFE_OF_JESUS'),
    url(r"^display_Friends_with_God_Bible_Story$", display_Friends_with_God_Bible_Story, name='display_Friends_with_God_Bible_Story'),

    url(r"^add_Rocky_Railway$", add_Rocky_Railway, name='add_Rocky_Railway'),
    url(r"^add_Roar$", add_Roar, name='add_Roar'),
    url(r"^add_Shipwreched$", add_Shipwreched, name='add_Shipwreched'),
    url(r"^add_FWN1$", add_FWN1, name='add_FWN1'),
    url(r"^add_FWN2$", add_FWN2, name='add_FWN2'),
    url(r"^add_FWN3$", add_FWN3, name='add_FWN3'),
    url(r"^add_LIFE_OF_JESUS$", add_LIFE_OF_JESUS, name='add_LIFE_OF_JESUS'),
    url(r"^add_Friends_with_God_Bible_Story$", add_Friends_with_God_Bible_Story, name='add_Friends_with_God_Bible_Story'),

    url(r"^edit_Rocky_Railway/(?P<pk>\d+)$", edit_Rocky_Railway, name='edit_Rocky_Railway'),
    url(r"^edit_Roar/(?P<pk>\d+)$", edit_Roar, name='edit_Roar'),
    url(r"^edit_Shipwreched/(?P<pk>\d+)$", edit_Shipwreched, name='edit_Shipwreched'),
    url(r"^edit_FWN1/(?P<pk>\d+)$", edit_FWN1, name='edit_FWN1'),
    url(r"^edit_FWN2/(?P<pk>\d+)$", edit_FWN2, name='edit_FWN2'),
    url(r"^edit_FWN3/(?P<pk>\d+)$", edit_FWN3, name='edit_FWN3'),
    url(r"^edit_LIFE_OF_JESUS/(?P<pk>\d+)$", edit_LIFE_OF_JESUS, name='edit_LIFE_OF_JESUS'),
    url(r"^edit_Friends_with_God_Bible_Story/(?P<pk>\d+)$", edit_Friends_with_God_Bible_Story, name='edit_Friends_with_God_Bible_Story'),

    url(r"^delete_Rocky_Railway/(?P<pk>\d+)$", delete_Rocky_Railway, name='delete_Rocky_Railway'),
    url(r"^delete_Roar/(?P<pk>\d+)$", delete_Roar, name='delete_Roar'),
    url(r"^delete_Shipwreched/(?P<pk>\d+)$", delete_Shipwreched, name='delete_Shipwreched'),
    url(r"^delete_FWN1/(?P<pk>\d+)$", delete_FWN1, name='delete_FWN1'),
    url(r"^delete_FWN2/(?P<pk>\d+)$", delete_FWN2, name='delete_FWN2'),
    url(r"^delete_FWN3/(?P<pk>\d+)$", delete_FWN3, name='delete_FWN3'),
    url(r"^delete_LIFE_OF_JESUS/(?P<pk>\d+)$", delete_LIFE_OF_JESUS, name='delete_LIFE_OF_JESUS'),
    url(r"^delete_Friends_with_God_Bible_Story/(?P<pk>\d+)$", delete_Friends_with_God_Bible_Story, name='delete_Friends_with_God_Bible_Story'),
]
