from djongo import models

class Team(models.Model):
    team_id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    user_id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24)

class Activity(models.Model):
    activity_id = models.CharField(max_length=24, primary_key=True)
    user_id = models.CharField(max_length=24)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Workout(models.Model):
    workout_id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=24, primary_key=True)
    user_id = models.CharField(max_length=24)
    points = models.IntegerField()
