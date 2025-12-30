from djongo import models


class Team(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	class Meta:
		db_table = 'teams'
	def __str__(self):
		return self.name


class User(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
	class Meta:
		db_table = 'users'
	def __str__(self):
		return self.email


class Workout(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	difficulty = models.CharField(max_length=50)
	class Meta:
		db_table = 'workouts'
	def __str__(self):
		return self.name


class Activity(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='activities')
	date = models.DateTimeField(auto_now_add=True)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	class Meta:
		db_table = 'activities'
	def __str__(self):
		return f"{self.user.email} - {self.workout.name}"


class Leaderboard(models.Model):
	id = models.ObjectIdField(primary_key=True, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
	score = models.IntegerField(default=0)
	class Meta:
		db_table = 'leaderboard'
	def __str__(self):
		return f"{self.user.email} - {self.score}"
