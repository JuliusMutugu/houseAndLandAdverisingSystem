from django.db import models

house_choices = [
	('houserentals', 'rent-house'),
	('housesale', 'sell-house')
	
]
x = 0

# Create your models here
class Agent(models.Model):
	username = models.CharField(max_length=40)
	password = models.CharField(max_length = 200)
	phoneNumber = models.CharField(max_length=20)
	national_id = models.IntegerField()
	social_link = models.TextField(null=True)
	agentImage = models.ImageField(upload_to = 'agentImages/')
	Agent_id = models.AutoField(primary_key=True)
	

class House(models.Model):
	hs_name = models.CharField(max_length=200, default = 'Master en suite')
	hs_Category  = models.CharField(choices=house_choices, max_length=50)
	hs_Location = models.TextField()
	hs_Price = models.IntegerField(null=True, default =0)
	agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE, null = True)
	hs_image = models.ImageField(upload_to='properties/house')
	hs_advertising_date = models.DateTimeField(auto_now_add=True)
	hs_last_check = models.DateTimeField(auto_now=True)
	hs_bed_rooms = models.IntegerField()
	hs_others= models.TextField(null=True)
	house_id  = models.AutoField(primary_key=True )
	
	
	

class Land(models.Model):
	la_category = models.CharField(max_length=40, choices=[('landlease', 'rent-land'), ('landsell', 'sell-land')])
	la_Location = models.TextField()
	la_Price = models.IntegerField()
	land_image = models.ImageField(upload_to='properties/land')
	advertising_date = models.DateTimeField(auto_now_add=True)
	la_width = models.IntegerField()
	la_height = models.IntegerField()
	agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE, null= True)
	Land_id = models.AutoField(primary_key=True)


class property_reviews(models.Model):
	hs_id = models.ForeignKey(House, on_delete=models.CASCADE,null=True)
	la_id = models.ForeignKey(Land, on_delete=models.CASCADE,null=True)
	review = models.CharField(max_length= 20, choices=[('notsatisfactory', '1'),  ('almost_there', '2'), ('fair', '3'), ('above_average', 4), ('great', "5")])
	message = models.TextField(null=True, blank=True)


