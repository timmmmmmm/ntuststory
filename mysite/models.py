from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now=True)
	family = models.IntegerField(default=0)
	education = models.IntegerField(default=0)
	friendship = models.IntegerField(default=0)
	health = models.IntegerField(default=0)
	wealth = models.IntegerField(default=50)
	love = models.IntegerField(default=0)
	class Meta:
		ordering = ["name"]
