from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team', 'fitness_level', 'created_at']
    list_filter = ['team', 'fitness_level', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'members_count', 'created_at']
    search_fields = ['name']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'activity_type', 'duration_minutes', 'calories_burned', 'distance_km', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['user_email']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'user_name', 'team', 'total_activities', 'total_calories', 'total_distance']
    list_filter = ['team']
    search_fields = ['user_name', 'user_email']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'fitness_level', 'duration_minutes', 'category']
    list_filter = ['fitness_level', 'category']
    search_fields = ['name', 'description']
    ordering = ['name']
