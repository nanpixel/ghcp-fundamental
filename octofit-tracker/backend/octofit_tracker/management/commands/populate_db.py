from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio endurance', difficulty='Medium'),
            Workout.objects.create(name='Deadlift', description='Full body strength', difficulty='Hard'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], workout=workouts[0], duration=30)
        Activity.objects.create(user=users[1], workout=workouts[1], duration=45)
        Activity.objects.create(user=users[2], workout=workouts[2], duration=60)
        Activity.objects.create(user=users[3], workout=workouts[0], duration=20)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=80)
        Leaderboard.objects.create(user=users[2], score=120)
        Leaderboard.objects.create(user=users[3], score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
