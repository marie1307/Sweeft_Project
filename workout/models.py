from django.db import models
from django.contrib.auth.models import User

# Exercises
class Exercise(models.Model):
    DIFFICULTY_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    TITLE_CHOICES =[
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
    ]
    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_LEVEL_CHOICES)
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=200)
    equipment_required = models.CharField(max_length=200)
    image = models.ImageField(upload_to='exercise_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# General Personal Plan
class PersonalPlan(models.Model):
    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_plans')
    plan_name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    goals = models.TextField()
    exercises = models.ManyToManyField(Exercise, through='PersonalPlanExercise')
    session_duration = models.IntegerField(default=30)  # in minutes
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.plan_name} - {self.user.username}"

# Personal plan per exercises / intermediary database between PersonalPlan model and User model
class PersonalPlanExercise(models.Model):
    personal_plan = models.ForeignKey(PersonalPlan, on_delete=models.CASCADE, related_name='plan_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise_plans')
    repetitions = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)  # in minutes
    distance = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # in kilometers

    def __str__(self):
        return f"{self.exercise.title} - {self.personal_plan.plan_name}"

class PersonalGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    goal = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.goal} - {self.user.username}"
