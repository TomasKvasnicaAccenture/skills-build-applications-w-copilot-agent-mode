from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import uuid

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data (workaround for Djongo unhashable error)
        for model in [User, Team, Activity, Leaderboard, Workout]:
            model.objects.all().delete()

        # Create teams
        marvel_id = str(uuid.uuid4())[:24]
        dc_id = str(uuid.uuid4())[:24]
        marvel = Team.objects.create(team_id=marvel_id, name='Marvel')
        dc = Team.objects.create(team_id=dc_id, name='DC')

        # Create users
        ironman_id = str(uuid.uuid4())[:24]
        captain_id = str(uuid.uuid4())[:24]
        batman_id = str(uuid.uuid4())[:24]
        superman_id = str(uuid.uuid4())[:24]
        ironman = User.objects.create(user_id=ironman_id, name='Iron Man', email='ironman@marvel.com', team_id=marvel_id)
        captain = User.objects.create(user_id=captain_id, name='Captain America', email='cap@marvel.com', team_id=marvel_id)
        batman = User.objects.create(user_id=batman_id, name='Batman', email='batman@dc.com', team_id=dc_id)
        superman = User.objects.create(user_id=superman_id, name='Superman', email='superman@dc.com', team_id=dc_id)

        # Create activities
        Activity.objects.create(activity_id=str(uuid.uuid4())[:24], user_id=ironman_id, type='Running', duration=30)
        Activity.objects.create(activity_id=str(uuid.uuid4())[:24], user_id=captain_id, type='Cycling', duration=45)
        Activity.objects.create(activity_id=str(uuid.uuid4())[:24], user_id=batman_id, type='Swimming', duration=60)
        Activity.objects.create(activity_id=str(uuid.uuid4())[:24], user_id=superman_id, type='Yoga', duration=20)

        # Create workouts
        Workout.objects.create(workout_id=str(uuid.uuid4())[:24], name='Morning Cardio', description='Cardio for all heroes')
        Workout.objects.create(workout_id=str(uuid.uuid4())[:24], name='Strength Training', description='Strength for all heroes')

        # Create leaderboard
        Leaderboard.objects.create(leaderboard_id=str(uuid.uuid4())[:24], user_id=ironman_id, points=100)
        Leaderboard.objects.create(leaderboard_id=str(uuid.uuid4())[:24], user_id=captain_id, points=90)
        Leaderboard.objects.create(leaderboard_id=str(uuid.uuid4())[:24], user_id=batman_id, points=95)
        Leaderboard.objects.create(leaderboard_id=str(uuid.uuid4())[:24], user_id=superman_id, points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
