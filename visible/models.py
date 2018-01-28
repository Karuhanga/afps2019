from django.db import models
from django.utils.text import slugify
import datetime
from django.utils.timezone import utc

# Create your models here.
class EventInformation(models.Model):
	class Meta:
		verbose_name = "Event Information"
		verbose_name_plural = "Event Information"

	date = models.DateField()
	registration_closes = models.DateField()
	theme = models.CharField(max_length=200)
	venue = models.CharField(max_length=200)
	link_to_venue_map = models.CharField(max_length=200)
	link_to_reg_form = models.CharField(max_length=200)
	link_to_immigration_details = models.CharField(max_length=200)

	def get_event_info():
		return EventInformation.objects.all()[0]

	def get_time_to_event(self):
		now = datetime.date.today()
		diff = self.date - now
		return diff.total_seconds()//(60*60*24)

	def get_time_to_reg_end(self):
		now = datetime.date.today()
		diff = self.registration_closes - now
		return diff.total_seconds()//(60*60*24)

	def __str__(self):
		return "Event Information"

class Post(models.Model):
	"""New Article on site"""
	title = models.CharField(max_length=200, unique=True)
	pub_date = models.DateField(auto_created=True)
	too_long_to_read = models.CharField(max_length=200)
	article = models.TextField()
	image = models.ImageField(verbose_name='Image(optional)', upload_to='blog', null=True, blank=True)
	slug = models.SlugField(blank=True, unique=True)

	def get_absolute_url(self):
		return '/article/'+self.slug
		# return reverse('visible.views.article', args=[self.slug])

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		count = 1
		self.slug = slugify(self.title)
		return super(Post, self).save(*args, **kwargs)

class EventSummaryCard(models.Model):
	title = models.CharField(max_length=20, unique=True)
	words = models.TextField(max_length=500)

	def __str__(self):
		return self.title

class PreviousEdition(models.Model):
	year = models.CharField(max_length=40)
	venue = models.CharField(max_length=30)
	theme = models.CharField(max_length=60)
	link_to_details = models.CharField(max_length=100)
	image = models.ImageField(upload_to='previous_events')

	def __str__(self):
		return self.venue

class Partner(models.Model):
	name = models.CharField(max_length=50)
	about_them = models.CharField(max_length=120)
	link_to_site = models.CharField(max_length=100)
	image = models.ImageField(upload_to='partners')

class Ad(models.Model):
	content = models.CharField(max_length=60)
	image = models.ImageField(upload_to='ads')
	link_to_details = models.CharField(max_length=100)

	def get_ads():
		ads = Ad.objects.all()
		ads = list(ads)
		if not (len(ads) % 2 == 0):
			ads.pop()
		return zip(ads[::2], ads[1::2])

class Schedule(models.Model):
	title = models.CharField(max_length=30)
	short_summary = models.TextField(max_length=500)
	date = models.DateField()
	cost = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class ImmigrationGuide(models.Model):
	title = models.CharField(max_length=15)
	content = models.TextField(max_length=250)

	def __str__(self):
		return self.title

class TeamMember(models.Model):
	name = models.CharField(max_length=50)
	role = models.CharField(max_length=20)
	image = models.ImageField(upload_to='team')
	twitter_link = models.CharField(max_length=100)
	facebook_link = models.CharField(max_length=100)
	linkedIn_link = models.CharField(max_length=100)

	def __str__(self):
		return self.name
