from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExercisesViewSet, PersonalPlanViewSet, PersonalPlanExerciseViewSet, PersonalGoalViewSet, ExerciseFeedbackViewSet, CompletedWorkoutViewSet, WorkoutSessionViewSet


router = DefaultRouter()
router.register(r'exercises', ExercisesViewSet, basename='exercises')
router.register(r'personal_plan', PersonalPlanViewSet, basename='personal_plan')
router.register(r'personal_plan_exercises', PersonalPlanExerciseViewSet, basename='personal_plan_exercises')
router.register(r'persona_goal', PersonalGoalViewSet, basename='persona_goal')
router.register(r'completedworkouts', CompletedWorkoutViewSet, basename='completedworkouts')
router.register(r'exercisefeedback', ExerciseFeedbackViewSet, basename='exercisefeedback')
router.register(r'workoutsessions', WorkoutSessionViewSet, basename='workoutsessions')

urlpatterns = [
    path('', include(router.urls)),
]
