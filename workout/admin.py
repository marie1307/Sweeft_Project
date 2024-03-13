from django.contrib import admin
from .models import Exercise, PersonalPlan, PersonalPlanExercise, PersonalGoal, CompletedWorkout, ExerciseFeedback, WorkoutSession

admin.site.register(Exercise)
admin.site.register(PersonalPlan)
admin.site.register(PersonalPlanExercise)
admin.site.register(PersonalGoal)
admin.site.register(CompletedWorkout)
admin.site.register(ExerciseFeedback)
admin.site.register(WorkoutSession)
