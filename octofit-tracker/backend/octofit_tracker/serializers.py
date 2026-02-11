from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'fitness_level', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    member_count = serializers.IntegerField(source='members_count', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members_count', 'member_count']
    
    def get_id(self, obj):
        return str(obj._id)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'activity_type', 'duration_minutes', 'calories_burned', 'distance_km', 'date', 'notes']
    
    def get_id(self, obj):
        return str(obj._id)


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    # Add aliases for frontend compatibility
    total_points = serializers.IntegerField(source='total_calories', read_only=True)
    points = serializers.IntegerField(source='total_calories', read_only=True)
    activities_count = serializers.IntegerField(source='total_activities', read_only=True)
    activity_count = serializers.IntegerField(source='total_activities', read_only=True)
    name = serializers.CharField(source='user_name', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_email', 'user_name', 'name', 'team', 'total_activities', 'activities_count', 
                  'activity_count', 'total_calories', 'total_points', 'points', 'total_distance', 'rank']
    
    def get_id(self, obj):
        return str(obj._id)


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'fitness_level', 'duration_minutes', 'category', 'exercises']
    
    def get_id(self, obj):
        return str(obj._id)
