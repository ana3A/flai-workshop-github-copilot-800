from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model."""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            team="Test Team",
            fitness_level="Intermediate"
        )
    
    def test_user_creation(self):
        """Test user is created correctly."""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for Team model."""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team",
            members_count=5
        )
    
    def test_team_creation(self):
        """Test team is created correctly."""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.members_count, 5)
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for Activity model."""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="test@example.com",
            activity_type="Running",
            duration_minutes=30,
            calories_burned=300,
            distance_km=5.0,
            date=datetime.now(),
            notes="Morning run"
        )
    
    def test_activity_creation(self):
        """Test activity is created correctly."""
        self.assertEqual(self.activity.user_email, "test@example.com")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration_minutes, 30)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints."""
    
    def setUp(self):
        self.user = User.objects.create(
            name="API Test User",
            email="apitest@example.com",
            team="API Team",
            fitness_level="Beginner"
        )
    
    def test_get_users_list(self):
        """Test retrieving list of users."""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        """Test creating a new user."""
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'team': 'New Team',
            'fitness_level': 'Advanced'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints."""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="API Test Team",
            description="Team for API testing",
            members_count=3
        )
    
    def test_get_teams_list(self):
        """Test retrieving list of teams."""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        """Test creating a new team."""
        data = {
            'name': 'New Team',
            'description': 'A brand new team',
            'members_count': 0
        }
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints."""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="activity@example.com",
            activity_type="Swimming",
            duration_minutes=45,
            calories_burned=400,
            distance_km=2.0,
            date=datetime.now()
        )
    
    def test_get_activities_list(self):
        """Test retrieving list of activities."""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_activity(self):
        """Test creating a new activity."""
        data = {
            'user_email': 'newactivity@example.com',
            'activity_type': 'Cycling',
            'duration_minutes': 60,
            'calories_burned': 500,
            'distance_km': 15.0,
            'date': datetime.now().isoformat()
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints."""
    
    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            user_email="leader@example.com",
            user_name="Leader User",
            team="Leader Team",
            total_activities=10,
            total_calories=5000,
            total_distance=50.0,
            rank=1
        )
    
    def test_get_leaderboard(self):
        """Test retrieving leaderboard."""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints."""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Test Workout",
            description="A test workout routine",
            fitness_level="Intermediate",
            duration_minutes=30,
            category="Cardio",
            exercises={"exercises": ["push-ups", "squats"]}
        )
    
    def test_get_workouts_list(self):
        """Test retrieving list of workouts."""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_workout(self):
        """Test creating a new workout."""
        data = {
            'name': 'New Workout',
            'description': 'A new workout routine',
            'fitness_level': 'Beginner',
            'duration_minutes': 20,
            'category': 'Strength',
            'exercises': {"exercises": ["planks", "lunges"]}
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
