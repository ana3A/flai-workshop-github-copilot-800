from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create teams
        teams_data = [
            {
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes unite for fitness!',
                'members_count': 6
            },
            {
                'name': 'Team DC',
                'description': 'Justice League assembles for peak performance!',
                'members_count': 6
            }
        ]
        
        for team_data in teams_data:
            Team.objects.create(**team_data)
        
        self.stdout.write('Creating users...')
        
        # Create users (superheroes)
        users_data = [
            # Team Marvel
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Team Marvel', 'fitness_level': 'advanced'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com', 'team': 'Team Marvel', 'fitness_level': 'expert'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team': 'Team Marvel', 'fitness_level': 'expert'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'team': 'Team Marvel', 'fitness_level': 'intermediate'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'team': 'Team Marvel', 'fitness_level': 'expert'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'team': 'Team Marvel', 'fitness_level': 'advanced'},
            
            # Team DC
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'Team DC', 'fitness_level': 'expert'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'Team DC', 'fitness_level': 'expert'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': 'Team DC', 'fitness_level': 'expert'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'team': 'Team DC', 'fitness_level': 'advanced'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'team': 'Team DC', 'fitness_level': 'advanced'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'team': 'Team DC', 'fitness_level': 'advanced'},
        ]
        
        for user_data in users_data:
            User.objects.create(**user_data)
        
        self.stdout.write('Creating activities...')
        
        # Create activities
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weight Training', 'Yoga', 'HIIT', 'Boxing', 'Martial Arts']
        
        for user_data in users_data:
            # Create 5-10 activities per user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = duration * random.randint(5, 12)
                distance = round(random.uniform(1.0, 15.0), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                
                Activity.objects.create(
                    user_email=user_data['email'],
                    activity_type=activity_type,
                    duration_minutes=duration,
                    calories_burned=calories,
                    distance_km=distance,
                    date=activity_date,
                    notes=f"{activity_type} session - {user_data['name']}"
                )
        
        self.stdout.write('Creating leaderboard entries...')
        
        # Create leaderboard entries
        for user_data in users_data:
            activities = Activity.objects.filter(user_email=user_data['email'])
            total_activities = activities.count()
            total_calories = sum(a.calories_burned for a in activities)
            total_distance = sum(a.distance_km for a in activities if a.distance_km)
            
            Leaderboard.objects.create(
                user_email=user_data['email'],
                user_name=user_data['name'],
                team=user_data['team'],
                total_activities=total_activities,
                total_calories=total_calories,
                total_distance=round(total_distance, 2)
            )
        
        # Update ranks based on total calories
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write('Creating workouts...')
        
        # Create workouts
        workouts_data = [
            {
                'name': 'Hero Training Basics',
                'description': 'Essential exercises for beginners starting their hero journey',
                'fitness_level': 'beginner',
                'duration_minutes': 30,
                'category': 'Strength',
                'exercises': [
                    {'name': 'Push-ups', 'sets': 3, 'reps': 10},
                    {'name': 'Squats', 'sets': 3, 'reps': 15},
                    {'name': 'Plank', 'sets': 3, 'duration_seconds': 30}
                ]
            },
            {
                'name': 'Avenger Cardio Blast',
                'description': 'High-intensity cardio to match the Avengers',
                'fitness_level': 'intermediate',
                'duration_minutes': 45,
                'category': 'Cardio',
                'exercises': [
                    {'name': 'Burpees', 'sets': 4, 'reps': 15},
                    {'name': 'Mountain Climbers', 'sets': 4, 'reps': 20},
                    {'name': 'Jump Squats', 'sets': 4, 'reps': 15}
                ]
            },
            {
                'name': 'Superman Strength',
                'description': 'Advanced strength training fit for the Man of Steel',
                'fitness_level': 'advanced',
                'duration_minutes': 60,
                'category': 'Strength',
                'exercises': [
                    {'name': 'Deadlifts', 'sets': 5, 'reps': 8},
                    {'name': 'Bench Press', 'sets': 5, 'reps': 8},
                    {'name': 'Pull-ups', 'sets': 5, 'reps': 10}
                ]
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Speed and agility drills inspired by the Fastest Man Alive',
                'fitness_level': 'advanced',
                'duration_minutes': 40,
                'category': 'Agility',
                'exercises': [
                    {'name': 'Sprint Intervals', 'sets': 8, 'duration_seconds': 30},
                    {'name': 'Ladder Drills', 'sets': 5, 'reps': 10},
                    {'name': 'Box Jumps', 'sets': 4, 'reps': 12}
                ]
            },
            {
                'name': 'Wonder Woman Warrior',
                'description': 'Warrior-inspired full body workout',
                'fitness_level': 'intermediate',
                'duration_minutes': 50,
                'category': 'Full Body',
                'exercises': [
                    {'name': 'Lunges', 'sets': 4, 'reps': 12},
                    {'name': 'Push-ups', 'sets': 4, 'reps': 15},
                    {'name': 'Kettlebell Swings', 'sets': 4, 'reps': 20}
                ]
            },
            {
                'name': 'Spider-Man Mobility',
                'description': 'Flexibility and mobility for web-slinging action',
                'fitness_level': 'beginner',
                'duration_minutes': 35,
                'category': 'Flexibility',
                'exercises': [
                    {'name': 'Dynamic Stretching', 'sets': 2, 'duration_seconds': 300},
                    {'name': 'Yoga Flow', 'sets': 3, 'duration_seconds': 180},
                    {'name': 'Foam Rolling', 'sets': 1, 'duration_seconds': 600}
                ]
            }
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with superhero test data!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
