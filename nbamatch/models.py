from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateTimeField()

	def __unicode__(self):
		return self.title

class Center(models.Model):
	player = models.CharField(max_length=200)
	pos = models.CharField(max_length=2)
	age = models.IntegerField(default=0)
	twopercent = models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrows = models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbs = models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assists = models.DecimalField(default=0, max_digits=10, decimal_places=9)
	steals = models.DecimalField(default=0, max_digits=10, decimal_places=9)
	blocks = models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrowsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assistsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	stealsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	blocksn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	def __str__(self):
		return self.player
	
class SmallForward(models.Model):
	player = models.CharField(max_length=200)
	pos = models.CharField(max_length=2)
	age= models.IntegerField(default=0)
	threepercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrows=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assists=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbs=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	steals=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	threepercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrowsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assistsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)	
	stealsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	def __str__(self):
		return self.player
	
	
   
class PowerForward(models.Model):
	player = models.CharField(max_length=200)
	pos = models.CharField(max_length=2)
	age= models.IntegerField(default=0)
	twopercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrows=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbs=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assists=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	steals=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	blocks=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrowsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assistsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	stealsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	blocksn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	def __str__(self):
		return self.player
	
class PointGuard(models.Model):
	player = models.CharField(max_length=200)
	pos = models.CharField(max_length=2)
	age= models.IntegerField(default=0)
	threepercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrows=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assists=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	steals=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbs=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	threepercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrowsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assistsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	stealsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)	
	def __str__(self):
		return self.player

class ShootingGuard(models.Model):
	player = models.CharField(max_length=200)
	pos = models.CharField(max_length=2)
	age= models.IntegerField(default=0)
	threepercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercent=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrows=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbs=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assists=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	steals=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	threepercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	twopercentn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	freethrowsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	trbsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	assistsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	stealsn=models.DecimalField(default=0, max_digits=10, decimal_places=9)
	def __str__(self):
		return self.player