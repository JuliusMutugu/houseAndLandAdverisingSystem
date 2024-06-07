from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import House, Land, Agent
from django.contrib import messages
from external.passwordManager import Password
import hashlib

# Create your views here.

agent_id = None 

def LandingPage(request):
    return render(request, "HouseAdvertising/landingPage.html")


def logInPage(request):
    contextdictionary = {}
    if request.method == "POST":
        usrname = request.POST.get('username')
        passwd = request.POST.get('password')
        try:
            user = Agent.objects.get(username = usrname)
            # userp = Agent.objects.get(password = passwd)
            contextdictionary = {'user':user}
            urlRedirect = f'agentprofile/{user.Agent_id}'
            agent_id = user.Agent_id
            return redirect(urlRedirect)
        except:
            contextdictionary = {'user':{'message':'username and password does not match !!!'}}
    return render(request, "HouseAdvertising/login.html", context=contextdictionary)

    
def homePage(request):
    house_data = House.objects.all()
    land_data = Land.objects.all()
    contextdict = {'house_data':house_data}
    return render(request, 'HouseAdvertising/house.html',context=contextdict)


def landsPage(request):
    land_data = Land.objects.all()
    contextdict = {'land_data': land_data}
    return render(request, 'HouseAdvertising/land.html', context=contextdict)


def searchPage(request, val):
    if request.method == "POST":
        val = request.POST.get('searchValue')
        contextdict ={}
        land_search_location =Land.objects.filter(la_Location=val)
        house_search_data =House.objects.filter(hs_name=val)
        search_data = House.objects.filter(hs_Category=val)
        return(redirect(f'find/{val}'))
    return render(request, "HouseAdvertising/propertySearch.html", {"search_data":search_data})


def becomeAgent(request):
    password1 =Password(password_length=10)
    passcode = password1.generate_password()
    if request.method == 'POST':            
        agentform = Agent(request.POST)
        agentform.username = request.POST.get('username')
        agentform.password = hashlib.md5(request.POST.get('password').encode("utf8")).hexdigest()            
        agentform.national_id = request.POST.get('national_id')
        agentform.social_link = request.POST.get('link')
        agentform.phoneNumber = request.POST.get('phone_number')
        if len(request.FILES) != 0:
            agentform.agentImage = request.FILES.get('agent_image')
        messages.success(request, 'account created successfully!')
        if agent_id != None:
            agentform.Agent_id = agent_id
        agentform.save()
        return(redirect('homePage'))
    return render(request, 'HouseAdvertising/agentAdd.html', {'passcode': passcode})


def createHouse(request):
    if request.method == 'POST':
        property_form = House(request.POST)
        property_form.hs_name = request.POST.get('name')
        property_form.hs_Category = request.POST.get('category')
        property_form.hs_Location = request.POST.get('location')
        property_form.hs_Price = request.POST.get('price')
        property_form.hs_bed_rooms = request.POST.get('bed_rooms')
        property_form.hs_others = request.POST.get('more')
        property_form.hs_image = request.FILES.get('image_prop')
        property_form.save()
        messages.success(request, 'Property created successfully')
        return redirect("homePage")
    return render(request, 'HouseAdvertising/houseAdd.html')

    
def createLand(request):
    if request.method == 'POST':
        property_form = Land(request.POST)
        property_form.la_category = request.POST.get('category')
        property_form.la_Location = request.POST.get('location')
        property_form.la_Price = request.POST.get('price')
        property_form.la_width = request.POST.get('width')
        property_form.la_height = request.POST.get('length')
        property_form.land_image = request.FILES.get('image')
        property_form.save()
        messages.success(request, 'Property created successfully')
        return(redirect('landsPage'))
    return render(request, 'HouseAdvertising/landAdd.html')

def openProperty(request, id):
    singleProperty = House.objects.get(house_id=str(id))
    singlProperty = {"singleProperty": singleProperty}
    return render(request, 'HouseAdvertising/singleProperty.html', context=singlProperty)


def openPropertyLand(request, id):
    singleProperty = Land.objects.get(Land_id=str(id))
    landProperty = {"singleProperty": singleProperty}
    return render(request, 'HouseAdvertising/singlePropertyLand.html', context=landProperty)

def agentProfile(request, id_value):
    singleAgent = Agent.objects.get(Agent_id= id_value)
    return render(request, 'HouseAdvertising/profile.html', {"singleAgent": singleAgent})

def auto_password(request):
    pass