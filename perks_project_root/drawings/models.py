from django.db import models


class User(models.Model):
	first_name = models.CharField(max_length=75)
	last_name = models.CharField(max_length=75)
	email = models.EmailField(max_length=254)
	admin = models.NullBooleanField()


class Contest(models.Model):
	user_id = models.ForeignKey('User')
	qty_winners = models.PositiveSmallIntegerField(default=1)
	run_date = models.DateTimeField(null=True)


class Win(models.Model):
	user_id = models.ForeignKey('User')
	contest_id = models.ForeignKey('Contest')
	place = models.PositiveSmallIntegerField(null=True)
