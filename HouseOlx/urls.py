from django.urls import path
from .views import homePage, landsPage, searchPage, becomeAgent, LandingPage, openPropertyLand, agentProfile
from .views import openProperty as singleProperty
from .views import createHouse as addHouse
from .views import createLand as addLand
from .views import logInPage
urlpatterns = [
    path("", LandingPage, name= "landingpage"),
    path('home', homePage, name='homePage'),
    path('land', landsPage, name = "landsPage"),
    path('find/<str:val>',searchPage, name="searchPage" ),
    path("add", becomeAgent, name="becomeAgent"),
    path('add_house', addHouse, name="addHouse"),
    path('add_land', addLand, name="addLand"),
    path('home/<int:id>', singleProperty, name="singleProperty"),
    path('land/<int:id>', openPropertyLand, name="openLand"),
    path("agentprofile/<str:id_value>", agentProfile, name= "agentProfileView"),
    path('login', logInPage, name="loginPage"),
    


   
]
