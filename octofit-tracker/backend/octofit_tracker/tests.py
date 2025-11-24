from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(team_id='t1', name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(team_id='t2', name='Test Team')
        user = User.objects.create(user_id='u1', name='Test User', email='test@example.com', team_id=team.team_id)
        self.assertEqual(user.name, 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(team_id='t3', name='Test Team')
        user = User.objects.create(user_id='u2', name='Test User', email='test2@example.com', team_id=team.team_id)
        activity = Activity.objects.create(activity_id='a1', user_id=user.user_id, type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(workout_id='w1', name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(team_id='t4', name='Test Team')
        user = User.objects.create(user_id='u3', name='Test User', email='test3@example.com', team_id=team.team_id)
        leaderboard = Leaderboard.objects.create(leaderboard_id='l1', user_id=user.user_id, points=100)
        self.assertEqual(leaderboard.points, 100)
