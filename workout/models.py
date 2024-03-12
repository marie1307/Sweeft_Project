from django.db import models
from django.contrib.auth.models import User

# Exercises
class Exercise(models.Model):
    difficulty_level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    title = models.CharField(max_length=100, choices=[
        ('Push-ups', 'Push-ups'),
        ('Pull-ups', 'Pull-ups'),
        ('Squats', 'Squats'),
        ('Deadlifts', 'Deadlifts'),
        ('Bench Press', 'Bench Press'),
        ('Dumbbell Rows', 'Dumbbell Rows'),
        ('Burpees', 'Burpees'),
        ('Jumping Jacks', 'Jumping Jacks'),
        ('Plank', 'Plank'),
        ('Russian Twists', 'Russian Twists'),
        ('Mountain Climbers', 'Mountain Climbers'),
        ('Lunges', 'Lunges'),
        ('Leg Press', 'Leg Press'),
        ('Calf Raises', 'Calf Raises'),
        ('Leg Curls', 'Leg Curls'),
        ('Lat Pulldowns', 'Lat Pulldowns'),
        ('Tricep Dips', 'Tricep Dips'),
        ('Bicep Curls', 'Bicep Curls'),
        ('Shoulder Press', 'Shoulder Press'),
    ])
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=200)
    equipment_required = models.CharField(max_length=200)
    image = models.ImageField(upload_to='exercise_images/', null=True, blank=True)

    def __str__(self):
        return self.title

# General Personal Plan
class PersonalPlan(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50, choices=[
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ])
    goals = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='PersonalPlanExercise')
    session_duration = models.IntegerField(default=30)  # in minutes
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user_name

# Personal plan per exercises / intermediary database between PersonalPlan model and User model
class PersonalPlanExercise(models.Model):
    personal_plan = models.ForeignKey(PersonalPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)  # in minutes
    distance = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # in kilometers

    def __str__(self):
        return f"{self.exercise} - {self.personal_plan}"

class PersonalGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return self.goal
